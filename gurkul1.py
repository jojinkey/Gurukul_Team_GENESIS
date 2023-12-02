
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bajaj')
def bajaj():
    return render_template('bajaj.html')

@app.route('/toyota')
def FORTUNER():
    return render_template('toyota.html')

@app.route('/yamaha')
def yamaha():
    return render_template('yamaha.html')

@app.route('/wagon')
def wagon():
    return render_template('wagon.html')

@app.route('/bullet')
def bullet():
    return render_template('bullet.html')

if __name__ == '__main__':
    app.run(debug=True)
