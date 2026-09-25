BEGIN;
--
-- Create model Autor
--
CREATE TABLE "cap02p2_autor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(50) NOT NULL, "apellido" varchar(50) NOT NULL);
--
-- Create model Libro
--
CREATE TABLE "cap02p2_libro" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(100) NOT NULL, "year" integer NOT NULL);
--
-- Create model AutorLibro
--
CREATE TABLE "cap02p2_autorlibro" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "traduccion" varchar(30) NOT NULL, "edicion" smallint unsigned NOT NULL CHECK ("edicion" >= 0), "creado_por" varchar(50) NOT NULL, "creacion" datetime NOT NULL, "autor_id" bigint NOT NULL REFERENCES "cap02p2_autor" ("id") DEFERRABLE INITIALLY DEFERRED, "libro_id" bigint NOT NULL REFERENCES "cap02p2_libro" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field libros to autor
--
CREATE TABLE "new__cap02p2_autor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(50) NOT NULL, "apellido" varchar(50) NOT NULL);
INSERT INTO "new__cap02p2_autor" ("id", "nombre", "apellido") SELECT "id", "nombre", "apellido" FROM "cap02p2_autor";
DROP TABLE "cap02p2_autor";
ALTER TABLE "new__cap02p2_autor" RENAME TO "cap02p2_autor";
CREATE INDEX "cap02p2_autorlibro_autor_id_bd4bc131" ON "cap02p2_autorlibro" ("autor_id");
CREATE INDEX "cap02p2_autorlibro_libro_id_5022033d" ON "cap02p2_autorlibro" ("libro_id");
COMMIT;
