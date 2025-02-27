from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Password should be the same as entered above')])
    password2 = PasswordField('Repeat Password')
    email = StringField('Email Address', validators=[Length(min=4, max=100), Email()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')