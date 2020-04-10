from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from present import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class PastRecord(db.Model):
    __tablename__ = "past_record"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True)
    binggo_name = db.Column(db.String(20))

    past_record2presents = db.relationship(
        "Present", back_populates="presents2past_record"
    )


class Present(db.Model):
    __tablename__ = "present"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    past_id = db.Column(db.Integer, db.ForeignKey("past_record.id"))
    presents2past_record = db.relationship(
        "PastRecord", back_populates="past_record2presents"
    )
