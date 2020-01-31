from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

class PracownicyForm(FlaskForm):
	imie = StringField('inputImie', validators=[DataRequired(), Length(min=2,max=30)])
	nazwisko = StringField('inputNazwisko', validators=[DataRequired(), Length(min=2,max=60)])
	ulica = StringField('inputUlica', validators=[DataRequired(), Length(max=50)])
	numer = StringField('inputNumer', validators=[DataRequired(), Length(max=10)])
	kod = StringField('inputKod', validators=[DataRequired(), Length(max=5)])
	miejscowosc = StringField('inputMiejscowosc', validators=[DataRequired(), Length(max=30)])
	pesel = StringField('inputPesel', validators=[Length(max=11)])
	dowod = StringField('inputDowod', validators=[Length(max=9)])
	stanowisko = SelectField('inputStanowisko', coerce=int)
	submit = SubmitField('Dodaj')

class DeleteForm(FlaskForm):
	id_action = IntegerField('inputId', validators=[DataRequired()])
	submit_delete = SubmitField('Wykonaj')

class ModifyForm(FlaskForm):
	id_action = IntegerField('inputId', validators=[DataRequired()])
	submit_modify = SubmitField('Wykonaj')

class ConfirmDeleteForm(FlaskForm):
	submit_confirm = SubmitField('Tak')

class ApplyModifyForm(FlaskForm):
	imie = StringField('inputImie', validators=[Length(max=30)])
	nazwisko = StringField('inputNazwisko', validators=[Length(max=60)])
	ulica = StringField('inputUlica', validators=[Length(max=50)])
	numer = StringField('inputNumer', validators=[Length(max=10)])
	kod = StringField('inputKod', validators=[Length(max=5)])
	miejscowosc = StringField('inputMiejscowosc', validators=[Length(max=30)])
	pesel = StringField('inputPesel', validators=[Length(max=11)])
	dowod = StringField('inputDowod', validators=[Length(max=9)])
	stanowisko = SelectField('inputStanowisko', coerce=int)
	submit_apply = SubmitField('Zmień')
