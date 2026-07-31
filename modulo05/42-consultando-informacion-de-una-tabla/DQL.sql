-- Ver total de ventas por cliente
SELECT c.nombre, c.apellido, COUNT(v.id_venta) AS total_ventas, 
       SUM(v.total_venta) AS monto_total
FROM clientes c
LEFT JOIN ventas v ON c.id_cliente = v.id_cliente
WHERE v.estado = 'completada'
GROUP BY c.id_cliente
HAVING SUM(v.total_venta) > 100000
ORDER BY monto_total DESC;

-- Productos más vendidos
SELECT p.nombre_producto, SUM(d.cantidad) AS cantidad_vendida,
       SUM(d.total_linea) AS total_ventas
FROM productos p
JOIN detalle_ventas d ON p.id_producto = d.id_producto
JOIN ventas v ON d.id_venta = v.id_venta
WHERE v.estado = 'completada'
GROUP BY p.id_producto
ORDER BY cantidad_vendida DESC
LIMIT 5;

-- Ventas por mes
SELECT TO_CHAR(fecha_venta, 'YYYY-MM') AS mes,
       COUNT(*) AS cantidad_ventas,
       SUM(total_venta) AS total_mes
FROM ventas
WHERE estado = 'completada'
GROUP BY TO_CHAR(fecha_venta, 'YYYY-MM')
ORDER BY mes;

-- Stock bajo (productos con stock crítico)
SELECT nombre_producto, stock_actual, stock_minimo,
       (stock_actual - stock_minimo) AS diferencia
FROM productos
WHERE stock_actual <= stock_minimo
ORDER BY stock_actual ASC;