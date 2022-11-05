from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from main import ok
#import pyodbc
import pymssql
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
	try: 
	    #ok.me()

	    ser = "mysqlserver00799.database.windows.net"
	    us = "room"
	    pw = "qwer$321"
	    db = "MyDBroom"

	    conn = pymssql.connect(ser, us, pw, db , port='1433')
	    cursor = conn.cursor(as_dict=False)
	    cursor.execute("select * from [dbo].[TestTab]")
	    temp = []
	    for row in cursor:
	        temp.append(temp)

	    return f"<p>DB DATA : {temp} </p>"
	except Exception as e:
		return f"error : {e}"
	


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)
    #app.debug = True
    #app.run(debug=True)
    app.run()
