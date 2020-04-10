from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length


class addPresent(FlaskForm):
    present_name = StringField("Present name:", validators=[DataRequired()])
    submit = SubmitField("add")


class BinggoPresent(FlaskForm):
    binggo_name = HiddenField("Binggo name:", validators=[DataRequired()])
    submit = SubmitField("确定")
