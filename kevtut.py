from flask import Flask,render_template
kevtut = Flask(__name__)

@kevtut.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    kevtut.run(debug=True)