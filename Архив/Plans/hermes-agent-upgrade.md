# Project Hermes — Self-Improving AI Agent

> Цель: превратить Lexa (меня) в fully autonomous self-improving agent 
> по образу Hermes Agent от Nous Research, но с нашей спецификой.

## Stack

- **GitHub** — репозиторий для конфигов, скиллов, планов, execution traces
- **Obsidian** — локальная база знаний с графом связей и markdown
- **opencode-supermemory-max** — расширенная векторная память поверх opencode-mem
- **Self-evolving skills** — авто-генерация и установка скиллов через рефлексию
- **Fasol Journal** — Telegram gateway + дашборд

---

## Фаза 0: GitHub + Основа (СЕЙЧАС)

- [ ] Установить SSH ключ на GitHub
- [ ] Создать репозиторий `lexa-brain` (конфиги, память, скиллы, traces)
- [ ] Настроить авто-пуш сессий в репозиторий
- [ ] gh CLI авторизация

**Репозитории:**
| Название | Назначение |
|----------|------------|
| `lexa-brain` | Память, планы, конфиги, execution traces |
| `lexa-skills` | Набор self-made скиллов |
| `fasol-stack` | Инфраструктура (exporter, journal и т.д.) |

## Фаза 1: Memory System Upgrade

- [x] Obsidian vault: `/root/lexa-obsidian/` — markdown база знаний (+ семьлинки на реальные файлы)
- [x] REST API памяти: `/api/memory/*` на порту 9200 (встроен в Fasol Journal)
  - `/search` — гибридный поиск (FTS + векторная)
  - `/knowledge` — FTS по знаниям
  - `/vector` — векторный поиск
  - `/save` — сохранение в векторную память
  - `/sessions` — история сессий
  - `/stats` — статистика
- [x] Tier 1: AGENTS.md (всегда в контексте) ✅
- [x] Tier 2: SQLite FTS + Obsidian ✅
- [ ] Tier 3: Векторная память через supermemory-max (ждёт API ключа)
- [ ] opencode-supermemory-max: установка и интеграция (отложено, нужен API ключ supermemory.ai)

## Фаза 2: Self-Evolving Skills

- [ ] Создать протокол само-генерации скилла:
  1. Выполнить задачу (5+ вызовов инструментов)
  2. Извлечь паттерн из execution trace
  3. Сгенерировать SKILL.md
  4. Установить через skill()
- [ ] Curator: фоновый скрипт очистки устаревших/дублирующихся скиллов
- [ ] Pin/Unpin система для критических скиллов

## Фаза 3: GEPA — Офлайн Оптимизация

- [ ] Collect execution traces в репозиторий
- [ ] LLM-as-judge: оценка эффективности скиллов
- [ ] Авто-PR с улучшенными версиями скиллов

## Фаза 4: Cron + Автономность

- [ ] Система джобов на человеческом языке (как Hermes cron)
- [ ] Ежедневные/еженедельные ритуалы (market regime, session tracking)
- [ ] Telegram delivery для всех джобов

## Фаза 5: Multi-Profile

- [ ] Профили для разных ролей:
  - `default` — я (трейдер/аналитик)
  - `researcher` — глубокий анализ токенов
  - `builder` — реализация кода
  - `oracle` — архитектурные решения

---

## Ресурсы

- Hermes Agent: https://github.com/NousResearch/hermes-agent
- Obsidian: https://obsidian.md
- opencode-supermemory-max: TBD
- GEPA Paper: ICLR 2026 Oral

Статус: **Фаза 0 ✅ → Фаза 1 🔄 (90%, ждёт supermemory API ключ)**
Последнее обновление: 2026-05-27
