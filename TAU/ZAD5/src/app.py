from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Przechowywanie użytkowników w pamięci (dla uproszczenia)
users = [
    {"id": 1, "name": "Jan Kowalski", "email": "jan@kowalski.pl"},
    {"id": 2, "name": "Anna Nowak", "email": "anna@nowak.pl"}
]


# GET /users - Zwraca listę użytkowników
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# GET /users/{id} - Zwraca szczegóły użytkownika
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        abort(404, description="User not found")
    return jsonify(user), 200


# POST /users - Tworzy nowego użytkownika
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        abort(400, description="Invalid data")

    new_user = {
        "id": max(u["id"] for u in users) + 1 if users else 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201


# PUT /users/{id} - Aktualizuje dane użytkownika
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        abort(404, description="User not found")

    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        abort(400, description="Invalid data")

    user["name"] = data["name"]
    user["email"] = data["email"]
    return jsonify(user), 200


# DELETE /users/{id} - Usuwa użytkownika
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        abort(404, description="User not found")

    users.remove(user)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)