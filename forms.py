from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, email_validator, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')

class PersoonForm(FlaskForm):
    naam_persoon = StringField('naam', validators=[DataRequired()])
    achternaam_persoon = StringField('achternaam', validators=[DataRequired()])
    land_persoon = StringField('land', validators=[DataRequired()])
    tel_nummer_persoon = StringField('tel_nummer', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
