# Definimos la clase Registro
class Registro:
    """Clase que lleva un conteo de cuántas instancias se han creado."""
    
    total_instancias = 0  # Variable de clase para contar instancias

    def __init__(self):
        """Constructor que incrementa el contador de instancias al crear un objeto."""
        Registro.total_instancias += 1

    @classmethod
    def contar_instancias(cls):
        """Método de clase que devuelve el número total de instancias creadas."""
        return cls.total_instancias

# Creación de algunas instancias de Registro
r1 = Registro()
r2 = Registro()
r3 = Registro()

# Mostrar el número total de instancias creadas
print(f"Total de instancias creadas: {Registro.contar_instancias()}")
