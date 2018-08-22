from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rose_data.db'
db = SQLAlchemy(app)

class Wine(db.Model):
  __tablename__ = 'wines'
  __table_args__ = {
    'autoload': True,
    'autoload_with': db.engine
  }
  index = db.Column(db.Integer, primary_key=True)


@app.route("/")
def hello():
  return "Do you like rosé wine? Do you like California? Find below all rosé wines produced in Napa Valley!"

@app.route("/wines/")
def list():
  wines = Wine.query.all()
  return render_template("list.html", wines=wines)

@app.route("/wines/<index>/")
def wine(index):
  wine = Wine.query.filter_by(index=index).first()
  return render_template("show.html", wine=wine)

if __name__ == "__main__":
  app.run(debug=True)