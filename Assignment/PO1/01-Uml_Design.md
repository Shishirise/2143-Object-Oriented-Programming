

## UML Diagram  
[UML Diagram PDF](.https://github.com/Shishirise/2143-Object-Oriented-Programming/blob/main/Assignment/PO1/a.jpg)

---

## Flask App
- **Attributes**
  - `meteor_db`: `MeteoriteDB`
- **Methods**
  - `get_all_meteorites()` : `void`  
  - `add_meteorite()` : `void`  
  - `get_meteorite()` : `void`  
  - `update_meteorite()` : `void`  
  - `delete_meteorite()` : `void`  

---

## JsonDB
Handles JSON file operations such as reading, writing, and performing basic CRUD operations on JSON data.

- **Attributes**
  - `filepath`: `str`  
  - `data`: `list`
- **Methods**
  - `_load_data()` : `void`  
  - `_save_data()` : `void`  
  - `read_all()` : `list`  
  - `read_one(index: int)` : `dict`  
  - `create(record: dict)` : `int`  
  - `update(index: int, updates: dict)` : `dict`  
  - `delete(index: int)` : `dict`  

---

## MeteoriteDB
Inherits from `JsonDB` and provides domain-specific operations related to meteorite data.

- **Methods**
  - `find_by_year_range(start: int, end: int)` : `list`  
  - `find_heaviest(top_n: int)` : `list`  

---

## Relationships

- **Flask App (1) --- MeteoriteDB (Composition):**  
  The `Flask App` contains one instance of `MeteoriteDB` called `meteor_db`, which handles data operations and exposes them via API endpoints.

- **MeteoriteDB (is-a) --- JsonDB (Inheritance):**  
  `MeteoriteDB` extends `JsonDB` to reuse its core functionality and add features specific to meteorite data.

---

## Design Reasoning

I designed this meteorite data management system with three logical components: **Flask App**, **JsonDB**, and **MeteoriteDB** — to promote clean separation of concerns, reuse, and scalability.

- **JsonDB**  
  Handles all core functionality such as reading, writing, and modifying records from a JSON file. It provides the foundational CRUD logic that can be reused across different datasets.

- **MeteoriteDB**  
  Extends the generic JSON database with meteorite-specific queries such as filtering by year and sorting by mass. This allows meteorite logic to live separately from core database logic.

- **Flask App**  
  Acts as a RESTful interface that exposes all meteorite functionality via API endpoints. It depends on a `MeteoriteDB` instance to read from and modify the data.

---

## Why Inheritance (Not Composition)?

- `MeteoriteDB` is a specialized form of `JsonDB`, so **inheritance** is the right fit.  
- The relationship is "MeteoriteDB **is-a** JsonDB," which allows shared methods like `read_all()`, `create()`, and `update()` to be inherited and reused.

By contrast:
- The **Flask App** uses **composition**: it **has-a** `MeteoriteDB`.

---

## Error-Checking

- **JsonDB** includes safe file handling and verifies whether the JSON file exists before loading.
- **MeteoriteDB** can be further extended to include validation, such as:
  - Ensuring `mass` is a float and `year` is a valid number.
  - Filtering out incomplete or corrupted records.


