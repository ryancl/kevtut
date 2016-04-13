from flask import Flask,render_template
import datetime
kevtut = Flask(__name__)

today = datetime.date.today()

@kevtut.route('/')
def index():
    return render_template('index.html', date=today)

if __name__ == '__main__':
    kevtut.run(debug=True)