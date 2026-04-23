# AgroFlete 🚛🌾

> Marketplace digital de fletes agropecuarios para Argentina

## Descripción

AgroFlete conecta productores y compradores con transportistas habilitados para el traslado de hacienda, granos y otros productos agropecuarios. La plataforma garantiza trazabilidad documental, seguimiento GPS en tiempo real y validación de habilitaciones (SENASA).

## Estructura del Proyecto

```
agroflete/
├── apps/
│   ├── backend/          # API REST con NestJS + TypeScript
│   └── mobile/           # App móvil con Expo (React Native)
├── packages/
│   └── shared/           # Tipos, DTOs y constantes compartidas
├── infra/
│   ├── postgres/         # Scripts de inicialización de DB
│   └── redis/            # Config de Redis
├── docker-compose.yml    # Orquestación de servicios
└── pnpm-workspace.yaml   # Configuración del monorepo
```

## Requisitos

- Node.js >= 20
- pnpm >= 9
- Docker + Docker Compose

## Primeros pasos

### 1. Instalar dependencias

```bash
pnpm install
```

### 2. Configurar variables de entorno

```bash
cp apps/backend/.env.example apps/backend/.env
# Editar el .env con tus valores
```

### 3. Levantar la infraestructura (PostgreSQL + Redis)

```bash
pnpm docker:up
```

### 4. Correr el backend

```bash
pnpm backend
```

### 5. Correr la app mobile (en otra terminal)

```bash
pnpm mobile
```

## Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| App móvil | Expo / React Native |
| Backend | NestJS + TypeScript |
| Base de datos | PostgreSQL |
| Cache / Real-time | Redis |
| Contenedores | Docker + Docker Compose |
| GPS/Mapas | Google Maps / Mapbox |
| Notificaciones | Firebase + Twilio SMS |
| Storage | AWS S3 / Cloudflare R2 |

## Documentación

- API Docs (Swagger): `http://localhost:3000/api/docs`
- Health Check: `http://localhost:3000/api/v1/health`

---

AgroFlete © 2026 — Documento confidencial
