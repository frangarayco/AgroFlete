export type UserRole = 'admin' | 'transporter' | 'requester';

export interface User {
  id: string;
  email: string;
  fullName: string;
  phone: string;
  role: UserRole;
  avatarUrl?: string;
  rating?: number;
  isVerified: boolean;
  createdAt: string;
}
