from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired

class UserDataForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                                choices=[('expense', 'expense'),
                                        ('income', 'income')])
#    category = SelectField("Category", validators=[DataRequired()],
#                                            choices =[('rent', 'rent'),
#                                            ('salary', 'salary'),
#                                            ('investment', 'investment'),
#                                            ('side_hustle', 'side_hustle')
#                                            ]
#                            )
    category = StringField('category', validators = [DataRequired()])  
    amount = FloatField('Amount', validators = [DataRequired()])     
    date = DateField('date', validators = [DataRequired()])                                
    submit = SubmitField('Generate Report')                            