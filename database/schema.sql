CREATE TABLE operations (
    id SERIAL PRIMARY KEY,
    tipo TEXT,
    cliente TEXT,
    monto NUMERIC,
    moneda TEXT,
    estado TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    respuesta JSONB
);
