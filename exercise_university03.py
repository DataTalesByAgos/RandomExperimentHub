# OOP practice

# Parent class "Entity" that inherits IDs to its children (tables)

# Abstraction: The Entity class provides a structure for creating entities with automatic IDs.
class Entity:
    _id_counter = {}

    def __init__(self, table_name):
        self.table_name = table_name
        if table_name not in Entity._id_counter:
            Entity._id_counter[table_name] = 1
        else:
            Entity._id_counter[table_name] += 1
        self._id = Entity._id_counter[table_name]  # Encapsulation: protected ID

    def __str__(self):  # Polymorphism: __str__ method to be overridden
        return f"Entity(id={self.id})"

    @property
    def id(self):  # Encapsulation: method to access the ID
        return self._id

    # Methods to validate counters and their origins
    @classmethod
    def get_all_ids(cls):
        return cls._id_counter

    @classmethod
    def get_ids_by_type(cls, table_name):
        return cls._id_counter.get(table_name, 0)


# Property class that inherits from Entity
class Property(Entity):
    def __init__(self, property_state_id, location_id, price):
        super().__init__('property')  # Inheritance: calling the parent class "Entity" constructor
        self.property_state_id = property_state_id
        self.location_id = location_id
        self.price = price

    def __str__(self):  # Polymorphism: __str__ method to print different content based on which class uses it
        return f"{super().__str__()}, state={self.property_state_id}, location={self.location_id}, price={self.price}"


# Rental class that inherits from Entity
class Rental(Entity):
    def __init__(self, real_estate_id, property_id, start_date, end_date, price, client_id, transaction_id):
        super().__init__('rental')  # Inheritance: calling the parent class "Entity" constructor
        self.real_estate_id = real_estate_id
        self.property_id = property_id
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.client_id = client_id
        self.transaction_id = transaction_id

    def __str__(self):  # Polymorphism: another behavior of the __str__ method
        return f"{super().__str__()}, real_estate={self.real_estate_id}, property={self.property_id}, start_date={self.start_date}, end_date={self.end_date}, price={self.price}, client={self.client_id}, transaction={self.transaction_id}"


# Real Estate Agency class that inherits from Entity
class RealEstateAgency(Entity):
    def __init__(self, business_name, location_id, cuit):
        super().__init__('real_estate_agency')  # Inheritance: calling the parent class "Entity" constructor
        self.business_name = business_name
        self.location_id = location_id
        self.cuit = cuit

    def __str__(self):  # Polymorphism: another behavior of the __str__ method
        return f"{super().__str__()}, business_name={self.business_name}, location={self.location_id}, cuit={self.cuit}"


# Data instantiation
property1 = Property(1, 1234, 350000)
rental1 = Rental(1, 1, '2020-01-01', '2024-06-11', 4567, 2, 101)
real_estate_agency1 = RealEstateAgency('Example Real Estate Agency', 1001, '30-12345678-9')

# Test
print(property1)
print(rental1)
print(real_estate_agency1)

property2 = Property(1, 1234, 450000)
print(property2)  # Print all IDs saved so far
print("All IDs by type:", Entity.get_all_ids())

# Print IDs by entity type created
print("Property IDs:", Entity.get_ids_by_type('property'))
print("Rental IDs:", Entity.get_ids_by_type('rental'))
print("Real Estate Agency IDs:", Entity.get_ids_by_type('real_estate_agency'))