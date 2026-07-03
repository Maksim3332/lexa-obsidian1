# Архитектура Signal Dashboard (MemeSniper SaaS)

## 1. Общая архитектура

```
┌─────────────────────────────────────────────────────────┐
│                   Клиент (Браузер)                       │
│  Frontend: React + TypeScript + Tailwind CSS             │
│  Recharts (графики), WebSocket (real-time)               │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP/WS
                     ▼
┌─────────────────────────────────────────────────────────┐
│              API Gateway (Nginx + Let's Encrypt)         │
│  HTTPS, rate limiting, статика                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Backend (FastAPI / Python)                  │
│  REST API endpoints                                      │
│  WebSocket для real-time сигналов                        │
│  Celery workers для фоновых задач                        │
│  Auth (JWT + Clerk/Auth0)                                │
└────────┬────────────┬────────────┬──────────────────────┘
         │            │            │
         ▼            ▼            ▼
┌────────────┐ ┌────────────┐ ┌──────────────────────────┐
│ PostgreSQL │ │  Redis     │ │  TimescaleDB              │
│ (пользоват. │ │ (кэш,      │ │  (рыночные временные     │
│  подписки,  │ │  очереди)  │ │   ряды: цены, объёмы)    │
│  настройки) │ │            │ │                          │
└────────────┘ └────────────┘ └──────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────┐
│              Внешние интеграции                          │
│  📡 Telethon — Telegram-каналы (Колонка 1)              │
│  🧠 GMGN API — Smart Money, KOL (Колонка 2)            │
│  🐦 Twitter/X API — соцсети (Колонка 3)                │
│  🦅 Birdeye API — рыночные данные                       │
│  📊 Dune API — ончейн-аналитика                         │
│  💳 Stripe/NowPayments — платежи                        │
└─────────────────────────────────────────────────────────┘
```

## 2. Стек технологий

### Frontend
| Компонент | Технология |
|-----------|-----------|
| Фреймворк | React 18+ / TypeScript |
| Стили | Tailwind CSS + CSS Modules |
| Графики | Recharts / Chart.js |
| Real-time | WebSocket (native) |
| Стейт-менеджмент | Zustand (легковесный) |
| Сборка | Vite |
| HTTP-клиент | fetch + WebSocket |

### Backend
| Компонент | Технология |
|-----------|-----------|
| API | FastAPI (Python 3.12) |
| ORM | SQLAlchemy 2.0 + Alembic |
| Фоновые задачи | Celery + Redis |
| Real-time | WebSocket (FastAPI native) |
| Аутентификация | Clerk / Auth0 (JWT) |
| Платежи | Stripe (фиат) + NowPayments (крипта) |
| Мониторинг | Sentry |

### База данных
| Компонент | Технология |
|-----------|-----------|
| Основная | PostgreSQL 16 |
| Временные ряды | TimescaleDB (extension) |
| Кэш | Redis 7 |
| Очереди | Redis (Celery broker) |

### DevOps
| Компонент | Технология |
|-----------|-----------|
| Контейнеризация | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| Прокси | Nginx |
| SSL | Let's Encrypt (certbot) |
| Логи | Sentry + Prometheus (опционально) |

## 3. Структура API-эндпоинтов

### Auth
```
POST   /api/auth/register          — Регистрация
POST   /api/auth/login             — Логин
POST   /api/auth/logout            — Выход
GET    /api/auth/me                — Текущий пользователь
POST   /api/auth/refresh           — Refresh JWT
```

### Подписки / Платежи
```
GET    /api/subscription/plans     — Список тарифов
POST   /api/subscription/create    — Создать подписку
POST   /api/subscription/cancel    — Отменить
GET    /api/subscription/status    — Статус подписки
POST   /api/payment/stripe-webhook — Webhook Stripe
POST   /api/payment/crypto-webhook — Webhook NowPayments
```

### Колонка 1 — TG Calls
```
GET    /api/v1/tg-calls            — Список последних сигналов из TG
GET    /api/v1/tg-calls/:id        — Детали сигнала
POST   /api/v1/tg-channels         — Добавить канал (user)
DELETE /api/v1/tg-channels/:id     — Удалить канал (user)
```

### Колонка 2 — Smart Money
```
GET    /api/v1/smart-money/trending  — Трендовые у SM
GET    /api/v1/smart-money/clusters  — Кластеры SM
GET    /api/v1/smart-money/token/:address  — SM по токену
```

### Колонка 3 — Social Radar
```
GET    /api/v1/social/mentions/:address      — Упоминания токена
GET    /api/v1/social/sentiment/:address     — Тональность
GET    /api/v1/social/influencers/:address   — Инфлюенсеры
GET    /api/v1/social/trending               — Всплески мет
```

### Токены / Рыночные данные
```
GET    /api/v1/token/:address          — Полные данные токена
GET    /api/v1/token/:address/price    — История цены
GET    /api/v1/token/:address/trades   — Сделки
POST   /api/v1/tokens/batch            — Batch lookup
```

### WebSocket
```
WS     /api/ws/tg-calls              — Real-time новые сигналы
WS     /api/ws/social-spikes         — Real-time всплески в соцсетях
WS     /api/ws/notifications         — Уведомления пользователя
```

### Админка
```
GET    /api/admin/stats              — Статистика системы
GET    /api/admin/users              — Список пользователей
POST   /api/admin/announce           — Рассылка
```

## 4. Схема базы данных

### users
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clerk_id VARCHAR(255) UNIQUE NOT NULL,    -- ID из Clerk/Auth0
    email VARCHAR(255) UNIQUE,
    username VARCHAR(100),
    plan VARCHAR(50) DEFAULT 'free',           -- free | pro | enterprise
    subscription_status VARCHAR(50) DEFAULT 'inactive',
    subscription_expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### tg_channels (пользовательские каналы)
