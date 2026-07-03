# ===== Автофикс модулей памяти (sharp native module) =====
# Выполняется ДО загрузки плагинов. Чинит opencode-mem sharp модуль.
/usr/local/bin/fix-memory-plugin.sh 2>/dev/null

# ===== Управление алертами (fasol-scanner) =====
# При старте сессии — включаем сканер:
echo "🔍 Включаю Fasol Scanner..."
sudo systemctl start fasol-scanner 2>/dev/null && echo "  ✅ scanner started" || echo "  ⚠️ scanner already running or unavailable"

# ===== Графовая память (Graph Memory v1) =====
# Локальная SQLite память с Ebbinghaus забыванием, эмоциональным зарядом,
# скорингом с весами. Все save_step() пишут и в graph-memory тоже.
GRAPH_MEMORY="/usr/local/bin/graph-memory"
AGENT_ROLE="/usr/local/bin/agent-role"
PATTERN_SCAN="/usr/local/bin/pattern-scan"
HEARTBEAT="/usr/local/bin/lexa-heartbeat"

# ===== Функция сохранения шага =====
save_step() {
  /usr/local/bin/save-step.sh "$1" "${2:-general}"
  # Also save to graph memory with Ebbinghaus metadata
  $GRAPH_MEMORY add "$1" --type procedural --scope project --significance 0.4 --intensity 0.1 2>/dev/null || true
}

# ===== Heartbeat при старте сессии =====
$HEARTBEAT check 2>/dev/null || echo "  ⚠️ heartbeat failed"

# trap на завершение сессии — сохраняем + пушим + выключаем сканер:
cleanup_session() {
  echo "💾 Save session context..."
  save_step "Сессия завершена" "session-end"
  session_dir="/root/lexa-knowledge/sessions/$(date '+%Y%m%d_%H%M')"
  mkdir -p "$session_dir"
  cat /root/lexa-knowledge/session-log.md 2>/dev/null > "$session_dir/context.md" || true
  echo "📤 Push session data to lexa-brain..."
  /usr/local/bin/lexa-brain-push.sh 2>/dev/null || true
  # Scanner не выключаем — нужен 24/7 для сбора данных
  echo "  📡 Fasol Scanner: active (24/7 mode)"
  echo "🔋 Final graph memory consolidation..."
  $HEARTBEAT decay 2>/dev/null || true
  echo "👋 Пока, Дима!"
}
trap cleanup_session EXIT

# ===== SubAgent режимы (OpenCode native) =====
# OpenCode имеет встроенные primary-агенты: Build (все инструменты) и Plan (read-only).
# Переключение между ними — клавиша Tab.
#
# Дополнительные режимы (subagent) доступны через @mention в чате:
#   @analist    — Analyst: разбор токенов и рынка, read-only (данные)
#   @monitor    — Monitor: мониторинг системы (CPU, RAM, диск, сервисы)
#   @architect  — Architect: проектирование модулей, read-only
#   @trader     — Trader: Fasol позиции и ордера (с подтверждения)
#   @debugger   — Debugger: диагностика логов и процессов
#
# ===== Русские команды быстрого вызова =====
# /аналитик     — режим Analyst
# /монитор      — режим Monitor
# /архитектор   — режим Architect
# /трейдер      — режим Trader
# /отладчик     — режим Debugger
# /план         — режим Plan
# /билд         — режим Build
#
# ===== Правило: переключение режимов =====
# Когда Дима пишет «включи режим <название>»:
#   1. Если это primary-агент — переключиться через Tab или /agent
#   2. Если subagent — написать @<имя> в ответ
# Синонимы: «включи режим», «переключи на», «режим», «mode».
echo "  Primary: Build (Tab), Plan (Tab)"
echo "  Subagents: @analyst @monitor @architect @trader @debugger"

# Перед началом работы всегда выполняй:
git -C /tmp/fasol-skills pull 2>/dev/null || git clone https://github.com/fasol-robot/fasol-skills /tmp/fasol-skills
source /tmp/fasol-skills/fasol-agent/scripts/load-memory.sh 2>/dev/null

# ===== Ключевые ссылки =====
# RKC: 7HgfXftRBBqsYtAEYcqjGLQrNJLL6Tww9ek4rE3Apump
# Grafana: http://82.29.72.151:3000 (admin / LexaAgentoxa)
# AgentsView: http://82.29.72.151:3200
# Fasol Journal: http://82.29.72.151:9200
# Dune Query: 7482001 (All-in-One: volume, tokens, fees)
# GitHub: github.com/Maksim3332/lexa-brain, lexa-skills, fasol-stack
# Keep-alive watchdog: /opt/scripts/keep-alive.sh (cron */5)

