from flask import Flask, render_template,request,request,redirect,url_for
from flask_mysqldb import MySQL
app=Flask(__name__)
#MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'student'
mysql= MySQL(app)
@app.route('/')

def index():
    return render_template('Class_room_student.html')
@app.route('/submit',methods=['POST'])
def submit():
 if request.method == 'POST':
  t1 = request.form['t1']
  t2 = request.form['t2']
  btn=request.form['b1']
 if(btn=="Save"):
  cur = mysql.connection.cursor()
  cur.execute("insert into class_room_student values("+t1+","+t2+")")
  mysql.connection.commit()
  cur.close()
  return redirect(url_for('index'))
 if(btn=="Delete"):
  cur=mysql.connection.cursor()
  cur.execute("delete from Class_room_student where Classroom_Id="+t1+"")
  mysql.connection.commit()
  cur.close()
  return redirect(url_for('index'))
 if(btn.lower()=="update"):
  cur=mysql.connection.cursor()
  cur.execute("update Class_room_student set Student_Id="+t2+" where Classroom_Id="+t1+"")
  mysql.connection.commit()
  cur.close()
  return redirect(url_for('index'))
 if(btn.lower()=="allsearch"):
  cur=mysql.connection.cursor()
  cur.execute("select * from class_room_student")
  data=cur.fetchall()
  cur.close()
  return render_template('class_room_studentsearch.html',data=data)
 if(btn.lower()=="psearch"):
  cur=mysql.connection.cursor()
  cur.execute("select * from class_room_student where classroom_id='"+t1+"'")
  data=cur.fetchall()
  cur.close()
  return render_template('class_room_studentsearch.html',data=data)
 if(btn.lower()=="specialsearch"):
  col=request.form['s']
  src=request.form['src']
  cur=mysql.connection.cursor()
 if(col=="All"):
  cur.execute("select * from class_room_student")
  data=cur.fetchall()
  cur.close()
  return render_template('class_room_studentsearch.html',data=data)
 else:  
  cur.execute("select * from class_room_student where "+col+"='"+src+"'")
  data=cur.fetchall()
  cur.close()
  return render_template('class_room_studentsearch.html',data=data)

if __name__=='__main__':
	app.run(debug=True,port=5008)