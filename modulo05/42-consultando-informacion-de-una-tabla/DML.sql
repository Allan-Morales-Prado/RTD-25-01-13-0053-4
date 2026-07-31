INSERT INTO categorias (nombre_categoria, descripcion, estado) VALUES
('Electrónicos', 'Productos electrónicos y tecnológicos', 'activo'),
('Hogar', 'Artículos para el hogar y decoración', 'activo'),
('Ropa y Accesorios', 'Prendas de vestir y complementos', 'activo'),
('Alimentos', 'Productos alimenticios y bebidas', 'activo'),
('Deportes', 'Equipamiento y artículos deportivos', 'activo'),
('Juguetes', 'Juguetes y juegos para niños', 'activo'),
('Libros', 'Libros, revistas y material educativo', 'activo'),
('Jardinería', 'Herramientas y plantas para jardín', 'activo'),
('Mascotas', 'Productos para mascotas', 'inactivo'),
('Oficina', 'Suministros de oficina y papelería', 'activo');

INSERT INTO clientes (nombre, apellido, email, telefono, direccion, activo) VALUES
('María', 'González', 'maria.gonzalez@email.com', '+56 9 1234 5678', 'Av. Siempre Viva 123, Santiago', true),
('Juan', 'Pérez', 'juan.perez@email.com', '+56 9 2345 6789', 'Calle Los Alamos 456, Viña del Mar', true),
('Catalina', 'Fernández', 'cata.fernandez@email.com', '+56 9 3456 7890', 'Pasaje Las Flores 789, Concepción', true),
('Roberto', 'Martínez', 'roberto.mtz@email.com', '+56 9 4567 8901', 'Av. Costanera 321, Valparaíso', true),
('Daniela', 'Soto', 'daniela.soto@email.com', '+56 9 5678 9012', 'Calle Principal 654, La Serena', true),
('Carlos', 'Ramírez', 'carlos.ramirez@email.com', '+56 9 6789 0123', 'Av. República 987, Santiago', false),
('Andrea', 'Torres', 'andrea.torres@email.com', '+56 9 7890 1234', 'Calle Los Pinos 147, Temuco', true),
('Felipe', 'Castro', 'felipe.castro@email.com', '+56 9 8901 2345', 'Pasaje El Sol 258, Antofagasta', true),
('Valentina', 'Morales', 'valentina.morales@email.com', '+56 9 9012 3456', 'Av. Del Mar 369, Iquique', true),
('José', 'Reyes', 'jose.reyes@email.com', '+56 9 0123 4567', 'Calle Nueva 741, Rancagua', false);

INSERT INTO empleados (nombre, apellido, email, telefono, cargo, fecha_contratacion, salario, estado) VALUES
('Ana', 'Martínez', 'ana.martinez@empresa.com', '+56 9 1111 2222', 'Vendedor', '2025-01-15', 550000, 'activo'),
('Carlos', 'López', 'carlos.lopez@empresa.com', '+56 9 2222 3333', 'Supervisor', '2024-11-01', 850000, 'activo'),
('Laura', 'García', 'laura.garcia@empresa.com', '+56 9 3333 4444', 'Vendedor', '2025-06-10', 520000, 'activo'),
('Pedro', 'Sánchez', 'pedro.sanchez@empresa.com', '+56 9 4444 5555', 'Vendedor', '2025-08-20', 530000, 'activo'),
('Elena', 'Díaz', 'elena.diaz@empresa.com', '+56 9 5555 6666', 'Gerente', '2024-05-05', 1200000, 'activo'),
('Miguel', 'Fuentes', 'miguel.fuentes@empresa.com', '+56 9 6666 7777', 'Vendedor', '2026-01-02', 500000, 'activo'),
('Sofía', 'Rojas', 'sofia.rojas@empresa.com', '+56 9 7777 8888', 'Vendedor', '2025-09-15', 540000, 'inactivo'),
('Andrés', 'Herrera', 'andres.herrera@empresa.com', '+56 9 8888 9999', 'Supervisor', '2024-07-10', 820000, 'activo'),
('Paula', 'Muñoz', 'paula.munoz@empresa.com', '+56 9 9999 0000', 'Vendedor', '2025-12-01', 510000, 'activo'),
('Ricardo', 'Silva', 'ricardo.silva@empresa.com', '+56 9 0000 1111', 'Vendedor', '2026-02-15', 505000, 'activo');

