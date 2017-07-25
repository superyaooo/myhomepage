from flask import Flask, render_template
from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app)
DEBUG = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html')

@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')




if __name__ == '__main__':
    app.run()
