CREATE TABLE IF NOT EXISTS public.firts_table
(
    
    "cod_loc" integer,
    "idprovincia" integer,
    "iddepartamento" integer,
    "category" character varying(50),
    "fuente" character varying(50),
    "localidad" character varying(50),
    "pantallas" integer,
    "provincia" character varying(50),
    "nombre" character varying(50),
    "direccion" character varying(50),
    "cp" character varying(50),
    "telefono" character varying(50),
    "mail" character varying(50),
    "web" character varying(50),
    "date_update" date,
    PRIMARY KEY ("nombre")
);