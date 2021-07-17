from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class url_input(FlaskForm):
    url=StringField('',validators=[DataRequired()])
    submit=SubmitField('Check the URL')