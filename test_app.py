import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_get_profiles(client):
    response = client.get('/profiles')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_profile_by_id_success(client):
    response = client.get('/profiles/1')
    assert response.status_code == 200
    assert 'name' in response.json


def test_get_profile_by_id_not_found(client):
    response = client.get('/profiles/999')
    assert response.status_code == 404
    assert 'error' in response.json


def test_create_profile(client):
    new_profile = {
        "name": "John Smith",
        "email": "john.smith@example.com",
        "skills": ["JavaScript", "Node.js"],
        "projects": [
            {
                "name": "Kanban API",
                "description": "A REST API with Express",
                "link": "https://github.com/johnsmith/kanban"
            }
        ]
    }
    response = client.post('/profiles', json=new_profile)
    assert response.status_code == 201
    assert response.json["name"] == "John Smith"


def test_delete_profile(client):
    # Crée un nouveau profil pour le supprimer ensuite
    response = client.post('/profiles', json={
        "name": "Temp Dev",
        "email": "temp@example.com",
        "skills": ["C++"],
        "projects": []
    })
    profile_id = response.json["id"]

    # Supprime ce profil
    delete_response = client.delete(f'/profiles/{profile_id}')
    assert delete_response.status_code == 200
    assert delete_response.json['message'] == 'Profil supprimé'


def test_get_profiles_by_skill(client):
    response = client.get('/profiles/skills?name=Python')
    assert response.status_code == 200
    assert isinstance(response.json, list)
