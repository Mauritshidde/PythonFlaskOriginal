from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3, json, collections, sys, os
from forms import HomeForm, BekijkenForm, ToevoegenForm, VerwijderenForm, AanpassenForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd1ccabe4c9d3d5813ba8881bd1082fef'

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = HomeForm()
    if form.validate_on_submit():
        if form.keuze_persoon_home.data == "bekijk_persoon":
            return redirect(url_for('bekijken'))
        elif form.keuze_persoon_home.data == "toevoegen_persoon":
            return redirect(url_for('toevoegen'))
        elif form.keuze_persoon_home.data == "verwijderen_persoon":
            return redirect(url_for('verwijderen'))
        elif form.keuze_persoon_home.data == "aanpassen_persoon":
            return redirect(url_for('aanpassen'))
        else:
            return redirect(url_for('home'))
    return render_template('index.html', title='Login', form=form)

@app.route('/bekijken')
def bekijken():
    form = BekijkenForm()
    return render_template('bekijken.html', title='Login', form=form)

@app.route('/toevoegen')
def toevoegen():
    form = ToevoegenForm()
    return render_template('toevoegen.html', title='Login', form=form)

@app.route('/verwijderen')
def verwijderen():
    form = VerwijderenForm()
    return render_template('verwijderen.html', title='Login', form=form)

@app.route('/aanpassen')
def aanpassen():
    form = AanpassenForm()
    return render_template('aanpassen.html', title='Login', form=form)

app.run(host='localhost', port=8080, debug=True)
