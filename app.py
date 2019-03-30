from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xk.981008@home.klzy.me:5306/testDB?charset=utf8'
@app.route('/')
def hello():
    return "test"

if __name__=="__main__":
    app.run()