from app_filharmonia import db
from datetime import date, datetime
from sqlalchemy.schema import Sequence
from sqlalchemy.dialects.oracle import *

class Pracownicy(db.Model):
	id_pracownika = db.Column(db.Integer, primary_key=True)
	imie_pracownika = db.Column(db.String(30), nullable=False)
	nazwisko_pracownika = db.Column(db.String(60), nullable=False)
	ulica_zam_pracown = db.Column(db.String(50), nullable=False)
	nr_budynku_zam_pracown = db.Column(db.String(10), nullable=False)
	kod_pocztowy_zam_pracown = db.Column(db.String(5), nullable=False)
	miejscowosc_zam_pracown = db.Column(db.String(30), nullable=False)
	pesel_pracownika = db.Column(db.String(11), nullable=True)
	dowod_pracownika = db.Column(db.String(9), nullable=True)
	data_zatrudnienia = db.Column(db.DateTime, nullable=False)
	id_stanowiska = db.Column(db.Integer, db.ForeignKey('stanowiska.id_stanowiska'), nullable=False)

	def __repr__(self):
		return f"Pracownicy('{self.imie_pracownika}', '{self.nazwisko_pracownika}')"

class Stanowiska(db.Model):
	id_stanowiska = db.Column(db.Integer, Sequence('id_stanowiska_seq'), primary_key=True)
	nazwa_stanowiska = db.Column(VARCHAR2(30), nullable=False)
	opis_stanowiska = db.Column(db.String(250), nullable=True)
	pracownicy = db.relationship('Pracownicy', backref='stanowiska', lazy=True)

	def __repr__(self):
		return f"Stanowiska('{self.nazwa_stanowiska}')"

