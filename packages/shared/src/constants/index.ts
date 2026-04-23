export const COMMISSION_RATE = {
  MIN: 0.10,
  MAX: 0.15,
  DEFAULT: 0.12,
} as const;

export const TRIP_STATUS_LABELS: Record<string, string> = {
  pending: 'Pendiente',
  matched: 'Transportista asignado',
  in_progress: 'En camino',
  completed: 'Completado',
  cancelled: 'Cancelado',
};

export const CARGO_TYPE_LABELS: Record<string, string> = {
  hacienda: 'Hacienda',
  granos: 'Granos',
  frutas: 'Frutas/Verduras',
  otro: 'Otro',
};

export const API_ROUTES = {
  AUTH: {
    LOGIN: '/auth/login',
    REGISTER: '/auth/register',
    REFRESH: '/auth/refresh',
    LOGOUT: '/auth/logout',
  },
  USERS: {
    PROFILE: '/users/me',
    UPDATE: '/users/me',
    DOCUMENTS: '/users/me/documents',
  },
  TRIPS: {
    LIST: '/trips',
    DETAIL: (id: string) => `/trips/${id}`,
    CREATE: '/trips',
    UPDATE: (id: string) => `/trips/${id}`,
    MATCH: (id: string) => `/trips/${id}/match`,
    COMPLETE: (id: string) => `/trips/${id}/complete`,
  },
} as const;
