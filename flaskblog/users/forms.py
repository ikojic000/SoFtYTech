from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField, FileField, SelectField, SelectMultipleField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_wtf.file import FileAllowed
from flaskblog.models import User
from flask_login import current_user


# Function for checking if username is taken when new user registers
def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError('That username is taken. Please choose a different one!')

# Function for checking if email is taken when new user registers
def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('That email is taken. Please choose a different one!')

# Function for checking if username is taken when user updates username
def validate_username_update(self, username):
    if username.data != current_user.username:
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose another one!')

# Function for checking if email is taken when user updates email
def validate_email_update(self, email):
    if email.data != current_user.email:
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken. Please choose another one!')

# FORMS
# USER SIDE FORMS
# Form for registration
class RegisterForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=3, max=15), validate_username])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), validate_email])
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# Form for updating user account
class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=3, max=15), validate_username_update])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), validate_email_update])
    submit = SubmitField('Update')

# Form for Roles - Admin
class UpdateAccountRoleForm(FlaskForm):
    role = StringField('Role',
                validators=[DataRequired()])
    submit = SubmitField('Update')
    
# Form for loging in
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    submit = SubmitField('Login')