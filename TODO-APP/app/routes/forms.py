from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(message="Name required"),  Regexp(r'^[A-Za-z\s]+$',message="number not valid"), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(message="email requard"), Email(message="this is not look like a valid email"), Length(max=150, message="set your email under 150 character")])
    password = PasswordField("PASSWORD", validators=[DataRequired(message="password requird"), Length(min=6, max=200, message="password must be atlest 6 charecter long")])
    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="email requard"), Email(message="this is not look like a valid email"), Length(max=150, message="set your email under 150 character")])
    password = PasswordField("PASSWORD", validators=[DataRequired(message="password requird"), Length(min=6, max=200, message="password must be atlest 6 charecter long")])
    submit = SubmitField("Login")