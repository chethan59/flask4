from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from main import ok
import pyodbc
app = Flask(__name__)



"""

sdj.azurewebsites.net > app service
DBSERVER > mysqlserver00799.database.windows.net > networking (White list)

un - room
pw - qwer$321
db - MyDBroom

create table TestTab(
	id int PRIMARY KEY,
	name varchar(20) default Null
)

insert into [dbo].[TestTab] (id, name) values
(1, 'MPC'),
(2, 'Mysore'),
(3, 'okok')

select * from [dbo].[TestTab]

"""


@app.route('/')
def hello_world():
    ok.me()
    return "<p>Hello, World </p>"

@app.route('/db')
def db():
    ok.me()
    
    connString = "Driver={ODBC Driver 13 for SQL Server};Server=tcp:mysqlserver00799.database.windows.net,1433;Database=MyDBroom;Uid=room;Pwd=qwer$321;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    conn = pyodbc.connect(connString,)
    cursor = conn.cursor()
    query="select * from [dbo].[TestTab]"
    cursor.execute(query) 
    row = cursor.fetchall()
    #print(row)
    
    return f"<p>DB DATA : {row} </p>"


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)
    #app.debug = True
    #app.run(debug=True)
    app.run()
