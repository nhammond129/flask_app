import flask

app = flask.Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/index.html")
def hello_world():
    return flask.render_template("index.html")

if __name__ == "__main__":
    app.run()