from flask import render_template, url_for
from app_filharmonia import app, db
from sqlalchemy.ext.automap import automap_base

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
app.secret_key = os.urandom(12)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Filharmonie = Base.classes.filharmonie
Uzytkownicy = Base.classes.uzytkownicy

#inny sposób na (tylko) odczyt danych z tabeli
#filharmonie = db.Table('FILHARMONIE', db.metadata, autoload=True, autoload_with=db.engine)

@app.route('/')

def index():
	#wypisuje tablice, ktore automatycznie znalazl (prawdopodobnie nie ma tych, ktore nie maja primary key (np. wiele-do-wielu))
	#for c in Base.classes:
	#	print (c)

	#dodaje nowy rekord (na razie trzeba podac id)
	#nowa_filharmonia = Filharmonie(id_filharmonii=3, nazwa_filharmonii='Filharmonia Pomorska', ulica_filharmonii='Muzyczna', nr_budynku_filharmonii='49', kod_pocztowy_filharmonii='12351', miejscowosc_filharmonii='Grajewo', numer_telefonu='888666222', liczba_sal=3)
	#db.session.add(nowa_filharmonia)
	#db.session.commit()

	#wyswietla nazwy filharmonii w bazie (wynik w konsoli)
	results = db.session.query(Filharmonie).all()
	for r in results:
		print(r.nazwa_filharmonii)

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return "Hello Boss! "


#umozliwia zalogowanie sie danymi uzytkownikow ktorzy sa w bazie
@app.route('/login', methods=['POST'])
def do_admin_login():
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])


	query = db.session.query(Uzytkownicy).filter(Uzytkownicy.username.in_([POST_USERNAME]), Uzytkownicy.passwrd.in_([POST_PASSWORD]))
	result = query.first()

	if result:
		session['logged_in'] = True
	else:
		flash('wrong password!')
	return index()

@app.route("/logout")
def logout():
	session['logged_in'] = False
	return index()

