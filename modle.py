from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    # __tablename__="郁峻峰牛批"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    jobName = db.Column(db.TEXT,default="NULL")
    company = db.Column(db.TEXT,default="NULL")
    city = db.Column(db.TEXT,default="NULL")
    pay = db.Column(db.TEXT,default="NULL")
    date = db.Column(db.TEXT,default="NULL")
    def __init__(self,jobName,company,city,pay,date):
        self.jobName=jobName
        self.company=company
        self.pay=pay
        self.date=date
    def __repr__(self):
        return '<company %r>' % self.company

# db.create_all()


