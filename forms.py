from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, email_validator, EqualTo

class HomeForm(FlaskForm):
    keuze_persoon_home = SelectField('keuze uit', choices=["toevoegen_persoon", "verwijderen_persoon", "aanpassen_persoon", "bekijk_persoon"], validators=[DataRequired()])
    submit = SubmitField('gekozen')

class BekijkenForm(FlaskForm):
    naam_bekijken = StringField('naam', validators=[DataRequired()])
    achternaam_bekijken = StringField('achternaam', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class ToevoegenForm(FlaskForm):
    naam_toevoegen = StringField('naam', validators=[DataRequired()])
    achternaam_toevoegen = StringField('achternaam', validators=[DataRequired()])
    land_toevoegen = StringField('land', validators=[DataRequired()])
    tel_nummer_toevoegen = StringField('tel_nummer', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class VerwijderenForm(FlaskForm):
    naam_verwijderen = StringField('naam', validators=[DataRequired()])
    achternaam_verwijderen = StringField('achternaam', validators=[DataRequired()])
    land_verwijderen = StringField('land', validators=[DataRequired()])
    tel_nummer_verwijderen = StringField('tel_nummer', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class AanpassenForm(FlaskForm):
    naam_aanpassen = StringField('naam', validators=[DataRequired()])
    achternaam_aanpassen = StringField('achternaam', validators=[DataRequired()])
    land_aanpassen = StringField('land', validators=[DataRequired()])
    tel_nummer_aanpassen = StringField('tel_nummer', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
