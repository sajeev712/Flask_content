from flask import Flask,redirect,url_for,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Registor,Base

engine=create_engine('sqlite:///bvc.db',connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind=engine

DBsession=sessionmaker(bind=engine)
session=DBsession()



app=Flask('__name__')
@app.route('/home')
def hello():
	return "<h1>hello welcome to home <h1>"
@app.route('/about')
def about():
	return "this is about page"
@app.route('/data/<name>/<age>/<number>/<marks>/<roll>')
def data(name,age,number,marks,roll):
	name="BaluSatya"
	age="19"
	number="9133787918"
	marks="6.8"
	roll="573"
	return "my name is {}<p> age is{}</p><p> mobile number is {}</p><p> marks in first year is {}</p><p> roll number is {}".format(name,age,number,marks,roll)

@app.route('/admin')
def admin():
	return render_template("sample.html")
@app.route("/student")
def student():
	return "<font color='blue'>hello welcome to student page</font>"

@app.route("/faculty")
def faculty():
	return "welcome to faculty data"




@app.route("/person/<uname>/<uage>/<unumber>/<umarks>/<uroll>")
def person(uname,uage,unumber,umarks,uroll):
	return render_template("samp.html",name=uname,age=uage,number=unumber,marks=umarks,roll=uroll)




@app.route("/table/<int:num>")
def table(num):
	return render_template("table.html",n=num)

dummy_data=[
{'name':'SAJEEV',
'org':'BVC',
'dob':'22 NOV 2000'},
{'name':'BALU',
'org':'BVC',
'dob':'14 NOV 1999'}]

@app.route("/showdata")
def showdata():
	return render_template("show_data.html",d=dummy_data)

@app.route("/register")
def reg():
	return render_template("register.html")




@app.route("/user/<name>")
def user(name):
	if name=='faculty':
		return redirect(url_for('faculty'))
	elif name=='student':
		return redirect(url_for('student'))
	elif name == 'admin':
		return redirect(url_for('admin'))
	else:
		return "<h3>There is no url<h3>"


@app.route("/file")
def fileupload():
	return render_template("fileupload.html")

@app.route("/success", methods=["POST","GET"])
def success():
	if request.method=="POST":
		f=request.files["file"]
		f.save(f.filename)
		return render_template("display.html",name= f.filename)

@app.route("/show_data")
def showData():
	registor=session.query(Registor).all()
	return render_template('show.html',register=registor)


@app.route('/add',methods=["POST","GET"])
def addData():
	if request.method=='POST':
		newData=Registor(name=request.form['name'],surname=request.form['surname'],roll_no=request.form['roll_no'],
			mobile=request.form['mobile'],branch=request.form['branch'])
		session.add(newData)
		session.commit()

		return redirect(url_for('showData'))
	else:
		return render_template('new.html')

@app.route('/<int:register_id>/edit',methods=["POST","GET"])
def editData(register_id):
	edited_Data=session.query(Registor).filter_by(id=register_id).one()
	if request.method == "POST":
		edited_Data.name=request.form['name']
		edited_Data.surname=request.form['surname']
		edited_Data.roll_no=request.form['roll_no']
		edited_Data.mobile=request.form['mobile']
		edited_Data.branch=request.form['branch']
		session.add(edited_Data)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('edit.html',register=edited_Data)


@app.route('/<int:register_id>/delete',methods=["POST","GET"])
def deleteData(register_id):
	deletedData=session.query(Registor).filter_by(id=register_id).one()

	if request.method=="POST":
		session.delete(deletedData)
		session.commit()
		return redirect(url_for('showData',register_id=register_id))
	else:
		return render_template('delete.html',register=deletedData)


if __name__ == '__main__':
	app.run(debug=True)