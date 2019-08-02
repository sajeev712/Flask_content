from flask import Flask 
app=Flask('__name__')

@app.route('/intro/<name>/<roll>')
def std(name,roll):
	name="BaluSatya"
	roll="573"
	no="91337879"
	pec1="68"
	pec2="73"
	return "My name is {}".format(name)
	return "and my roll no is {}".format(roll)
	return "mobile no"

if __name__=='__main__':
	app.run(debug=True)