# Buildroom — Hermes Auto-Build

**Дата:** 2026-06-10
**Статус:** ✅ Struct + CLI ready, awaiting first build cycle

## Архитектура

Основана на [gkisokay Hermes Auto-Build guide](https://gkisokay.substack.com/p/how-to-build-a-hermes-agent-that).

### Роли (Contract Chain)

```
Dreamer (Auto-think) → Main (approval) → Coder → QA → Trust → Retention → Operator
```

### Контракты

1. `research-input` — evidence + summary от Dreamer
2. `idea-contract` — что делаем, кому нужно, почему сейчас
3. `main-review` — approved/rejected + risk score
4. `product-plan` — allowed paths, planned files, verification commands
5. `verification-delta` — confirmed/drift/regression/missing_evidence
6. `trust-report` — clean/watch/investigate

## CLI (`/usr/local/bin/buildroom.sh`)

```bash
buildroom.sh init              # создать схемы
buildroom.sh propose <title> <what> <why>  # предложить идею
buildroom.sh review <file> [decision] [risk] [score]  # ревью
buildroom.sh status            # статус комнаты
buildroom.sh from-dreamer [board|sync|clean]  # мост с Dreamer
```

## Dreamer Bridge

- `from-dreamer board` — парсит доску Dreamer, создаёт `research-input` из watching-сигналов
- Когда сигнал переходит в `ready` — автоматически создаётся `idea-contract`
- Cron: `*/30 * * * * /usr/local/bin/buildroom.sh from-dreamer board`

## Структура

```
/root/lexa-buildroom/
├── schemas/           # JSON схемы контрактов
├── examples/demo-room/
│   ├── research/      # research-inputs от Dreamer
│   ├── ideas/         # idea-contracts
│   ├── plans/         # main-review решения
│   ├── jobs/          # build jobs
│   ├── verification/  # verification reports
│   ├── trust/         # trust reports
│   └── retention/     # retention reviews
├── docs/
├── engine/
└── scripts/
```

## Guardrails

- QA проверяет независимо от Coder и Dreamer
- Coder не расширяет scope без аппрува
- Dreamer не аппрувит builds
