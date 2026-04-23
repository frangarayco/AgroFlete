// DTOs (Data Transfer Objects) compartidos
// Se completan a medida que se implementan los módulos

export interface PaginationDto {
  page: number;
  limit: number;
}

export interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  limit: number;
  totalPages: number;
}

export interface ApiResponse<T = void> {
  success: boolean;
  data?: T;
  message?: string;
  errors?: string[];
}
