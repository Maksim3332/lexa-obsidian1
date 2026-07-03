# Installed Tools — Session 2026-06-10

## Zero CLI

- **Репозиторий:** github.com/igus_ai/zero (now @zeroxyz/cli)
- **Версия:** v0.0.45
- **Путь:** `/usr/bin/zero`
- **Назначение:** search engine for AI agent capabilities (Solana tokens, blockchain data, etc.)
- **Использование:** `zero search <query>`

## Agent-Skills (Addy Osmani)

- **Репозиторий:** github.com/addyosmani/agent-skills (49.4K★)
- **Путь:** `/tmp/agent-skills/`
- **Лицензия:** MIT
- **Скиллы (20+):** api-design, testing, ci-cd, debugging, frontend, security, react, python, node, sql, docker, git, graphql, rest, observability, performance, accessibility, shell, typescript, nextjs
- **Формат:** Каждый скилл = markdown + spec + template

## Walrus Memory

- **SDK:** `memwal` (Python), v0.1.4
- **Назначение:** Portable encrypted memory layer на Sui blockchain
- **Статус:** ⏳ Установлен, ждёт ключи (MEMWAL_PRIVATE_KEY + MEMWAL_ACCOUNT_ID)
- **Регистрация:** memory.walrus.xyz
- **Документация:** https://memory.walrus.xyz/skills/setup

## Open Notebook (Self-hosted NotebookLM)

- **Репозиторий:** github.com/lfnovo/open-notebook (v1.9.0)
- **Деплой:** Docker Compose
- **Порты:** Web UI 8502, REST API 5055, SurrealDB 8000
- **URL:** http://82.29.72.151:8502
- **Бэкенд:** SurrealDB (векторное хранилище)
- **Статус:** ✅ Production

## Fasol Skills (Agent API)

- **Репозиторий:** github.com/fasol-robot/fasol-skills
- **Путь:** `/tmp/fasol-skills/fasol-agent/skills/`
- **Новые под-скиллы (2026-06-10):**
  - `smart-money-stream.md` — SSE feed of curated SM cohort swaps
  - `calls-stream.md` — SSE feed of followed callers' publications
  - `changelog.md` — обновлён (3 фичи: SM stream, Calls, 400 fix)
