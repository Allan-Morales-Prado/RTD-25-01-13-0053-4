-- Contar registros en cada tabla
SELECT 'Categorías' AS tabla, COUNT(*) AS cantidad FROM categorias
UNION ALL
SELECT 'Clientes', COUNT(*) FROM clientes
UNION ALL
SELECT 'Empleados', COUNT(*) FROM empleados
UNION ALL
SELECT 'Proveedores', COUNT(*) FROM proveedores
UNION ALL
SELECT 'Productos', COUNT(*) FROM productos
UNION ALL
SELECT 'Ventas', COUNT(*) FROM ventas
UNION ALL
SELECT 'Detalle Ventas', COUNT(*) FROM detalle_ventas
UNION ALL
SELECT 'Auditoría', COUNT(*) FROM auditoria
UNION ALL
SELECT 'Compras', COUNT(*) FROM compras
UNION ALL
SELECT 'Usuarios', COUNT(*) FROM usuarios;