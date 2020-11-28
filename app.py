from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('index.html')

@app.route('/about')
def render_about():
    return render_template('about.html')


app.run('0.0.0.0', 8000)