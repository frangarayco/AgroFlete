voy-- =============================================
-- AgroFlete - Inicialización de base de datos
-- =============================================

-- Extensiones necesarias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Enum de roles de usuario
CREATE TYPE user_role AS ENUM ('admin', 'transporter', 'requester');

-- Enum de estados de viaje
CREATE TYPE trip_status AS ENUM ('pending', 'matched', 'in_progress', 'completed', 'cancelled');

-- Enum de tipos de carga
CREATE TYPE cargo_type AS ENUM ('hacienda', 'granos', 'frutas', 'otro');

COMMENT ON DATABASE agroflete IS 'Base de datos de AgroFlete - Marketplace de fletes agropecuarios';
