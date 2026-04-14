create table operaciones (
  id uuid default gen_random_uuid() primary key,
  user_id uuid,
  email text,
  cliente text,
  tipo text,
  monto numeric,
  moneda text,
  descripcion text,
  fecha timestamp default now()
);
