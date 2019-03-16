from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

class Contact(FlaskForm):
    email = StringField('email',validators=[DataRequired()])
    name = StringField('name',validators=[DataRequired()])
    age = IntegerField('age',validators=[DataRequired()])
    grade = SelectField('grade',validators=[DataRequired()],coerce=str)
    message = TextAreaField('message', validators=[DataRequired()])
    source = HiddenField('source', default="NAVBAR", id="contact-source")
