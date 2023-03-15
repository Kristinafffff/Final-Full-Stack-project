
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from notebook_app.models import User


class UpdateNoteForm(FlaskForm):
	subject = StringField('Kategorija', validators=[DataRequired()])
	notes = TextAreaField('Užrašas', validators=[DataRequired()])

	updateNoteBtn = SubmitField('Atnaujinti')

class NewSubjectForm(FlaskForm):
	subjects_name = StringField('Įrašykite naują kategoriją čia', validators=[DataRequired()])
	
	submitSubjectUpdateBtn = SubmitField('IŠSAUGOTI')

class RegistrationForm(FlaskForm):
	username = StringField('Prisijungimas', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("El. paštas", validators=[DataRequired(), Email()])
	password = PasswordField('Slaptažodis', validators=[DataRequired()])
	confirm_pasword = PasswordField('Pakartoti slaptažodį', validators=[DataRequired()])

	RegisterBtn = SubmitField('Prisijungti')

	

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Šis el. paštas jau yra. Pasirinkite kitą el. paštą')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('Šis el. paštas jau yra. Pasirinkite kitą el. paštą')



class LoginForm(FlaskForm):
	email = StringField("El. paštas", validators=[DataRequired(), Email()])
	password = PasswordField('Slaptažodis', validators=[DataRequired()])

	loginBtn = SubmitField('Prisijungti')


# UPDATE ACCOUNT FORM 

class UpdateAccountForm(FlaskForm):
	username = StringField('Prisijungimas', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("El. paštas", validators=[DataRequired(), Email()])

	updateAccBtn = SubmitField('Atnaujinti')

	# Validations

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Šis el. paštas jau yra. Pasirinkite kitą el. paštą')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('Šis el. paštas jau yra. Pasirinkite kitą el. paštą')




