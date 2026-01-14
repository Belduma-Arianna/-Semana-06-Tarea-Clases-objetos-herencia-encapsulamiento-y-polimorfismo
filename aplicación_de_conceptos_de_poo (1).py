# Clase Base: Animal (Demuestra el concepto de encapsulación estricta)
class Animal:
    def __init__(self, name, sound):
        # Encapsulación estricta: '__name' y '__sound' son atributos "privados" (mediante Name Mangling).
        # Esto significa que su acceso y modificación están forzados a ser a través de los métodos.
        self.__name = name
        self.__sound = sound

    # Getter para '__name': Permite obtener el valor del nombre de forma controlada.
    def get_name(self):
        return self.__name

    # Setter para '__name': Permite modificar el nombre, incluyendo lógica de validación.
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            print(f"Cambiando el nombre de '{self.__name}' a '{new_name}'.")
            self.__name = new_name
        else:
            print("¡Error! El nuevo nombre no es válido o está vacío.")

    # Método que utiliza los atributos encapsulados para una acción.
    def speak(self):
        return f"{self.__name} emite un {self.__sound}"


# Clase Derivada: Perro (Demuestra el concepto de herencia y polimorfismo)
class Perro(Animal):
    def __init__(self, name, breed):
        # Herencia: Llama al constructor de la clase base Animal para inicializar nombre y sonido.
        super().__init__(name, "Guau!")
        self.breed = breed

    # Polimorfismo: Sobreescritura del método 'speak'.
    # Esta implementación es específica para Perro, diferente de la de Animal.
    def speak(self):
        # Accedemos al nombre a través del getter de la clase base.
        return f"{self.get_name()} el {self.breed} ladra: ¡Woof! ¡Woof!"

    # Método adicional específico de la clase Perro.
    def fetch(self, item):
        return f"{self.get_name()} está trayendo el {item}."


# --- Demostración de Encapsulación Estricta, Herencia y Polimorfismo ---

print("\n--- Demostración de Encapsulación ---")
# Creación de una instancia de la clase Animal.
animal = Animal("León", "Rugido")
print(f"Animal inicial: {animal.get_name()}") # Acceso al nombre a través del getter.
print(animal.speak())

# Modificación del nombre utilizando el método setter.
animal.set_name("Simba")
print(f"Animal después de set_name(): {animal.get_name()}")
print(animal.speak())

# Intentos de establecer nombres inválidos para demostrar la validación del setter.
animal.set_name("") # Intento de establecer un nombre vacío.
animal.set_name(123) # Intento de establecer un nombre que no es string.
print(f"Animal después de intentos inválidos: {animal.get_name()}") # El nombre permanece inalterado.

print("\n--- Demostración de Herencia y Polimorfismo ---")
# Creación de una instancia de la clase derivada Perro.
perro = Perro("Buddy", "Golden Retriever")

# Polimorfismo en acción: Ambos objetos responden al método 'speak', pero de diferente manera.
print(animal.speak()) # Llama al método 'speak' de Animal.
print(perro.speak())  # Llama al método 'speak' de Perro (sobrescrito).

# Uso de un método específico de la clase derivada.
print(perro.fetch("pelota"))

# Demostración de polimorfismo con una lista de diferentes tipos de animales.
print("\n--- Polimorfismo con una lista de seres vivos ---")
seres_vivos = [animal, perro]
for ser in seres_vivos:
    # Cada objeto en la lista llama a su propia implementación del método 'speak'.
    print(ser.speak())
