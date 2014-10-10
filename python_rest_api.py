from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/123.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)
#
manager = APIManager(app, flask_sqlalchemy_db=db)


class Cats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    photo = db.Column(db.String(256))

    def __unicode__(self):
        return "<Cat {0}>".format(self.name)
#
#     @classmethod
#     def query(cls):
#         return super(Cats, cls).query.filter_by(age=5)
#
#
    def name_and_age(self):
        return "%s (aged %d)" % (self.name, self.age)


@app.route('/blabla')
def hello_world():
    return 'Hello World!'

manager.create_api(Cats, methods=["GET", "POST", "PUT", "DELETE"], include_methods=["name_and_age"])

if __name__ == '__main__':
    db.create_all()
    app.run()
