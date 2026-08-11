--C)

BEGIN TRANSACTION;
UPDATE productos SET precio = precio * 0.85 WHERE categoria = 'electronicos';
SAVEPOINT antes_ajuste;
UPDATE productos SET precio = 100 WHERE categoria = 'electronicos' AND precio < 100;
ROLLBACK TO antes_ajuste;
COMMIT;
--D)

BEGIN TRANSACTION;
UPDATE productos SET precio = GREATEST(precio * 0.85, 100) WHERE categoria = 'electronicos';
COMMIT;