from flask import Flask
app=Flask('__name__')

@app.route('/home')
def hello():
	return "<h1>hello welcome </h1>"

@app.route('/about')
def about():
	return "about page"

@app.route("/data/<name>")
def data(name):
	name="BaluSatya"
	return "Hello{}".format(name)
if __name__=='__main__':
	app.run(debug=True)