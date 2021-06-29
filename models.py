from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    date = db.Column(db.Date)

    def __repr__(self):
        return f'{self.title} added on {self.date}'
