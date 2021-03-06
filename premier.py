from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap
from flask import send_from_directory
from werkzeug.contrib.fixers import ProxyFix
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 
				   'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/')
def index():
	theAgent = request.headers.get('User-Agent')
	return render_template('index.html', theAgent=theAgent)

@app.route('/user/<name>')
def user(name):
	theAgent = request.headers.get('User-Agent')
	return render_template('user.html', name=name, theAgent=theAgent)

@app.route('/products/encodem')
def encodem():
	return render_template('base.html')

@app.route('/products/namebot')
def namebot():
	return render_template('base.html')

@app.route('/products')
def products():
	return render_template('base.html')

@app.route('/products/libraries')
def libraries():
        return render_template('libraries.html')

@app.route('/products/libraries/listreader')
def lib_listreader():
        return render_template('lib_listreader.html')

@app.route('/products/libraries/propertiesfoo')
def lib_propertiesfoo():
        return render_template('lib_propertiesfoo.html')

@app.route('/about')
def about():
        return render_template('about.html')

@app.route('/about/licenses')
def licenses():
        return render_template('abt_licenses.html')

if __name__ == '__main__':
#	app.run(debug=True,host="192.168.0.103", port=2184)
        app.run(debug=True)
