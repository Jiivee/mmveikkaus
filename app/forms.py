from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, RadioField, validators, ValidationError
from wtforms.validators import InputRequired, Length
from models import User


def validate_email(form, field):
    email = field.data
    print form.name.data
    if User.query.filter(User.email==email).first():
        raise ValidationError('Email is already exists')

def validate_password(form, field):
    email = form.email.data
    password = field.data
    if not User.query.filter(User.email==email, User.password==password).first():
        raise ValidationError('Username or Password is invalid')


class LoginForm(Form):
    email = TextField('Email', validators=[
        InputRequired(),
        Length(max=50)
    ])
    password = TextField('Password', validators=[
        InputRequired(),
        Length(min=2, max=50),
        validate_password
    ])


class RegistrationForm(Form):
    name = TextField('Name', validators=[
        InputRequired(),
        Length(min=2, max=50)
    ])
    email = TextField('Email', validators=[
        InputRequired(),
        Length(max=50),
        validate_email
    ])
    password = TextField('Password', validators=[
        InputRequired(),
        Length(min=2, max=50)
    ])



