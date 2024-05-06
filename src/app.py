from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trajetória')
def trajetória():
    return render_template('trajetória.html')

@app.route('/discografia')
def discografia():
    return render_template('discografia.html')

@app.route('/resenha')
def resenha():
    return render_template('resenha.html')

if __name__ == '__main__':
    app.run(debug=True)

    
