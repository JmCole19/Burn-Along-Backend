from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    rating = db.Column(db.Float(4))
    summary = db.Column(db.String(300))

def __repr__(self):
	return '<Item %r>' % self.id

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)