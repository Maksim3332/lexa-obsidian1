# Session 28 May 2026 — Obsidian Full Load + supermemory-max

## Что сделано

1. **Opencode-supermemory-max v2.1.0** установлен и настроен
   - Форк от kandotrun: incremental capture, dedup, signal extraction, entity context
   - API ключ supermemory.ai сохранён в конфиге
   - oh-my-opencode контекст-хук отключён
   - Ре-инжект контекста каждые 10 сообщений
   - signalExtraction: true (сохраняет только важное)

2. **Obsidian vault** полностью загружен
   - 183 файла, 80 markdown в 7 разделах
   - Knowledge/: стратегии, правила, токены, сессии, паттерны
   - Plans/: проекты (Hermes Phase 1), конфиги агентов
   - Trading/: логи сделок, точность
   - Sessions/: вся история сессий
   - Infrastructure/: архитектура, сервисы
   - Memory/: документация памяти
   - Configs/: конфиги opencode и плагинов
   - Wiki-линки между всеми разделами (граф связей)

3. **Авто-синк** через cron (каждый час)
   - lexa-vault-sync.sh копирует новые файлы в Obsidian
   - alwaysUpdateLinks: true

## История исправления памяти
- Диагностирована: auto-capture opencode-mem не был настроен
- Починено: добавлен opencodeProvider → memories теперь создаются
- Ручное сохранение: 5 пропущенных memory из 27 May
