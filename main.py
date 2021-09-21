import flask
import backend
from threading import Thread

app = flask.Flask(__name__, template_folder='templates', static_folder='static', static_url_path='')

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

@app.route("/data")
def data():
    return flask.render_template("data.html")

@app.route('/data-sse-stream')
def chart_data():
    sub = backend.generator.subscribe()
    return flask.Response(sub.read(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(threaded=True)