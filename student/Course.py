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
    return render_template('course.html')
@app.route('/submit',methods=['POST'])
def submit():
 if request.method == 'POST':
  t1 = request.form['t1']
  t2 = request.form['t2']
  t3 = request.form['t3']
  t4 = request.form['t4']
  btn=request.form['b1']
 if(btn=="Save"):
  cur = mysql.connection.cursor()
  cur.execute("insert into course values("+t1+",'"+t2+"','"+t3+"',"+t4+")")
  mysql.connection.commit()
  cur.close()
  return redirect(url_for('index'))
 if(btn=="Delete"):
  cur=mysql.connection.cursor()
  cur.execute("delete from course where Course_Id='"+t1+"'")
  mysql.connection.commit()
  cur.close()
  return redirect(url_for('index'))
 if(btn.lower()=="update"):
  cur=mysql.connection.cursor()
  cur.execute("update Course set Course_Id='"+t1+"',Desc1='"+t3+"',Grade_Id='"+t4+"' where Name='"+t2+"'")
  mysql.connection.commit()
  cur.close()
  return redirect(url_for('index'))
 if(btn.lower()=="allsearch"):
  cur=mysql.connection.cursor()
  cur.execute("select * from course")
  data=cur.fetchall()
  cur.close()
  return render_template('coursesearch.html',data=data)
 if(btn.lower()=="psearch"):
  cur=mysql.connection.cursor()
  cur.execute("select * from course where course_id="+t1+" ")
  data=cur.fetchall()
  cur.close()
  return render_template('coursesearch.html',data=data)
 if(btn.lower()=="specialsearch"):
  col=request.form['s']
  src=request.form['src']
  cur=mysql.connection.cursor()
 if(col=="All"):
  cur.execute("select * from course")
  data=cur.fetchall()
  cur.close()
  return render_template('coursesearch.html',data=data)
 else: 
  cur.execute("select * from course where "+col+"='"+src+"'")
  data=cur.fetchall()
  cur.close()
  return render_template('courseSearch.html',data=data)
if __name__=='__main__':
	app.run(debug=True,port=5002)