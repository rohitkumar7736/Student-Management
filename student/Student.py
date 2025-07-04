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
    return render_template('student.html')
@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
     t1 = request.form['t1']
     t2 = request.form['t2']
     t3 = request.form['t3']
     t4 = request.form['t4']
     t5 = request.form['t5']
     t6 = request.form['t6']
     t7 = request.form['t7']
     t8 = request.form['t8']
     t9 = request.form['t9']
     btn=request.form['b1']
     if(btn=="Save"):
      cur = mysql.connection.cursor()
      cur.execute("insert into student values("+t1+",'"+t2+"','"+t3+"','"+t4+"',"+t5+","+t6+",'"+t7+"','"+t8+"','"+t9+"')")
      mysql.connection.commit()
      cur.close()
      return redirect(url_for('index'))
     if(btn=="Delete"):
      cur = mysql.connection.cursor()
      cur.execute("Delete from student where fname='"+t2+"'")
      mysql.connection.commit()
      cur.close()
      return redirect(url_for('index')) 
     if(btn=="Update"):
      cur = mysql.connection.cursor()
      cur.execute("Update student set fname='"+t2+"', student_id="+t1+",dob='"+t4+"',phone="+t5+",mobile="+t6+",parent_id='"+t7+"',date_of_join='"+t8+"',status='"+t9+"' where lname='"+t3+"'")
      mysql.connection.commit()
      cur.close()
      return redirect(url_for('index')) 
     if(btn.lower()=="allsearch"):
      cur=mysql.connection.cursor()
      cur.execute("select * from student")
      data=cur.fetchall()
      cur.close()
      return render_template('studentsearch.html',data=data)
     if(btn.lower()=="psearch"):
      cur=mysql.connection.cursor()
      cur.execute("select * from student where Student_Id="+t1+"")
      data=cur.fetchall()
      cur.close()
      return render_template('studentsearch.html',data=data)   

     if(btn.lower()=="specialsearch"):
      col=request.form['s']
      src=request.form['src']
      cur=mysql.connection.cursor()
     if(col=="All"):
      cur.execute("select * from student")
      data=cur.fetchall()
      cur.close()
      return render_template('studentsearch.html',data=data)
    else:  
      cur.execute("select * from Student where "+col+"='"+src+"'")
      data=cur.fetchall()
      cur.close()
      return render_template('studentsearch.html',data=data)  
    
if __name__=='__main__':
	app.run(debug=True,port=5005)