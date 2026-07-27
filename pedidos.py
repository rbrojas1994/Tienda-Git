# pedidos.py - Módulo para gestión de pedidos
class GestorPedidos:
    def __init__(self, db_conexion):
        self.db = db_conexion
    
    def crear_pedido(self, usuario_id, productos):
        """
        Crea un nuevo pedido en el sistema.
        Valida stock antes de confirmar.
        """
        # Verificar stock de cada producto
        for producto in productos:
            if not self.verificar_stock(producto['id'], producto['cantidad']):
                raise ValueError(f"Stock insuficiente para producto {producto['id']}")
        
        # Crear pedido en BD
        query = "INSERT INTO pedidos (usuario_id, fecha, estado) VALUES (%s, NOW(), 'pendiente')"
        # ... lógica de inserción
        return {"pedido_id": 123, "estado": "pendiente"}
    
    def verificar_stock(self, producto_id, cantidad):
        # Lógica de verificación
        return True