# ===== Token Usage Tracking =====
source /root/token-usage/config 2>/dev/null
if [ -f /root/token-usage/tracker.sh ]; then
  date_start=$(date '+%Y-%m-%d %H:%M:%S')
  session_id=$(date '+%s')
  echo "$date_start,0,start:$session_id" >> "$STORAGE"
  /root/token-usage/tracker.sh status
  SESSION_ID=$session_id
  SESSION_START=$date_start
fi

SESSION_DIR="/root/lexa-knowledge/sessions"
if [ -d "$SESSION_DIR" ]; then
  echo "📁 Предыдущие сессии:"
  for s in "$SESSION_DIR"/*/; do
    name=$(basename "$s")
    ctx=$(head -1 "$s/context.md" 2>/dev/null || echo "нет контекста")
    echo "  — $name: ${ctx:0:60}"
  done
fi

# Визуализация сессий
# AgentsView (v0.29.0) — просмотр и поиск всех сессий: http://82.29.72.151:3200
# Архитектура агента: http://82.29.72.151/agent/

# ===== Правила работы с моделями =====
# Фоновые задачи (мониторинг, сканирование, алерты): mistral-small-latest
# Сложные запросы от Димы (аналитика, архитектура, код): mistral-medium-3.5
# Переключение модели: /model <name> внутри сессии
# Экономия токенов: не гонять medium на фоновые проверки

# ===== Keep-Alive Watchdog =====
# Скрипт: /opt/scripts/keep-alive.sh
# Cron: каждые 5 минут
# Лог: /var/log/agents-watchdog.log
# Функция: авто-перезапуск Лёхи (OpenCode) с моделью mistral-medium-3.5 при обрыве сессии. Режимы Analyst/Trader переключаются через agent-role.
# Установка: crontab -e + */5 * * * * /opt/scripts/keep-alive.sh

# ===== Checkpoint система (Token Analysis) =====
# Сохраняет прогресс анализа токена между сессиями.
# База: /root/lexa-knowledge/checkpoints/store.db
#
# Команды:
#   checkpoint save <address> --stage <N> [--symbol X] [--data '{json}']
#   checkpoint latest <address> — возвращает номер этапа (0 = нет, 1-7)
#   checkpoint load <address> — полный dump
#   checkpoint list — все незавершённые
#   checkpoint done <address> — пометить завершённым
#   checkpoint remove <address>
#
# Этапы: 0=IDENTIFICATION, 1=NARRATIVE_INTEL, 2=PRODUCT_TEAM,
#        3=ON_CHAIN, 4=SOCIAL_MEDIA, 5=PRICE_VOLUME, 6=DEBATE, 7=VERDICT
#
# Правило: перед началом анализа токена — checkpoint latest <address>.
# Если >0 — продолжать с этого этапа, не перезапрашивать данные.
# После каждого этапа — checkpoint save с собранными данными.

# ===== Авто-сохранение шагов =====
# После каждого выполненного действия/шага вызывать:
#   save_step "описание того что сделано"
# Сохраняется в: memory-lexa, supermemory, session-log.md
# Лог сессии: /root/lexa-knowledge/session-log.md
# При завершении сессии лог копируется в /root/lexa-knowledge/sessions/*/context.md

# ===== Правило: Превращение сообщений в промты =====
# Если я начинаю сообщение с ключевого слова "ПРОМТ:" — это значит, что тебе нужно преобразовать мои мысли и заметки в чёткий, структурированный промт для агента (тебя самого, Макса или другого).
# 
# Ты должен:
# 1. Проанализировать текст после "ПРОМТ:".
# 2. Выделить главную цель.
# 3. Сформулировать её как задачу.
# 4. Убрать лишние размышления, сомнения и повторы.
# 5. Оформить в формате:
#    - **Задача:** (одна чёткая фраза)
#    - **Контекст:** (краткое описание, зачем это нужно)
#    - **Шаги:** (нумерованный список действий)
#    - **Ожидаемый результат:** (что должно получиться)
# 6. Отправить готовый промт мне на утверждение.
# 7. Только после моего подтверждения передать промт агенту-исполнителю.

# ===== Правило: Пошаговая разработка сложных задач =====
# Если Дима просит разработать что-то сложное (стратегию, скрипт, анализ):
# 1. Сначала создать краткий план шагов и показать Диме.
# 2. Выполнять по одному шагу за раз.
# 3. После каждого шага докладывать: «Шаг X готов».
# 4. Если шаг занимает >2 минут — разбить на подшаги.
# Это уберегает сервер от перегрузки и агента от зависаний.