INSERT INTO proveedores (nombre_proveedor, contacto, telefono, email, direccion, condiciones_pago, calificacion) VALUES
('Tech Solutions Chile', 'Carlos Henríquez', '+56 2 2222 1111', 'carlos@techsolutions.cl', 'Av. Providencia 1234, Santiago', '30 días', 5),
('Mega Store Import', 'María José Fernández', '+56 2 3333 2222', 'mjose@megastore.cl', 'Calle San Francisco 456, Santiago', 'Contado', 4),
('Distribuidora Hogar Plus', 'Roberto Acuña', '+56 2 4444 3333', 'racuna@hogarplus.cl', 'Av. Américo Vespucio 789, Santiago', '60 días', 5),
('Alimentos del Sur', 'Patricia Morales', '+56 2 5555 4444', 'pmorales@alimentosdelsur.cl', 'Ruta 5 Sur Km 45, Chillán', '15 días', 3),
('Sport World SPA', 'Gabriel Fuenzalida', '+56 2 6666 5555', 'gfuenzalida@sportworld.cl', 'Av. El Salto 123, Quilicura', '30 días', 4),
('Juguetes Fantásticos', 'Daniela Pereira', '+56 2 7777 6666', 'dpereira@juguetesfantasticos.cl', 'Calle Lira 789, Santiago', 'Contado', 5),
('Librería y Papelera Central', 'Claudio Espinoza', '+56 2 8888 7777', 'cespinoza@central.cl', 'Av. Libertador 456, Santiago', '30 días', 4),
('Green Garden', 'Fernanda Solar', '+56 2 9999 8888', 'fsolar@greengarden.cl', 'Calle Los Jardines 234, Maipú', '45 días', 3),
('Importadora Textil', 'Luis Martínez', '+56 2 0000 9999', 'lmartinez@importtextil.cl', 'Av. San Pablo 567, Santiago', '60 días', 4),
('Alimentos Nutry', 'Pablo Villalobos', '+56 2 1111 0000', 'pvillalobos@nutry.cl', 'Camino Melipilla 890, Pudahuel', '15 días', 5);

INSERT INTO productos (id_categoria, codigo_barras, nombre_producto, descripcion, precio_compra, precio_venta, stock_actual, stock_minimo, unidad_medida, activo) VALUES
(1, '78910001', 'Televisor LED 55" 4K UHD', 'TV Smart con resolución 4K, HDR, Android TV', 350000, 550000, 15, 5, 'unidad', true),
(1, '78910002', 'Computador Portátil 14"', 'Laptop i5, 16GB RAM, 512GB SSD', 600000, 850000, 8, 3, 'unidad', true),
(1, '78910003', 'Tablet 10"', 'Tablet Android, 64GB, WiFi', 120000, 180000, 20, 5, 'unidad', true),
(2, '78920001', 'Set de Sartenes 3 piezas', 'Sartenes antiadherentes, incluye 20, 24, 28 cm', 25000, 45000, 30, 10, 'set', true),
(2, '78920002', 'Juego de Toallas 8 piezas', 'Toallas de baño, 100% algodón, 500gr/m2', 18000, 32000, 25, 8, 'set', true),
(2, '78920003', 'Vajilla 24 piezas', 'Vajilla completa para 6 personas, porcelana blanca', 45000, 75000, 12, 5, 'set', true),
(3, '78930001', 'Camisa Hombre', 'Camisa formal manga larga, 100% algodón', 12000, 25000, 40, 10, 'unidad', true),
(3, '78930002', 'Chaqueta Cuero', 'Chaqueta de cuero genuino, color negro', 65000, 120000, 8, 3, 'unidad', true),
(3, '78930003', 'Zapatos Deportivos', 'Zapatillas running, tallas 38-44', 35000, 65000, 18, 6, 'par', true),
(4, '78940001', 'Café Gourmet 1kg', 'Café tostado molido, origen colombiano', 8000, 15900, 50, 15, 'kg', true),
(4, '78940002', 'Aceite de Oliva 500ml', 'Aceite extra virgen, primera prensada', 5000, 9900, 35, 10, 'unidad', true),
(4, '78940003', 'Caja de Vinos 6 unidades', 'Selección de vinos tintos, 6 botellas', 40000, 75000, 10, 3, 'caja', true),
(5, '78950001', 'Pelota Fútbol', 'Pelota oficial, tamaño 5', 15000, 28000, 25, 8, 'unidad', true),
(5, '78950002', 'Bicicleta MTB', 'Bicicleta montaña 21 velocidades, suspensión', 250000, 420000, 5, 2, 'unidad', true),
(5, '78950003', 'Juego de Pesas 20kg', 'Set de mancuernas ajustables', 80000, 135000, 10, 3, 'set', true),
(6, '78960001', 'Muñeca Articulada', 'Muñeca con articulaciones, incluye ropa y accesorios', 8000, 15900, 30, 10, 'unidad', true),
(6, '78960002', 'Set de Construcción 500 piezas', 'Bloques de construcción, compatible con ladrillos', 12000, 25000, 20, 5, 'set', true),
(6, '78960003', 'Coche Teledirigido', 'Auto RC, batería recargable, control 2.4GHz', 25000, 45000, 12, 4, 'unidad', true),
(7, '78970001', 'Diccionario Inglés-Español', 'Diccionario bilingüe, 2000 páginas', 15000, 29000, 15, 5, 'unidad', true),
(7, '78970002', 'Pack de 5 Cuentos Infantiles', 'Colección de cuentos ilustrados para niños', 9000, 18000, 25, 8, 'set', true),
(8, '78980001', 'Set Jardinería 8 piezas', 'Herramientas manuales para jardín, incluye guantes', 15000, 28000, 12, 4, 'set', true),
(8, '78980002', 'Semillas de Flores', 'Pack de 10 variedades de semillas de flores', 3000, 6500, 40, 15, 'unidad', true),
(10, '78990001', 'Tóner para Impresora', 'Cartucho de tóner negro, compatible HP', 25000, 45000, 15, 5, 'unidad', true),
(10, '78990002', 'Set de Marcadores 24 colores', 'Marcadores permanentes de colores, punta fina', 4000, 8900, 30, 10, 'set', true);

