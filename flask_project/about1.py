from flask import Flask 
app=Flask('__name__')

@app.route('/list')
def hello():
	return "Hello to the Sublime Text"


if __name__=='__main__':
	app.run(debug=True)