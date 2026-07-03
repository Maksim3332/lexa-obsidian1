# Project Hermes — Self-Improving AI Agent

> Цель: превратить Lexa (меня) в fully autonomous self-improving agent 
> по образу Hermes Agent от Nous Research, но с нашей спецификой.

## Stack

- **GitHub** — репозиторий для конфигов, скиллов, планов, execution traces
- **Obsidian** — локальная база знаний с графом связей и markdown
- **opencode-supermemory-max** — расширенная векторная память
- **Self-evolving skills** — авто-генерация и установка скиллов через рефлексию
  - `proto-skill-gen.sh` — генератор SKILL.md
  - `skill-curator.sh` — чистка дубликатов
  - `skill-pin.sh` — pin/unpin критических скиллов
- **Multi-Profile** — переключение ролей через `switch-profile.sh`

---

## Фаза 0: GitHub + Основа

- [x] SSH ключ на GitHub
- [x] Репозиторий `lexa-brain` (конфиги, память, скиллы, traces)
- [x] Авто-пуш сессий в репозиторий (`lexa-brain-push.sh`)
- [x] gh CLI авторизация

**Репозитории:**
| Название | Назначение |
|----------|------------|
| `lexa-brain` | Память, планы, конфиги, execution traces |
| `lexa-skills` | Набор self-made скиллов |
| `fasol-stack` | Инфраструктура (exporter, scanner) |

## Фаза 1: Memory System Upgrade

- [x] Obsidian vault: `/root/lexa-obsidian/` — markdown база знаний
- [x] Tier 1: AGENTS.md (всегда в контексте)
- [x] Tier 2: SQLite FTS + Obsidian
- [x] Tier 3: Векторная память через supermemory-max (ключ есть, плагин работает)
- [x] `memory-lexa` CLI — локальный бэкап SQLite
- [x] `/root/lexa-knowledge/` — сессии, решения, паттерны

## Фаза 2: Self-Evolving Skills ✅

- [x] **ProtoSkill Generator** — `/usr/local/bin/proto-skill-gen.sh`
  - Принимает: name, description, instructions
  - Создаёт: `/root/.agents/skills/<name>/SKILL.md`
- [x] **Curator** — `/usr/local/bin/skill-curator.sh`
  - Сканирует дубликаты, пустые описания, oversized файлы
- [x] **Pin/Unpin** — `/usr/local/bin/skill-pin.sh`
  - `pin <name>` / `unpin <name>` / `list`
  - Маркер: `.pinned` файл в директории скилла
- [x] **Тест:** сгенерирован `quick-scan` скилл

## Фаза 3: GEPA — Офлайн Оптимизация ✅

- [x] Collect execution traces в репозиторий (`trace-collector.sh`)
- [x] LLM-as-judge: оценка эффективности скиллов (`skill-judge.sh`)
- [x] Авто-PR с улучшенными версиями скиллов (`auto-pr.sh`)

## Фаза 4: Cron + Автономность ✅

- [x] Система джобов на человеческом языке (`hermes-cron.sh`)
- [x] Ежедневные/еженедельные ритуалы (`morning-routine.sh`, `session-track.sh`, `weekly-review.sh`)
- [ ] Telegram delivery для всех джобов (пока алерты отключены)

## Фаза 5: Multi-Profile ✅

- [x] **default** — трейдер/аналитик (текущий)
- [x] **researcher** — глубокий анализ токенов
- [x] **builder** — разработка
- [x] **oracle** — архитектура/ревью
- [x] **switch-profile.sh** — переключение профилей
  - Авто-pin/unpin скиллов под профиль
  - `switch-profile.sh list` — список профилей
  - `switch-profile.sh <name>` — смена

---

## Ресурсы

- Hermes Agent: https://github.com/NousResearch/hermes-agent
- Obsidian: https://obsidian.md
- GEPA Paper: ICLR 2026 Oral

**Статус: Фаза 0 ✅ → Фаза 1 ✅ → Фаза 2 ✅ → Фаза 3 ✅ → Фаза 4 ✅ → Фаза 5 ✅ || Telegram delivery ❌**
**Последнее обновление: 2026-06-10**
