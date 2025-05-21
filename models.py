# models.py

class Project:
    def __init__(self, name, description, link):
        self.name = name
        self.description = description
        self.link = link

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "link": self.link
        }


class Profile:
    def __init__(self, id, name, email, skills, projects):
        self.id = id
        self.name = name
        self.email = email
        self.skills = skills
        self.projects = [Project(**proj) for proj in projects]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "skills": self.skills,
            "projects": [p.to_dict() for p in self.projects]
        }
