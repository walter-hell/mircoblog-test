from app import db,models

# u1 = models.User(nickname='hell', email='102245405@qq.com')
# u2 = models.User(nickname='susan', email='susan@qq.com')
# db.session.add(u1)
# db.session.add(u2)
# db.session.commit()

# print(models.User.query.all())

#提交第一篇blog
import datetime

u = models.User.query.get(1)
p = models.Post(body='my first post!',timestamp=datetime.datetime.utcnow(), author = u)
db.session.add(p)
db.session.commit()
