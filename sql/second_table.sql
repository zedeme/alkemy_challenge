CREATE TABLE IF NOT EXISTS public.second_table
(
    "category" character varying(40),
    "fuente" character varying(40),
    "provincia" integer,
    "date_update" date,
    PRIMARY KEY ("category")
)