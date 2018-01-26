import flask
from flask import request
app = flask.Flask(__name__)
@app.route("/")
def index():
	return "home page"
@app.route("/name")
def hello():
	name = request.args.get("name")
	if name == None:
		name = 'test'
	return flask.render_template('name.html', name=name)

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'),404

@app.errorhandler(403)
def page_not_found(error):
	return flask.render_template('403.html'),403	


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
