from modle import db,Job,SQLAlchemy


# test=db.session.query(Job).filter(Job.company.like("%云计算%")).all()
# print(test)

from sqlalchemy import or_

words = ['%产品%', '%经理%',"%销售%"]

print(*[Job.jobName.like(w) for w in words])
rule = or_(*[Job.jobName.like(w) for w in words])
print(rule)
t2=Job.query.filter(rule)
print(t2)

# print(db.session.query(Job).params(company="深圳市腾讯计算机系统有限公司").all())