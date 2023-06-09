# Creamos la clase productos y la coleccion que guardaremos en nuestra base de datos
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Creamos la funcion para crear la coleccion o el documento que se va a guardar en la base de datos

    def toDBCollection(self):
        return{
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }