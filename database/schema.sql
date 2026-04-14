-- 1. Crear tabla
create table if not exists operaciones (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references auth.users(id),
    cliente text,
    monto numeric,
    tipo text,
    estado text default 'pendiente',
    created_at timestamp default now()
);

-- 2. Activar RLS
alter table operaciones enable row level security;

-- 3. Policy SELECT (ver solo tus datos)
create policy "Usuarios ven sus operaciones"
on operaciones
for select
using (auth.uid() = user_id);

-- 4. Policy INSERT (solo insertar tus propios datos)
create policy "Usuarios pueden insertar"
on operaciones
for insert
with check (auth.uid() = user_id);
