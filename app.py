from flask import Flask, render_template,request
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)


app.config["MYSQL_HOST"] = "demoproject2-server.mysql.database.azure.com"
app.config["MYSQL_USER"] = "ittknjtmcf"
app.config["MYSQL_PASSWORD"] = "41B7507XLZ23H22S$"
app.config["MYSQL_DB"] = "demoproject2-database"


mysql = MySQL(app)
def new_user():
    cursor = mysql.connection.cursor(MySQLdb.cursors.Cursor)
    cursor.execute('SELECT * from accountsuser')
    userdata = cursor.fetchall()
    mysql.connection.commit()
    return userdata 

def create_table():
    cursor = mysql.connection.cursor(MySQLdb.cursors.Cursor)
    cursor.execute("""
            CREATE TABLE if not exists accountsuser (
                id int NOT NULL ,
                username varchar(255),
                password varchar(255)
            );
        """)

    mysql.connection.commit()

with app.app_context():
    create_table()    

@app.route('/', methods=['GET','POST'])
def user_login():
    if request.method == "POST":
       
        id=request.form["userid"]
        username = request.form["InputUserName"]
        password = request.form["password"]
           
           
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)


        cursor.execute('INSERT INTO accountsuser VALUES (% s, % s, % s)',(id, username, password),)
           
        mysql.connection.commit()
    userdata = new_user()

    return render_template('register.html',userdata=userdata)




if __name__ == "__main__":
    app.run(debug=True)


