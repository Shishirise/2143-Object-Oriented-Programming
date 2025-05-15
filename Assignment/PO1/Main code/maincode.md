#  Full code structure and logic

Flask Meteorite API Code Explanation

This Flask API allows users to perform CRUD operations on a list of meteorites stored in a JSON file. Here's a breakdown of the code:

---

##  JsonDB Class

The `JsonDB` class is a base class responsible for reading from and writing to the JSON file and providing generic CRUD operations.

###  Attributes
- `filepath`: path to the JSON file
- `data`: list of meteorite records, loaded into memory

###  Methods
- `_load_data()` – loads the data from the JSON file
- `_save_data()` – writes the in-memory data back to the JSON file
- `read_all()` – returns all records
- `read_one(index)` – returns the record at a specific index
- `create(record)` – adds a new record
- `update(index, updates)` – updates an existing record
- `delete(index)` – deletes a record at a specific index

---

##  MeteoriteDB Class

Inherits from `JsonDB`. Adds meteorite-specific queries:

###  Methods
- `find_by_year_range(start, end)` – finds meteorites within a year range
- `find_heaviest(top_n)` – returns top N heaviest meteorites

---

##  Flask Routes

### `GET /api/meteorites`
Returns all meteorite records.

### `POST /api/meteorites`
Adds a new meteorite. Requires a JSON body with meteorite data.

### `GET /api/meteorites/<index>`
Returns the meteorite at the specified index.

### `PUT /api/meteorites/<index>`
Updates the meteorite at the specified index. Requires a JSON body with fields to update.

### `DELETE /api/meteorites/<index>`
Deletes the meteorite at the specified index.

### `GET /api/meteorites/year/<start>/<end>`
Returns meteorites that fell between the specified years.

### `GET /api/meteorites/heaviest`
Returns the top N heaviest meteorites (default is 5). Accepts `?top=n` query parameter.

---

##  How It Works

- When the app starts, `MeteoriteDB` loads the meteorite data from `meteorites.json`
- All API routes use this instance (`meteor_db`) to read, modify, or delete records
- Changes are immediately saved to the file

---



##  OOP Design Explanation: JsonDB vs MeteoriteDB

###  1. Base Class: JsonDB

The `JsonDB` class is a generic, reusable database handler that provides the foundational operations needed to manage any JSON-based dataset.

**Its responsibilities:**
- Read/write data from a `.json` file
- Provide universal CRUD methods:
  - `create()`
  - `read_all()`
  - `read_one(index)`
  - `update(index, updates)`
  - `delete(index)`

This class is data-agnostic — it doesn’t care what type of records it's storing. It just provides the core database functionality.

---

###  2. Subclass Example: MeteoriteDB

The `MeteoriteDB` class inherits from `JsonDB`, gaining all its CRUD capabilities, and extends it with custom behavior specific to meteorite data.

**Extra domain-specific methods in `MeteoriteDB`:**
- `find_heaviest(top_n)` – find the N heaviest meteorites
- `find_by_year_range(start, end)` – filter meteorites by year

These methods are tailored to the meteorite domain and would not belong in a general-purpose `JsonDB`.

---

###  Why Use Inheritance?

This design intentionally separates general-purpose functionality from domain-specific logic.

> Instead of building one giant class that tries to handle every possible case, we use OOP to cleanly divide responsibilities.

- `JsonDB` handles universal JSON operations (for any data type)
- `MeteoriteDB` handles meteorite-specific logic

---

###  Design Philosophy

> This exercise shows the power of Object-Oriented Programming (OOP):  
> you can build reusable, generic tools (`JsonDB`), and then extend them for specific needs (`MeteoriteDB`), keeping your code organized, scalable, and easy to maintain.

Even though the example might seem a little contrived, this structure helps demonstrate:
- Inheritance
- Encapsulation
- Separation of concerns
"""

