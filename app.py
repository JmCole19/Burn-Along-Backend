from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

def get_data():
    data_url = ('http://code.burnalong.com/items')
    try:
        _r = requests.get(
            data_url,
            # headers=_headers
        )
        return _r.json()
    except Exception as ee:
        print('Could not get data: {}'.format(ee))
        return None

def main():
    db.create_all()
    get_data()
# print (_r.json())
# print (_data)

# def add_to_db(_data):
#     if _data:
#         try:



@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        main()
        app.run(debug=True)