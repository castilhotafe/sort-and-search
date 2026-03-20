"""
This module provides the definition of the `Storage` class, which inherits
from the `float` type. The `Storage` class extends the behavior of a
floating-point number to include an additional unit attribute to describe
the measurement unit (e.g., GB, MB).

The class includes functionality for creating instances and representing them
as formatted strings.
"""
class Storage(float): #storage inherits from float class
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        instance.value = value

        return instance
    def __str__(self):
        return f'Storage has {self.value:.2f}{self.unit} of memory'

storage_size = Storage(512, "GB")
print(storage_size)