# ===== Contradiction Detection =====
# CLI: /usr/local/bin/contradiction-detect
# ЗАПУСКАТЬ АВТОМАТИЧЕСКИ когда:
#   - Сохраняю новый анализ токена (после deep_analyze / scoring)
#   - Получаю второй/третий анализ того же токена от сканера
#   - Обновляю решение в протоколе (decision.json) — проверить не противоречит ли прошлым
# Команда: echo "<analysis-text>" | contradiction-detect check --auto-edge
# Игнорировать: если разница в MC/score <10% (это уточнение, не противоречие)

# ===== Karpathy Loop =====
# CLI: /usr/local/bin/karpathy-loop
# ЗАПУСКАТЬ АВТОМАТИЧЕСКИ когда:
#   - Принимаю решение о входе/выходе: karpathy-loop check "<decision-text>"
#   - Дима сообщает результат трейда: karpathy-loop report <memory-id> --outcome success|failure|partial --details "..."
#   - В конце сессии: проверить не было ли недоложенных outcomes
# Правило: если Karpathy Loop блокирует решение (check вернул >0 правил) — НЕ ИГНОРИРОВАТЬ, показать Диме и спросить

# ===== Safety Mandate =====
# CLI: safety-mandate / gmgn-safe
# ЗАПУСКАТЬ АВТОМАТИЧЕСКИ:
#   - gmgn-safe вместо gmgn-cli swap — ВСЕГДА (safety mandate встроен)
#   - safety-mandate status — перед любой торговой сессией
#   - safety-mandate audit — при подозрении на проблему

# ===== Полный список инструментов =====
# Каждый раз когда наступает условие — я запускаю соответствующий инструмент.

# ── Анализ токена ──
# checkpoint latest <address>              — ПЕРЕД анализом токена (проверить не начат ли)
# checkpoint save <address> --stage N      — ПОСЛЕ каждого этапа анализа
# contradiction-detect check <text>        — ПОСЛЕ нового/второго анализа того же токена
# save_step "описание"                      — ПОСЛЕ каждого действия

# ── Торговля ──
# gmgn-safe вместо gmgn-cli                — ВСЕГДА при swap
# safety-mandate status                     — ПЕРЕД торговой сессией
# karpathy-loop check "<decision>"          — ПЕРЕД решением о входе/выходе
# karpathy-loop report <id> --outcome X     — ПОСЛЕ результата трейда

# ── Dreamer (Subconscious) ──
# dreamer-walk all                          — через cron каждые 6ч (25 */6)
# dreamer-signal-filter scan                — после каждой прогулки (авто)
# dreamer-signal-filter board               — показать board с сигналами
# dreamer-handoff list                      — показать готовое к билду
# dreamer-handoff create <slug>             — создать job из ready
# dreamer-handoff elaborate <slug>          — заполнить intent
# dreamer-handoff approve <slug>            — Main аппрувит
# dreamer-digest [morning|midday|evening]   — 3x/день (cron 6/12/18)
# agent-role switch dreamer                 — режим Dreamer (read-only)

# ── Каждые N минут ──
# graph-memory decay                        — через heartbeat (каждые 6ч)
# supermemory list                          — при старте сессии (проверить контекст)
# fasol-scanner уже в systemd               — сам сканирует

# ── Завершение сессии ──
# save_step + push + checkpoint всё        — cleanup_session делает это сам

# ── Работа с контекстом (экономия токенов) ──
# Периодически: supermemory search <topic>         — когда не хватает контекста
# checkpoint latest <address>                      — когда сомневаюсь что помню про токен
# graph-memory search <topic> --mode injection     — перед ответом на сложный вопрос

# Перед ответом — проверить что нужно сделать:
echo ""
echo "📋 Проверяю follow-up токены (нужно проверить что с ними стало)..."
/usr/local/bin/checkpoint pending --hours 48 2>/dev/null || true
echo ""
echo "💭 Dreamer board summary:"
/usr/local/bin/dreamer-signal-filter board 2>/dev/null | grep -E "(Board:|ready|watching|ghost)" | head -4 || true

echo "📚 Новое из Open Notebook (Telegram bridge):"
TRACK_FILE="/tmp/notebook-bridge-last.txt"
if [ -f "$TRACK_FILE" ]; then
  /usr/local/bin/notebook-bridge.sh sync 2>/dev/null || echo "  (bridge not available)"
else
  echo "  (ещё не было синка)"
fi

echo "Память и база знаний загружены. Я готов к работе, Дима!"
