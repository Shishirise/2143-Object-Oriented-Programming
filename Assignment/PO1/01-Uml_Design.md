# UML Diagram

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


[UML Diagram PDF](./Uml%20diagram.pdf)
