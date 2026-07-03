# Issues / Что сломалось

## 2026-05-16 — Knowledge dashboard не открывается
**Статус:** fixed
**Фикс:** Добавил `/knowledge/` location в nginx, alias на `/opt/system-viz/knowledge/`
**Описание:** Сделал дашборд графа знаний. Через Python HTTP сервер на :8081 — хостинг блокирует порт. Через :8080/knowledge/ — тоже не работает. Через Grafana — тоже не открывается.
**Попытки починить:**
1. Python http.server на :8081 → порт заблокирован хостингом
2. Перенёс на :8080/knowledge/ → та же проблема
3. Grafana dashboard с Mermaid → не работает
**Нужно:** Разобраться, почему внешний доступ не работает, или найти другой способ
**Связано:** knowledge dashboard, доступность

## 2026-05-15 — daily-market-regime.sh падал с ошибкой
**Статус:** fixed
**Описание:** NameError: name 'MC_RKC' is not defined — экранированные переменные в heredoc'е
**Фикс:** Убрал `\` перед `$` в print-строках
