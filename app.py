from flask import make_response,Flask,render_template
from modle import db
from sql import test_make

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xk.981008@home.klzy.me:5306/testDB?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xk.981008@10.255.46.97:3306/testDB?charset=utf8'


def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()


@app.route('/')
def hello():
    resp=make_response(test_make())
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()


if __name__=="__main__":
    init_db()
    app.run(
        host='0.0.0.0')