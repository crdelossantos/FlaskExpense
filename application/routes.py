from application import app
from flask import render_template, url_for, redirect,flash, get_flashed_messages
from application.form import UserDataForm
from application.models import IncomeExpenses
from application import db
import json
import sqlite3
import csv
import datetime

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    return render_template('index.html', entries = entries)


@app.route('/add', methods = ["POST", "GET"])
def add_expense():
    form = UserDataForm()
    if form.validate_on_submit():
        entry = IncomeExpenses(type=form.type.data, category=form.category.data, amount=form.amount.data, date=form.date.data)
        db.session.add(entry)
        db.session.commit()
        flash(f"{form.type.data} has been added to {form.type.data}s", "success")
        return redirect(url_for('index'))
    return render_template('add.html', title="Add expenses", form=form)
    


@app.route('/delete-post/<int:entry_id>')
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for("index"))

#He añadido esto a ver si funciona @app.route('/download')
@app.route('/download')
def download():
    con = sqlite3.connect('expenseDB.db')
    # Get the current date and time
    now = datetime.datetime.now()
    # Format the date as a string
    date_string = now.strftime("%Y%m%d_%H%M")
    # Create a filename using the date string
    filename = f"{date_string}_daytoday.csv"
    query = 'select * from IncomeExpenses'
    df = pd.read_sql_query(query, con=con)
    df.set_index('id',inplace = True)
    return Response(df.to_csv(),mimetype="text/csv",headers={"Content-Disposition":"attachment;filename="+ filename}) 

@app.route('/dashboard')
def dashboard():
    income_vs_expense = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.type).group_by(IncomeExpenses.type).order_by(IncomeExpenses.type).all()

    category_comparison = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.category).group_by(IncomeExpenses.category).order_by(IncomeExpenses.category).all()

    dates = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.date).group_by(IncomeExpenses.date).order_by(IncomeExpenses.date).all()

    income_category = []
    for amounts, _ in category_comparison:
        income_category.append(amounts)

    income_expense = []
    for total_amount, _ in income_vs_expense:
        income_expense.append(total_amount)

    over_time_expenditure = []
    dates_label = []
    for amount, date in dates:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_expenditure.append(amount)

    return render_template('dashboard.html',
                            income_vs_expense=json.dumps(income_expense),
                            income_category=json.dumps(income_category),
                            over_time_expenditure=json.dumps(over_time_expenditure),
                            dates_label =json.dumps(dates_label)
                        )
