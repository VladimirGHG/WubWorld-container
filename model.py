from app import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key="True")
    username = db.Column(db.String(75), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '-User {0}-'.format(self.username)

with app.app_context():
    db.create_all()
    db.session.commit()

