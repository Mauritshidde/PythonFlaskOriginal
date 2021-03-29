from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, email_validator, EqualTo

class HomeForm(FlaskForm):
    keuze_persoon_home = SelectField('keuze uit', choices=["toevoegen_persoon", "verwijderen_persoon", "aanpassen_persoon", "bekijk_persoon"], validators=[DataRequired()])
    submit = SubmitField('gekozen')

class VerwijderenForm(FlaskForm):
    naam_verwijderen = StringField('naam', validators=[DataRequired()])
    achternaam_verwijderen = StringField('achternaam', validators=[DataRequired()])
    keuze_persoon = SelectField('keuze uit', choices=["confirm", "cancel"], validators=[DataRequired()])
    submit = SubmitField('Verwijder')

class BekijkenForm(FlaskForm):
    naam_bekijken = StringField('naam', validators=[DataRequired()])
    achternaam_bekijken = StringField('achternaam', validators=[DataRequired()])
    keuze_persoon = SelectField('keuze uit', choices=["confirm", "cancel"], validators=[DataRequired()])
    submit = SubmitField('Bekijk')

class ToevoegenForm(FlaskForm):
    naam_toevoegen = StringField('naam', validators=[DataRequired()])
    achternaam_toevoegen = StringField('achternaam', validators=[DataRequired()])
    land_toevoegen = StringField('land', validators=[DataRequired()])
    tel_nummer_toevoegen = StringField('tel_nummer', validators=[DataRequired()])
    keuze_persoon = SelectField('keuze uit', choices=["confirm", "cancel"], validators=[DataRequired()])
    submit = SubmitField('Toevoegen')

class BekijkenPrintForm(FlaskForm):
    submit = SubmitField('Sign Up')
