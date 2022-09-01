from database import db

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)

    def __str__(self):
        return f'User(id:{self.id}, name:{self.name}, email:{self.email})'