import axios from 'axios';

const BASE_URL = process.env.EXPO_PUBLIC_API_URL ?? 'http://localhost:3000/api/v1';

export const apiClient = axios.create({
  baseURL: BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor: agregar token JWT a cada request
apiClient.interceptors.request.use(
  (config) => {
    // TODO: leer token desde SecureStore
    // const token = await SecureStore.getItemAsync('auth_token');
    // if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
  },
  (error) => Promise.reject(error),
);

// Interceptor: manejo global de errores
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // TODO: redirigir a login / refrescar token
    }
    return Promise.reject(error);
  },
);
