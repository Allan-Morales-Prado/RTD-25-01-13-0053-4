-- C)
SELECT categoria, AVG(precio) 
FROM productos 
GROUP BY categoria 
HAVING AVG(precio) > 5000;

-- D)
SELECT categoria, AVG(precio) 
FROM productos 
WHERE AVG(precio) > 5000 
GROUP BY categoria;

