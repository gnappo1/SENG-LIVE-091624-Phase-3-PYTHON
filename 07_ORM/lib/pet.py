# Pet Attributes:
# name: TEXT
# species: TEXT
# breed: TEXT
# temperament: TEXT

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3
from helper import Helper

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('lib/resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

class Pet(Helper): #! mixin -> throwing a class in the inheritance line just to share functionality
    all_ = {} #! TABULATION
    
    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__(self, name, species, breed, temperament, id_=None):
        # instantiation VS persistance
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament
        self.id = id_

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(f"""
                CREATE TABLE IF NOT EXISTS {cls.pascal_to_camel_plural()} (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    species TEXT NOT NULL,
                    breed TEXT NOT NULL,
                    temperament TEXT
                    
                );
            """)
        except Exception as e:
            return e

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute(f"""
                DROP TABLE IF EXISTS {cls.pascal_to_camel_plural()};
            """)
        except Exception as e:
            return e

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
    def save(self):
        try:
            with CONN:
                CURSOR.execute(f"""
                    INSERT INTO {type(self).pascal_to_camel_plural()}
                    (name, species, breed, temperament)
                    VALUES
                    (?, ?, ?, ?)
                """, (self.name, self.species, self.breed, self.temperament))
                self.id = CURSOR.lastrowid
                type(self).all_[self.id] = self
        except Exception as e:
            return e
        
        # try:
        #     CURSOR.execute(f"""
        #         INSERT INTO {type(self).pascal_to_camel_plural()}
        #         (name, species, breed, temperament)
        #         VALUES
        #         (?, ?, ?, ?)
        #     """, (self.name, self.species, self.breed, self.temperament))
        #     CONN.commit()
        # except Exception as e:
        #     CONN.rollback()
        #     return e
    
    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create(cls, name, species, breed, temperament):
        pet = cls(name, species, breed, temperament) #! 1. instantiate the object
        pet.save() #! now the obj attributes have been saved as row of data into the table
        return pet

    # ✅ 6. Add "update" Instance Method to Update the db based on its Attributes
    def update(self):
        try:
            with CONN:
                CURSOR.execute(f"""
                    UPDATE {type(self).pascal_to_camel_plural()}
                    SET name=?, species=?, breed=?, temperament=?
                    WHERE id = ?;
                """, (self.name, self.species, self.breed, self.temperament, self.id))
                type(self).all_[self.id] = self
        except Exception as e:
            return e
    
    def delete(self):
        try:
            with CONN:
                CURSOR.execute(f"""
                    DELETE FROM {type(self).pascal_to_camel_plural()}
                    WHERE id = ?;
                """, (self.id,))
                del type(self).all_[self.id]
        except Exception as e:
            return e
    
    # ✅ 7. Add "new_from_db" Class Method to Instantiate a new "pet" Instance from a row of pet Attributes From DB
    @classmethod
    def new_from_db(cls, row_of_data):
        try:
            return cls(row_of_data[1], row_of_data[2], row_of_data[3], row_of_data[4], row_of_data[0])
        except Exception as e:
            return e

    # ✅ 8. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def get_all(cls):
        try:
            with CONN:
                query = CURSOR.execute(f"""
                    SELECT * FROM {cls.pascal_to_camel_plural()}
                """)
                data = query.fetchall()
                return [cls.new_from_db(row) for row in data]
        except Exception as e:
            return e
    # ✅ 9. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB
    @classmethod
    def find_by_name(cls, name):
        try:
            with CONN:
                query = CURSOR.execute(f"""
                    SELECT * FROM {cls.pascal_to_camel_plural()}
                    WHERE name=?
                    LIMIT 1;
                """, (name.lower(),))
                row_of_data = query.fetchone()
                return cls.new_from_db(row_of_data) if row_of_data else None
        except Exception as e:
            return e

    # If No "pet" Found, return "None"

    # ✅ 10. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

    # If No "pet" Found, return "None"

    # ✅ 11. Add "find_or_create_by" Class Method to:

    #  Find and Retrieve "pet" Instance w/ All Attributes

    # If No "pet" Found, Create New "pet" Instance w/ All Attributes

# import ipdb; ipdb.set_trace()