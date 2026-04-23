export type TripStatus =
  | 'pending'
  | 'matched'
  | 'in_progress'
  | 'completed'
  | 'cancelled';

export type CargoType = 'hacienda' | 'granos' | 'frutas' | 'otro';

export interface Location {
  latitude: number;
  longitude: number;
  address: string;
  city: string;
  province: string;
}

export interface Trip {
  id: string;
  requesterId: string;
  transporterId?: string;
  status: TripStatus;
  cargoType: CargoType;
  originLocation: Location;
  destinationLocation: Location;
  scheduledDate: string;
  estimatedWeight: number; // en kg
  agreedPrice?: number;
  commissionRate: number;  // entre 0.10 y 0.15
  notes?: string;
  createdAt: string;
  updatedAt: string;
}
