from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class PracownicyForm(FlaskForm):
	imie = StringField('inputImie', validators=[DataRequired(), Length(min=2,max=30)])
	nazwisko = StringField('inputNazwisko', validators=[DataRequired(), Length(min=2,max=30)])
	ulica = StringField('inputUlica', validators=[DataRequired(), Length(max=30)])
	numer = StringField('inputNumer', validators=[DataRequired(), Length(max=30)])
	kod = StringField('inputKod', validators=[DataRequired(), Length(max=30)])
	miejscowosc = StringField('inputMiejscowosc', validators=[DataRequired(), Length(max=30)])
	pesel = StringField('inputPesel', validators=[Length(max=30)])
	dowod = StringField('inputDowod', validators=[Length(max=30)])
	stanowisko = SelectField('inputStanowisko', coerce=int)
	submit = SubmitField('Dodaj')