INSERT INTO ventas (id_cliente, id_empleado, numero_factura, fecha_venta, total_venta, metodo_pago, estado, observaciones) VALUES
(1, 1, 'FAC-2026-0001', '2026-01-15 10:30:00', 550000, 'tarjeta', 'completada', 'Venta normal'),
(2, 3, 'FAC-2026-0002', '2026-01-16 11:45:00', 970000, 'transferencia', 'completada', 'Descuento especial'),
(3, 6, 'FAC-2026-0003', '2026-01-18 09:20:00', 65000, 'efectivo', 'completada', NULL),
(4, 1, 'FAC-2026-0004', '2026-01-20 15:10:00', 28000, 'tarjeta', 'completada', 'Regalo'),
(5, 9, 'FAC-2026-0005', '2026-01-22 12:00:00', 135000, 'efectivo', 'completada', NULL),
(6, 3, 'FAC-2026-0006', '2026-01-25 17:30:00', 15900, 'tarjeta', 'pendiente', 'Error en pago'),
(7, 6, 'FAC-2026-0007', '2026-02-01 10:00:00', 120000, 'transferencia', 'completada', 'Envío urgente'),
(8, 9, 'FAC-2026-0008', '2026-02-03 14:20:00', 45000, 'efectivo', 'completada', NULL),
(1, 1, 'FAC-2026-0009', '2026-02-05 09:30:00', 25000, 'tarjeta', 'completada', 'Compra online'),
(9, 3, 'FAC-2026-0010', '2026-02-07 16:15:00', 29000, 'efectivo', 'anulada', 'Cliente desistió'),
(10, 6, 'FAC-2026-0011', '2026-02-10 11:00:00', 75000, 'transferencia', 'completada', NULL),
(2, 9, 'FAC-2026-0012', '2026-02-12 13:45:00', 850000, 'tarjeta', 'completada', 'Venta corporativa'),
(4, 1, 'FAC-2026-0013', '2026-02-14 10:30:00', 28000, 'efectivo', 'completada', NULL),
(5, 3, 'FAC-2026-0014', '2026-02-16 09:15:00', 45000, 'tarjeta', 'pendiente', 'Pendiente de confirmación'),
(8, 6, 'FAC-2026-0015', '2026-02-18 12:00:00', 420000, 'transferencia', 'completada', 'Venta especial');

INSERT INTO detalle_ventas (id_venta, id_producto, cantidad, precio_unitario, subtotal, descuento, total_linea) VALUES
-- Venta 1
(1, 1, 1, 550000, 550000, 0, 550000),

