### 🔹Delete Using Index
Remove a specific meteorite record by its index in the JSON array.

DELETE http://127.0.0.1:5000/api/meteorites/0

```json
{
  "message": "Meteorite deleted",
  "data": {
    "GeoLocation": "(35.666670, 139.650000)",
    "_id": { "$oid": "5d9deac32ebe2da7d4da1b3e" },
    "fall": "Fell",
    "id": 3,
    "mass": 11000,
    "name": "Tokyo",
    "nametype": "Valid",
    "recclass": "L5",
    "reclat": 35.66667,
    "reclong": 139.65,
    "year": 1986
  }
}
