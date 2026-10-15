export type ServiceType =
  | 'Instagram unban'
  | 'Facebook unban'
  | 'Instagram & Facebook unbans'
  | 'Ad account unban'
  | 'Hacked account recovery'
  | 'Instagram username claim'
  | 'Ban request — genuine policy violation'
  | 'Page access & ownership'
  | 'Impersonation & content reports'
  | 'Profile & name changes'
  | 'Something else';

export interface LeadItem {
  id: number;
  name: string;
  handle: string;
  email: string;
  phone: string;
  service: string;
  status: 'New' | 'In progress' | 'Closed';
  date: string;
  message: string;
  note?: string;
}

export type PageView = 'home' | 'unban' | 'username' | 'ban' | 'apply' | 'admin';
