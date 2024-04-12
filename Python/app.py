from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', database='db')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM students')
students = cursor.fetchall()
connection.close()
aggr=str(students[0][1])+" "+str(students[0][2])+" "+str(students[0][3])
@app.route('/')
def index():
    return render_template('index.html', student_name=aggr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)



print(students)