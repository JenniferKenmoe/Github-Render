from flask import Flask, jsonify, request

app = Flask(__name__)

# Données simulées
profiles = [
    {
        "id": 1,
        "name": "JenniferKenmoe",
        "email": "jenniferkenmoe17@gmail.com",
        "skills": ["Python", "Flask", "Docker"],
        "projects": [
            {
                "title": "API de blog",
                "github": "https://github.com/JenniferKenmoe/blog-api"
            }
        ]
    }
]


# GET /profiles - liste tous les profils
@app.route('/profiles', methods=['GET'])
def get_profiles():
    return jsonify(profiles), 200


# GET /profiles/<id> - afficher un profil par ID
@app.route('/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    profile = next((p for p in profiles if p['id'] == profile_id), None)
    if profile:
        return jsonify(profile), 200
    return jsonify({'error': 'Profil non trouvé'}), 404


# POST /profiles - créer un nouveau profil
@app.route('/profiles', methods=['POST'])
def create_profile():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Aucune donnée envoyée'}), 400
    data['id'] = profiles[-1]['id'] + 1 if profiles else 1
    profiles.append(data)
    return jsonify(data), 201


# DELETE /profiles/<id> - supprimer un profil
@app.route('/profiles/<int:profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    global profiles
    profiles = [p for p in profiles if p['id'] != profile_id]
    return jsonify({'message': 'Profil supprimé'}), 200


# GET /profiles/skills?name=Python - profils par compétence
@app.route('/profiles/skills', methods=['GET'])
def get_profiles_by_skill():
    skill = request.args.get('name')
    if not skill:
        return jsonify({'error': 'Paramètre "name" requis'}), 400
    filtered = [p for p in profiles if skill in p.get('skills', [])]
    return jsonify(filtered), 200

# Point d'entrée pour Render
    if __name__ == '__main__':
        app.run(debug=True)
