-- C)

BEGIN TRANSACTION;
SAVEPOINT actualizacion;
UPDATE pedidos SET estado = 'completado';
UPDATE pedidos SET estado = 'pendiente' WHERE fecha_entrega > CURRENT_DATE;
ROLLBACK TO actualizacion;
COMMIT;

-- D)

UPDATE pedidos SET estado = 'completado' WHERE fecha_entrega > CURRENT_DATE;
SELECT * FROM pedidos WHERE estado = 'completado';