# Holbertonschool-AirBnB_clone
This is the AirBnB clone project for Holberton School. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

## Description
This repository contains the first step towards building our first full web application: the AirBnB clone. This first step consists of a custom command-line interface for data management.

## File Structure

AirBnBClone/
|-- models/
|   |-- __init__.py
|   |-- amenity.py
|   |-- base_model.py
|   |-- city.py
|   |-- place.py
|   |-- review.py
|   |-- state.py
|   |-- user.py
|-- tests/
|   |-- __pycache__/
|   |-- engine/
|   |   |   |-- __init__.py
|   |   |   |-- test_file_storage.py
|   |-- __init__.py
|   |-- test_models/
|   |   |-- __init__.py
|   |   |-- test_amenity.py
|   |   |-- test_base_model.py
|   |   |-- test_city.py
|   |   |-- test_place.py
|   |   |-- test_review.py
|   |   |-- test_state.py
|   |   |-- test_user.py
|   |
|   |-- __init__.py
|-- 
|-- AUTHORS
|-- console.py
|-- README.md


## Directory | Description |

**module**: Contains all the classes used for the entire project.
**engine**: Contains the file storage class.
**tests**: Contains all the unittests.


## File | Description |

models/**base_model.py:** The BaseModel class of the project.
models/**amenity.py:** The Amenity class of the project.
models/**city.py**: The City class of the project.
models/**place.py:** The Place class of the project.
models/**review.py:** The Review class of the project.
models/**state.py:** The State class of the project.
models/**user.py:** The User class of the project.
--- 
models/engine/**__init__.py:** The init file of the engine directory.
models/engine/**test_file_storage.py:** The FileStorage class of the project.
---
tests/**__init__.py:** The init file of the tests directory.
tests/test_models/**test_base_model.py:** The unittests for the BaseModel class.
tests/test_models/**test_city.py:** The unittests for the City class.
tests/test_models/**test_place.py:** The unittests for the Place class.
tests/test_models/**test_review.py:** The unittests for the Review class.
tests/test_models/**test_state.py:** The unittests for the State class.
tests/test_models/**test_user.py:** The unittests for the User class.


## Class Definitions

* **User:** Represents a User with attributes email, password, first_name, and last_name.
* **State:** Represents a State with an attribute name.
* **City** Represents a City with attributes state_id and name.
* **Amenity:** Represents an Amenity with an attribute name.
* **Place:** Represents a Place with attributes city_id, user_id, name, description,          number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, and amenity_ids.
* **Review:** Represents a Review with attributes place_id, user_id, and text.

## Requirements
* Ubuntu 14.04 LTS
* python3 (version 3.4.3)
* pep8 (version 1.7)
* MySQL 5.7 (version 5.7.8-rc)
* MySQLdb (version 1.3.10)
* SQLAlchemy (version 1.2.5)


## Usage

The console supports various commands for managing AirBnB objects:

Create a new instance of a class, save it, and print its ID.
    * **show**: Show the string representation of an instance based on class name and ID.
    * **destroy**: Delete an instance based on class name and ID.
    * **all**: Print string representations of all instances based on class name (optional).
    * **update**: Update an instance based on class name and ID by adding or updating an attribute.

To launch the console application in interactive mode simply run:
```bash

./console.py
```

## Authors and Contributors 
# This file lists all contributors to the repository.

Sweety Castro | [https://github.com/SMCastr]
Walter Carrion | [https://github.com/Scopecr]