-- Venta 2
(2, 2, 1, 850000, 850000, 0, 850000),
(2, 3, 1, 180000, 180000, 60000, 120000),

-- Venta 3
(3, 6, 1, 75000, 75000, 10000, 65000),

-- Venta 4
(4, 13, 1, 28000, 28000, 0, 28000),

-- Venta 5
(5, 15, 1, 135000, 135000, 0, 135000),

-- Venta 6
(6, 11, 1, 15900, 15900, 0, 15900),

-- Venta 7
(7, 8, 1, 120000, 120000, 0, 120000),

-- Venta 8
(8, 23, 1, 45000, 45000, 0, 45000),

-- Venta 9
(9, 7, 1, 25000, 25000, 0, 25000),

-- Venta 10
(10, 19, 1, 29000, 29000, 0, 29000),

-- Venta 11
(11, 5, 1, 32000, 32000, 0, 32000),
(11, 6, 1, 75000, 75000, 32000, 43000),

-- Venta 12
(12, 2, 1, 850000, 850000, 0, 850000),

-- Venta 13
(13, 14, 1, 28000, 28000, 0, 28000),

-- Venta 14
(14, 22, 1, 6500, 6500, 0, 6500),
(14, 4, 1, 45000, 45000, 6500, 38500),

-- Venta 15
(15, 14, 1, 420000, 420000, 0, 420000);

INSERT INTO auditoria (tabla_afectada, accion, id_registro, usuario, datos_anteriores, datos_nuevos) VALUES
('productos', 'UPDATE', 1, 'sistema', '{"stock_actual": "20"}', '{"stock_actual": "15"}'),
('clientes', 'INSERT', 11, 'admin', '{}', '{"nombre": "Marcela", "apellido": "Luna"}'),
('ventas', 'UPDATE', 6, 'admin', '{"estado": "pendiente"}', '{"estado": "completada"}'),
('productos', 'INSERT', 25, 'sistema', '{}', '{"nombre_producto": "Cámara Digital"}');

INSERT INTO compras (id_proveedor, numero_orden, fecha_compra, total_compra, estado) VALUES
(1, 'OC-2026-0001', '2026-01-10 08:00:00', 1050000, 'recibida'),
(2, 'OC-2026-0002', '2026-01-15 09:30:00', 450000, 'pendiente'),
(3, 'OC-2026-0003', '2026-01-20 10:00:00', 750000, 'recibida'),
(4, 'OC-2026-0004', '2026-01-25 11:15:00', 320000, 'anulada'),
(5, 'OC-2026-0005', '2026-02-01 08:45:00', 680000, 'recibida'),
(6, 'OC-2026-0006', '2026-02-05 09:00:00', 250000, 'pendiente'),
(7, 'OC-2026-0007', '2026-02-10 10:30:00', 180000, 'recibida'),
(8, 'OC-2026-0008', '2026-02-15 11:00:00', 420000, 'en proceso'),
(1, 'OC-2026-0009', '2026-02-20 08:15:00', 590000, 'recibida'),
(10, 'OC-2026-0010', '2026-02-25 09:45:00', 280000, 'pendiente');

INSERT INTO usuarios (id_empleado, nombre_usuario, contraseña_hash, rol, ultimo_acceso, activo) VALUES
(1, 'ana.martinez', 'hash_ana_123456', 'vendedor', '2026-02-28 17:30:00', true),
(2, 'carlos.lopez', 'hash_carlos_123456', 'supervisor', '2026-02-28 18:00:00', true),
(5, 'elena.diaz', 'hash_elena_123456', 'admin', '2026-02-28 19:15:00', true),
(3, 'laura.garcia', 'hash_laura_123456', 'vendedor', '2026-02-27 16:45:00', true),
(4, 'pedro.sanchez', 'hash_pedro_123456', 'vendedor', '2026-02-26 15:20:00', true),
(6, 'miguel.fuentes', 'hash_miguel_123456', 'vendedor', '2026-02-28 14:10:00', true),
(8, 'andres.herrera', 'hash_andres_123456', 'supervisor', '2026-02-27 12:30:00', true),
(9, 'paula.munoz', 'hash_paula_123456', 'vendedor', '2026-02-26 11:00:00', true),
(7, 'sofia.rojas', 'hash_sofia_123456', 'vendedor', '2026-01-15 10:00:00', false),
(10, 'ricardo.silva', 'hash_ricardo_123456', 'vendedor', '2026-02-28 09:45:00', true);