import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)

@app.route("/")
def authentication():
    image_path = 'images/sign-up-page.png'
    return render_template('home.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
