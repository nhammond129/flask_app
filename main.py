import flask

app = flask.Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/post")
def post():
	return flask.render_template("post.html")

@app.route("/request", methods=['POST'])
def request():
	name = flask.request.form['name']
	return flask.render_template("request.html", name=name)

if __name__ == "__main__":
    app.run()