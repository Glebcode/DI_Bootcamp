import flask

app = flask.Flask(__name__)

@app.route('/main')
def main_route():
	return flask.render_template("main_page.html")

@app.route("/blue") # this solution will work, but try to make generic which means to create just one template and each time pass to it the color
def blue_route():
	return flask.render_template("blue.html")

@app.route("/green")
def green_route():
	return flask.render_template("green.html")

@app.route("/yellow")
def yellow_route():
	return flask.render_template("yellow.html")

@app.route("/red")
def red_route():
	return flask.render_template("red.html")

app.run(port=8080, debug=True)
