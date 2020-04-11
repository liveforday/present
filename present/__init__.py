import sys
import os

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.sql import func
from flask_moment import Moment

WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"
else:
    prefix = "sqlite:////"
app = Flask("present")

app.config["SQLALCHEMY_DATABASE_URI"] = prefix + os.path.join(
    os.path.dirname(app.root_path), os.getenv("DATABASE_FILE", "data.db")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "devf")

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
moment = Moment(app)


@login_manager.user_loader
def load_user():
    from present.models import User

    user = User.query.get(int(user_id))
    return dict(user=usre)


login_manager.login_view = "login"


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.context_processor
def inject_user():
    from present.models import User, PastRecord

    latest_record = PastRecord.query.order_by(PastRecord.name.desc()).first()
    user = User.query.first()
    return dict(user=user, latest_record=latest_record)


from present import views, models, commands
