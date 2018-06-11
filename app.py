from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('h/index.html')

@app.route('/cosmos')
def home_cosmos():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/", "contributors.json")
    data = json.load(open(json_url))
    return render_template('h/cosmos.html', data=data)

@app.route('/quark')
def home_quark():
    return render_template('h/quark.html')

@app.route('/search')
def home_search():
    return render_template('h/search.html')

@app.route('/iq')
def home_iq():
    return render_template('h/iq.html')

@app.route('/discuss')
def home_discuss():
    return render_template('h/discuss.html')

@app.route('/logo')
def logo():
	return send_from_directory('static/files', 'logo.jpg')

if __name__ == '__main__':
	app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
