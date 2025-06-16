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
    return render_template('Login.html')
@app.route("/submit",methods=['POST'])
def submit():
 if request.method=='POST':
  t1=request.form['t1']
  t2=request.form['t2']
  b1=request.form['b1']
  if(b1=="Login"):
   cur=mysql.connection.cursor()
   cur.execute("SELECT * FROM Login")
   data=cur.fetchall()
   cur.close()
   return render_template("Login.html",data=data,t1=t1,t2=t2)  

@app.route('/menu')
def mymenu():
   return render_template('menu.html')  

@app.route("/loginsubmit",methods=['post'])
@app.route('/Classroom')
def classroom():
   return render_template('Classroom.html')  

@app.route("/loginsubmit",methods=['post'])
@app.route('/Attendance')
def Attendance():
   return render_template('Attendance.html')  


@app.route("/loginsubmit",methods=['post'])
@app.route('/Class_room_student')
def Class_room_student():
   return render_template('Class_room_student.html')  


@app.route("/loginsubmit",methods=['post'])
@app.route('/Course')
def Course():
   return render_template('Course.html')  


@app.route("/loginsubmit",methods=['post'])
@app.route('/Exam')
def Exam():
   return render_template('Exam.html')  


@app.route("/loginsubmit",methods=['post'])
@app.route('/Exam_type')
def Exam_type():
   return render_template('Exam_type.html')  

@app.route("/loginsubmit",methods=['post'])
@app.route('/Exam_result')
def Exam_result():
   return render_template('Exam_result.html')  


@app.route("/loginsubmit",methods=['post'])
@app.route('/Grade')
def Grade():
   return render_template('Grade.html')  


@app.route("/loginsubmit",methods=['post'])
@app.route('/Parent')
def Parent():
   return render_template('Parent.html')  


@app.route("/loginsubmit",methods=['post'])
@app.route('/Student')
def Student():
   return render_template('Student.html')  


@app.route("/loginsubmit",methods=['post'])
@app.route('/Teacher')
def Teacher():
   return render_template('Teacher.html')  




if __name__=='__main__':
	app.run(debug=True)
