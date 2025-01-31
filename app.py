from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Allow cross-origin requests

# Temporary storage (mock database)
about = []

#Returns basic information about the API along with the current UTC timestamp.
@app.route("/")
def get_info():
    return jsonify({
        "id": 1,
        "name": "Ezenagu Chinemerem",
        "email": "chinemeremezenagu@gmail.com",
        "github_url": "https://github.com/Pascal509/Public_API",
        "current_datetime": datetime.utcnow().isoformat() + "Z"
    })

#returns a list of all people stored in database.
@app.route("/about", methods=["GET"])
def about_me():
    return jsonify(about)

#Adds allows you to add a new person to the "about" list
@app.route("/about", methods=["POST"])
def create_about():
    data = request.get_json()
    new = {"id": len(about) + 1, "name": data.get("name")}
    about.append(new)
    return jsonify({"message": "Item created", "item": new}), 200

#updates the name of a person with the specified about_id
@app.route("/about/<int:about_id>", methods=["PUT"])
def update_about(about_id):
    data = request.get_json()
    for person in about:
        if person["id"] == about_id:
            person["name"] = data.get("name", person["name"])
            return jsonify({"message": "person updated", "person":person})
    return jsonify({"error": "person not found"}), 404

#deletes the person with the specified about_id
@app.route("/about/<int:about_id>", methods=["DELETE"])
def delete_item(about_id):
    global about
    about = [person for person in about if person["id"] != about_id]
    return jsonify({"message": "person deleted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))