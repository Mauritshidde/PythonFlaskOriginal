from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3, json, collections, sys, os
from forms import HomeForm, ToevoegenForm, VerwijderenForm, BekijkenForm, BekijkenPrintForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd1ccabe4c9d3d5813ba8881bd1082fef'
y = {}
contact_mogelijkheden = {""}
keuze_mogelijkheden = {"achternaam", "tel_nummer", "land"}
conn = sqlite3.connect('Telefoonboek.db')
c = conn.cursor()

#c.execute("""CREATE TABLE Telefoonboek (
            #naam text,
            #achternaam text,
            #land,
            #tel_nummer int
            #)""")

def maak_API(y):
    conn = sqlite3.connect('Telefoonboek.db')
    c = conn.cursor()
    c.execute("SELECT naam, achternaam, land ,tel_nummer FROM Telefoonboek")
    rows = c.fetchall()
    rowarray_list = []
    for row in rows:
        x = {
            row[0]: {
                'achternaam': row[1],
                'land': row[2],
                'tel_nummer': row[3]}
            }
        xz = {row[0]}
        contact_mogelijkheden.update(xz)
        y.update(x)

        with open("Telefoonboek.json", "w") as write_file:
            json.dump(y, write_file)

def contact_toevoegen(gekozen_naam, gekozen_achternaam, gekozen_tel_nummer, gekozen_land):
    conn = sqlite3.connect('Telefoonboek.db')
    c = conn.cursor()
    os.system('cls' if os.name == 'nt' else 'clear')
    in_Telefoonboek = c.execute("SELECT * FROM Telefoonboek WHERE naam = :first AND achternaam = :last",
                {'first': gekozen_naam, 'last': gekozen_achternaam}).fetchall()
    if in_Telefoonboek:
        return redirect(url_for('home'))
    else:
        c.execute("INSERT INTO Telefoonboek VALUES ('{}', '{}', '{}', {})".format(gekozen_naam, gekozen_achternaam, gekozen_land, gekozen_tel_nummer))
        conn.commit()
        return redirect(url_for('home'))


def contact_verwijderen(gekozen_naam_verw, gekozen_achternaam_verw):
    conn = sqlite3.connect('Telefoonboek.db')
    c = conn.cursor()
    os.system('cls' if os.name == 'nt' else 'clear')
    in_Telefoonboek = c.execute("SELECT * FROM Telefoonboek WHERE naam = :first AND achternaam = :last",
                {'first': gekozen_naam_verw, 'last': gekozen_achternaam_verw}).fetchall()
    if in_Telefoonboek:
        c.execute("DELETE from Telefoonboek WHERE naam = :first AND achternaam = :last",
                    {'first': gekozen_naam_verw, 'last': gekozen_achternaam_verw})
    else:
        print("Dat is niet mogelijk. ")

    conn.commit()

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

@app.route('/bekijken', methods=['GET', 'POST'])
def bekijken():
    form = BekijkenForm()
    form2 = BekijkenPrintForm()
    if form.validate_on_submit():
        maak_API(y)
        naam_bekijken = form.naam_bekijken.data
        achternaam_bekijken = form.achternaam_bekijken.data
        if naam_bekijken in y:
            if y[naam_bekijken]["achternaam"] == achternaam_bekijken:
                naam_api2 = naam_bekijken
                achternaam_api2 = y[naam_bekijken]["achternaam"]
                tel_nummer_api2 = y[naam_bekijken]["tel_nummer"]
                land_api2 = y[naam_bekijken]["land"]
                return render_template('bekijkenprint.html', title='Login', form=form2, naam_api=naam_api2, achternaam_api=achternaam_api2, tel_nummer_api=tel_nummer_api2, land_api=land_api2)
            else:
                return redirect(url_for('home'))
        else:
            print("kan niet")
    return render_template('bekijken.html', title='Login', form=form)

@app.route('/toevoegen', methods=['GET', 'POST'])
def toevoegen():
    form = ToevoegenForm()
    if form.validate_on_submit():
        if form.keuze_persoon.data == "confirm":
            gekozen_naam = form.naam_toevoegen.data
            gekozen_achternaam = form.achternaam_toevoegen.data
            gekozen_tel_nummer = form.tel_nummer_toevoegen.data
            gekozen_land = form.land_toevoegen.data
            gelukt = ""
            contact_toevoegen(gekozen_naam, gekozen_achternaam, gekozen_tel_nummer, gekozen_land)
        elif form.keuze_persoon.data == "cancel":
            return redirect(url_for('home'))


    return render_template('toevoegen.html', title='Login', form=form)

@app.route('/verwijderen', methods=['GET', 'POST'])
def verwijderen():
    form = VerwijderenForm()
    if form.validate_on_submit():
        if form.keuze_persoon.data == "confirm":
            gekozen_naam_verw = form.naam_verwijderen.data
            gekozen_achternaam_verw = form.achternaam_verwijderen.data
            contact_verwijderen(gekozen_naam_verw, gekozen_achternaam_verw)
            return redirect(url_for('home'))
        elif form.keuze_persoon.data == "cancel":
            return redirect(url_for('toevoegen'))
    return render_template('verwijderen.html', title='Login', form=form)

@app.route('/aanpassen')
def aanpassen():
    form = AanpassenForm()
    return render_template('aanpassen.html', title='Login', form=form)

app.run(host='localhost', port=8080, debug=True)