```sql
CREATE TABLE tg_channels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    username VARCHAR(255) NOT NULL,             -- @channel
    title VARCHAR(255),
    active BOOLEAN DEFAULT TRUE,
    last_message_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### tg_calls (сигналы из TG)
```sql
CREATE TABLE tg_calls (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    address VARCHAR(64) NOT NULL,              -- контракт токена
    source_channel VARCHAR(255),               -- @channel
    source_title VARCHAR(255),
    message_text TEXT,
    token_symbol VARCHAR(50),
    token_name VARCHAR(255),
    market_cap NUMERIC,
    liquidity NUMERIC,
    volume_24h NUMERIC,
    holder_count INTEGER,
    smart_degen_count INTEGER,
    renowned_count INTEGER,
    score_def1 NUMERIC,                        -- оценка агента
    called_at TIMESTAMPTZ,                     -- когда позвали
    created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_tg_calls_address ON tg_calls(address);
CREATE INDEX idx_tg_calls_created ON tg_calls(created_at DESC);
```

### token_prices (TimescaleDB hypertable)
```sql
CREATE TABLE token_prices (
    address VARCHAR(64) NOT NULL,
    price NUMERIC NOT NULL,
    volume NUMERIC,
    market_cap NUMERIC,
    liquidity NUMERIC,
    ts TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
SELECT create_hypertable('token_prices', 'ts');
CREATE INDEX idx_token_prices_addr_ts ON token_prices(address, ts DESC);
```

### social_mentions
```sql
CREATE TABLE social_mentions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    address VARCHAR(64),
    platform VARCHAR(50) DEFAULT 'twitter',     -- twitter, reddit, discord
    mention_text TEXT,
    author VARCHAR(255),
    author_followers INTEGER,
    sentiment NUMERIC,                         -- -1.0 .. 1.0
    engagement INTEGER,                        -- likes + retweets
    mentioned_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_social_mentions_addr ON social_mentions(address);
CREATE INDEX idx_social_mentions_ts ON social_mentions(mentioned_at DESC);
```

### subscriptions (платежи)
```sql
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    plan VARCHAR(50) NOT NULL,
    stripe_subscription_id VARCHAR(255),
    crypto_payment_id VARCHAR(255),
    status VARCHAR(50),                         -- active, cancelled, expired
    amount NUMERIC,
    currency VARCHAR(10),
    period_start TIMESTAMPTZ,
    period_end TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

## 5. План монетизации

### Тарифы

| План | Цена | Колонки | TG-каналы | Исторические данные | API |
|------|------|---------|-----------|-------------------|-----|
| Free | $0 | 1 (TG demo) | 1 канал | 24ч | нет |
| Pro | $29/мес | 3 колонки | 5 каналов | 7 дней | 1000 req/день |
| Enterprise | $99/мес | 3 колонки | ∞ каналов | 30 дней | 10000 req/день |
| Whitelabel | $499/мес | Кастом | ∞ | ∞ | без лимитов |

### Способы оплаты
- **Фиат**: Stripe (карты, Google Pay, Apple Pay)
- **Крипта**: NowPayments (USDT, SOL, ETH, BTC)
- **Скидка**: -20% при оплате за год

### Триггеры конверсии
- Бесплатный пробный период 7 дней (Pro)
- Тизер: "У вас осталось 3 из 5 сигналов сегодня"
- После просмотра 10 токенов в демо → показать план Pro

## 6. Колонка 3 — Social Radar (предложение)

### Что делает
- Мониторит Twitter/X на упоминания токенов
- Анализирует тональность (позитив/негатив/нейтрально)
- Выявляет инфлюенсеров, пишущих о токене
- Находит "мету" (трендовую тему) до попадания в TG

### Источники данных
- **Twitter/X API v2** — поиск твитов по ключевым словам
- **MCP-x-intelligence** (уже настроен) — search_viral_content, get_trending_topics
- **Narrative Intelligence** — классификация нарративов (из протокола v3)

### Отображение
- График упоминаний за 24ч / 7д
- Облако слов (ключевые фразы)
- Список инфлюенсеров с фолловерами
- Общий сентимент-скор

## 7. Дорожная карта

### MVP (текущий этап — работает)
- [x] HTML-дашборд с 3 колонками
- [x] TG-парсинг через Telethon
- [x] GMGN интеграция
- [x] 3 языка (zh/en/ru)
- [ ] Сохранение сессии TG (сделано)

### Phase 1 — Backend (1-2 недели)
- [ ] FastAPI сервер с эндпоинтами
- [ ] PostgreSQL + TimescaleDB
- [ ] Celery фоновые задачи
- [ ] WebSocket для real-time
- [ ] Сохранение TG сигналов в БД
- [ ] Docker Compose для деплоя

### Phase 2 — Frontend React (2-3 недели)
- [ ] React + TypeScript + Tailwind
- [ ] Компонентная архитектура
- [ ] Recharts графики
- [ ] WebSocket-client
- [ ] Тёмная/светлая тема
- [ ] Адаптивный дизайн

### Phase 3 — Social Radar (1 неделя)
- [ ] Twitter/X парсинг
- [ ] Анализ тональности (NLP)
- [ ] Обнаружение мет
- [ ] Интеграция в Колонку 3

### Phase 4 — SaaS (1 неделя)
- [ ] Clerk аутентификация
- [ ] Stripe + NowPayments
- [ ] Личный кабинет
- [ ] Лимиты по тарифам
- [ ] Админка

### Phase 5 — Production (ongoing)
- [ ] Sentry мониторинг
- [ ] CI/CD (GitHub Actions)
- [ ] Nginx + SSL
- [ ] Performance оптимизация
- [ ] User onboarding
