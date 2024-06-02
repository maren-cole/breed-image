from flask import Flask, jsonify, send_from_directory, abort
import os

app = Flask(__name__)

breeds = {
    "Arabian": "arabian.jpg",
    "Andalusian": "andalusian.jpg",
    "Thoroughbred": "thoroughbred.jpg",
    "Clydesdale": "clydesdale.jpg",
    "Irish Sport Horse": "irish_sport_horse.jpg",
    "Quarter Horse": "quarter_horse.jpg",
    "Standardbred": "standardbred.jpg",
    "Tennessee Walker": "tennessee_walker.jpg"
}


@app.route('/breed-image/<breed>', methods=['GET'])
def get_breed_image(breed):
    breed = breed.capitalize()
    if breed in breeds:
        filename = breeds[breed]
        return send_from_directory(os.path.join(app.root_path, 'static'), filename)
    else:
        return jsonify({"error": "Breed not found"}), 404


if __name__ == '__main__':
    app.run()
