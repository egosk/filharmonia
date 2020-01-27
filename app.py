from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://kwilnick:kwilnick@ora3.elka.pw.edu.pl:1521/ora3inf'
db = SQLAlchemy(app)

#inny sposób na (tylko) odczyt danych z tabeli
#filharmonie = db.Table('FILHARMONIE', db.metadata, autoload=True, autoload_with=db.engine)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Filharmonie = Base.classes.filharmonie


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

	
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)