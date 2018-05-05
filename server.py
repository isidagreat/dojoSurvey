from flask import Flask, render_template,request, redirect
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/result",methods=['POST'])
def didplayInfo():
	print ("Received POST")
	print(request.form)
	name = request.form["name"]
	city = request.form["city"]
	lang = request.form["lang"]
	text = request.form["textBox"]
	return render_template('/result.html', passn= name, passl= lang, passc =city, passt=text)

@app.route("/danger/")
def danger():
	print("*********\n"* 80)
	print("a user tried to visit /danger.  we have redirected the user to /")
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)

