from flask import make_response,Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import test
app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xk.981008@home.klzy.me:5306/testDB?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xk.981008@10.255.46.97:3306/testDB?charset=utf8'
@app.route('/')
def hello():
    resp=make_response(test.test())
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__=="__main__":
    app.run(
        host='0.0.0.0')