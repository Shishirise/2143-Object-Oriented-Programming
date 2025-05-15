from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
FILE = "/Users/shishiradhikari/Documents/meteorites/meteorites.json"  # Your specified path

class JsonDB:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r") as file:
            return json.load(file)

    def _save_data(self):
        with open(self.filepath, "w") as file:
            json.dump(self.data, file, indent=2)

    def read_all(self):
        return self.data

    def read_one(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

    def create(self, record):
        self.data.append(record)
        self._save_data()
        return len(self.data) - 1

    def update(self, index, updates):
        if 0 <= index < len(self.data):
            self.data[index].update(updates)
            self._save_data()
            return self.data[index]
        return None

    def delete(self, index):
        if 0 <= index < len(self.data):
            deleted = self.data.pop(index)
            self._save_data()
            return deleted
        return None

class MeteoriteDB(JsonDB):
    def __init__(self):
        super().__init__(FILE)

    def find_by_year_range(self, start, end):
        return [
            m for m in self.data
            if 'year' in m and m['year'].isdigit() and start <= int(m['year']) <= end
        ]

    def find_heaviest(self, top_n=5):
        return sorted(
            [m for m in self.data if 'mass' in m and str(m['mass']).replace('.', '', 1).isdigit()],
            key=lambda x: float(x['mass']),
            reverse=True
        )[:top_n]

meteor_db = MeteoriteDB()

@app.route("/api/meteorites", methods=["GET"])
def get_all_meteorites():
    return jsonify(meteor_db.read_all()), 200

@app.route("/api/meteorites", methods=["POST"])
def add_meteorite():
    new_item = request.json
    index = meteor_db.create(new_item)
    return jsonify({"message": "Meteorite added", "index": index}), 201

@app.route("/api/meteorites/<int:index>", methods=["GET"])
def get_meteorite(index):
    record = meteor_db.read_one(index)
    if record:
        return jsonify(record), 200
    return jsonify({"error": "Index out of range"}), 404

@app.route("/api/meteorites/<int:index>", methods=["PUT"])
def update_meteorite(index):
    updates = request.json
    updated = meteor_db.update(index, updates)
    if updated:
        return jsonify({"message": "Meteorite updated", "data": updated}), 200
    return jsonify({"error": "Index out of range"}), 404

@app.route("/api/meteorites/<int:index>", methods=["DELETE"])
def delete_meteorite(index):
    deleted = meteor_db.delete(index)
    if deleted:
        return jsonify({"message": "Meteorite deleted", "data": deleted}), 200
    return jsonify({"error": "Index out of range"}), 404

@app.route("/api/meteorites/year/<int:start>/<int:end>", methods=["GET"])
def meteorites_by_year(start, end):
    result = meteor_db.find_by_year_range(start, end)
    return jsonify(result), 200

@app.route("/api/meteorites/heaviest", methods=["GET"])
def heaviest_meteorites():
    top_n = int(request.args.get("top", 5))  # ?top=10
    result = meteor_db.find_heaviest(top_n)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
