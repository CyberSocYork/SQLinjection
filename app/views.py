from app import app, database
from flask import render_template, request
import sqlite3



SQL_query = '''SELECT customers.Firstname, customers.LastName, customers.Address,
            customers.Phone, customers.Email
            FROM customers
            WHERE customers.CustomerId=?'''


#SQL_query2 = "SELECT tracks.Name, tracks.Composer FROM tracks WHERE tracks.TrackId = {}".format(customerId)


@app.route('/', methods=['GET','POST'])
def index():

    if request.method == "GET":
        return render_template('index.html')

    elif request.method == "POST":

        customerId = request.form.get('customerId', "")
        conn = database.create_connection()
        if conn is not None:
            cur = conn.cursor()
            try:
                cur.execute("SELECT tracks.Name, tracks.Composer FROM tracks WHERE tracks.TrackId = {}".format(customerId))
            except sqlite3.OperationalError as e:
                return e.__str__()
            except sqlite3.Warning as e:
                return e.__str__()
            rows = cur.fetchall()
            print(rows)
            return render_template('index.html',output=rows)




