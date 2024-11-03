from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data awal beberapa hewan
animals = {
    "1": {
        "name": "Lion",
        "description": "Hewan karnivora besar yang dikenal sebagai raja hutan.",
        "habitat": "Savannah",
        "lifespan_years": 12,
        "diet": "Carnivore"
    },
    "2": {
        "name": "Elephant",
        "description": "Mamalia darat terbesar di dunia dengan belalai yang panjang.",
        "habitat": "Savannah and Forests",
        "lifespan_years": 60,
        "diet": "Herbivore"
    },
    "3": {
        "name": "Penguin",
        "description": "Burung yang tidak bisa terbang dan hidup di lingkungan dingin.",
        "habitat": "Antarctica",
        "lifespan_years": 20,
        "diet": "Carnivore"
    }
}

# Endpoint untuk mendapatkan semua hewan
class AnimalList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(animals),
            "animals": animals
        }

# Endpoint untuk mendapatkan detail hewan berdasarkan ID
class AnimalDetail(Resource):
    def get(self, animal_id):
        if animal_id in animals:
            return {
                "error": False,
                "message": "Success",
                "animal": animals[animal_id]
            }
        return {"error": True, "message": "Animal not found"}, 404

# Endpoint untuk menambahkan hewan baru
class AddAnimal(Resource):
    def post(self):
        data = request.get_json()
        animal_id = str(len(animals) + 1)
        new_animal = {
            "name": data.get("name"),
            "description": data.get("description"),
            "habitat": data.get("habitat"),
            "lifespan_years": data.get("lifespan_years"),
            "diet": data.get("diet")
        }
        animals[animal_id] = new_animal
        return {
            "error": False,
            "message": "Animal added successfully",
            "animal": new_animal
        }, 201

# Endpoint untuk mengupdate data hewan berdasarkan ID
class UpdateAnimal(Resource):
    def put(self, animal_id):
        if animal_id in animals:
            data = request.get_json()
            animal = animals[animal_id]
            animal["name"] = data.get("name", animal["name"])
            animal["description"] = data.get("description", animal["description"])
            animal["habitat"] = data.get("habitat", animal["habitat"])
            animal["lifespan_years"] = data.get("lifespan_years", animal["lifespan_years"])
            animal["diet"] = data.get("diet", animal["diet"])
            return {
                "error": False,
                "message": "Animal updated successfully",
                "animal": animal
            }
        return {"error": True, "message": "Animal not found"}, 404

# Endpoint untuk menghapus data hewan berdasarkan ID
class DeleteAnimal(Resource):
    def delete(self, animal_id):
        if animal_id in animals:
            deleted_animal = animals.pop(animal_id)
            return {
                "error": False,
                "message": "Animal deleted successfully",
                "animal": deleted_animal
            }
        return {"error": True, "message": "Animal not found"}, 404

# Menambahkan endpoint ke API
api.add_resource(AnimalList, '/animals')
api.add_resource(AnimalDetail, '/animals/<string:animal_id>')
api.add_resource(AddAnimal, '/animals/add')
api.add_resource(UpdateAnimal, '/animals/update/<string:animal_id>')
api.add_resource(DeleteAnimal, '/animals/delete/<string:animal_id>')

if __name__ == '__main__':
    app.run(debug=True)
