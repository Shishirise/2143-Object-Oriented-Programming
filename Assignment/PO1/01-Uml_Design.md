# UML Diagram
[UML Diagram PDF](./Uml%20diagram.pdf)



## CandyManager
- **Attributes**
  - `candies`: List
  - `json_db`: JSONDBManager
- **Methods**
  - `add_candy()` : void
  - `remove_candy()` : void
  - `get_candy_list()` : void
  - `load_from_file()` : void
  - `save_to_file()` : void

---

## JSONDBManager
Handles JSON file operations such as reading, writing, and validating JSON data.

---

## Candy
- **Attributes**
  - `name`: String
  - `file_path`: String
  - `flavor`: String
  - `price`: float
- **Methods**
  - `load_data()` : void
  - `save_data()` : void
  - `validate_json()` : void
  - `get_name()` : void
  - `set_name()` : void
  - `get_flavor()` : void
  - `set_flavor()` : void
  - `get_price()` : void

---

## Relationships

- **Candy (1..*) --- JSONDBManager (Composition):**  
  The `JSONDBManager` acts as a manager responsible for maintaining data integrity for multiple `Candy` objects. It ensures the smooth operation of data storage and retrieval for the candies it oversees.

- **JSONDBManager (1) --- CandyManager (Composition):**  
  The `CandyManager` is equipped with a single instance of `JSONDBManager` (referred to as `json_db`), which handles all file-related operations, such as loading and saving data, thereby centralizing file management responsibilities.

---

## Design Reasoning
I built this JSON database manager with three classes  Candy, JSONDBManager, and CandyManager  to keep things organized and easy to work with. Here’s the breakdown:
- **Candy**:
  This is just a simple class to hold candy info like id, name, price, and stock. It doesn’t do much on its own  it’s like a data card for each candy.
- **JSONDBManager**:
  This handles all the JSON file tasks: reading, writing, and ensuring data integrity with methods like `readJSON()`, `writeJSON()`, and `validateJSON()`.
- **CandyManager**:
  It keeps a list of candies in memory, uses `json_db` to save them, and provides handy methods like `add_candy`, `remove_candy`, `get_candy_list`, `load_from_file`, and `save_to_file` to manage everything.

---

## Why Composition (Not Inheritance)?
I chose composition because it made more sense for this design:
- **CandyManager** has a JSONDBManager to handle file operations.
- **JSONDBManager** deals with multiple Candy objects.

It’s a "has-a" relationship, which makes it easy to swap out JSONDBManager for a different implementation if needed.

---

## Error-Checking
- **JSONDBManager** ensures the integrity of JSON data to avoid any file-related errors.
- **CandyManager** could add additional checks, such as:
  - Ensuring IDs aren’t duplicated.
  - Verifying stock isn’t negative when adding candy.



