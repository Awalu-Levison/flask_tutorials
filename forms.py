from types import MethodType
from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


"""Ctreate a registration form"""
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                             validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('Sign Up')
    
    
    """Ctreate a Login form"""
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')