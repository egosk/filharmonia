from flask import flash, redirect, render_template, request, session, abort, url_for
from app_filharmonia import app, db
from sqlalchemy.ext.automap import automap_base
from datetime import datetime
import os
app.secret_key = os.urandom(12)
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
app.secret_key = os.urandom(12)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Filharmonie = Base.classes.filharmonie
Uzytkownicy = Base.classes.uzytkownicy
Klienci = Base.classes.klienci
Pracownicy = Base.classes.pracownicy
Bilety = Base.classes.bilety
user_id = 1

#Pracownicy = Base.classes.pracownicy
#Stanowiska = Base.classes.stanowiska

#inny sposób na (tylko) odczyt danych z tabeli
#filharmonie = db.Table('FILHARMONIE', db.metadata, autoload=True, autoload_with=db.engine)

from app_filharmonia.models import Pracownicy, Stanowiska
from app_filharmonia.forms import PracownicyForm

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
	# results = db.session.query(Filharmonie).all()
	# for r in results:
	# 	print(r.nazwa_filharmonii)

	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		bilety = db.session.query(Bilety).filter_by(id_klienta=user_id).all()
		user = db.session.query(Klienci).filter_by(id_klienta=user_id).first()

		return render_template('profile.html', loggedin=session.get('logged_in'), bilety=bilety, user=user)
		#return render_template('dashboard.html', title='Flask-Login Tutorial.', template='dashboard-template', body="You are now logged in!")


#umozliwia zalogowanie sie danymi uzytkownikow ktorzy sa w bazie
@app.route('/login', methods=['POST'])
def do_admin_login():
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])


	query = db.session.query(Klienci).filter(Klienci.login_klienta.in_([POST_USERNAME]), Klienci.haslo_klienta.in_([POST_PASSWORD]))
	user = db.session.query(Klienci).filter_by(login_klienta=POST_USERNAME).first()
	global user_id
	user_id =user.id_klienta

	#zmienna przelaczajaca widok zalogowany/niezalogowany (na probe)
	session['logged_in'] = True

	result = query.first()
	if result and POST_USERNAME == "admin":
		bilety = db.session.query(Bilety).all()
		return render_template('index.html', loggedin=session.get('logged_in'))
		#return render_template('admin_view.html', loggedin=session.get('logged_in'), bilety=bilety)
	if result:
		session['logged_in'] = True
	else:
		flash('WRONG CREDENTIALS!')
	return index()

	# if POST_USERNAME == 'admin':
	# 	return render_template('index.html', loggedin=session.get('logged_in'))
	# else:
	# 	bilety = db.session.query(Bilety).filter_by(id_klienta=user_id).all()
	# 	user = db.session.query(Klienci).filter_by(id_klienta=user_id).first()
	#
	# 	return render_template('profile.html', loggedin=session.get('logged_in'), bilety=bilety, user=user)

@app.route('/pracownicy')

def pracownicy():

	lista_pracownikow = db.session.query(Pracownicy).all()

	for x in lista_pracownikow:
		print(x.nazwisko_pracownika)

	return render_template('pracownicy.html', loggedin=session.get('logged_in'), lista_pracownikow=lista_pracownikow)

@app.route('/pracownicy/add', methods=['GET','POST'])

def pracownicy_add():

	lista_stanowisk = db.session.query(Stanowiska).all()
	form = PracownicyForm()

	form.stanowisko.choices = [(g.id_stanowiska, g.nazwa_stanowiska) for g in lista_stanowisk]

	if form.validate_on_submit():
		to_send = Pracownicy(imie_pracownika=form.imie.data, nazwisko_pracownika=form.nazwisko.data,
			ulica_zam_pracown=form.ulica.data, nr_budynku_zam_pracown=form.numer.data,
			kod_pocztowy_zam_pracown=form.kod.data, miejscowosc_zam_pracown=form.miejscowosc.data,
			data_zatrudnienia=datetime.utcnow(), id_filharmonii='1', id_stanowiska=form.stanowisko.data)

		db.session.add(to_send)
		db.session.commit()

		#flash(f'Dodano pracownika {form.imie.data} {form.nazwisko.data}', 'success')
		return redirect(url_for('pracownicy'))

	return render_template('pracownicy_add.html', loggedin=session.get('logged_in'), lista_stanowisk=lista_stanowisk, form=form)

@app.route('/pracownicy/delete')

def pracownicy_delete():

	return render_template('pracownicy_delete.html', loggedin=session.get('logged_in'))

@app.route('/pracownicy/modify')

def pracownicy_modify():

	return render_template('pracownicy_modify.html', loggedin=session.get('logged_in'))





@app.route("/logout")
def logout():
	session['logged_in'] = False
	return index()

@app.route("/admin_view")
def admin_view():
	bilety = db.session.query(Bilety).all()
	return render_template('admin_view.html', loggedin=session.get('logged_in'), bilety=bilety)