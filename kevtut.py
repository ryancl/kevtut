from flask import Flask,render_template
import datetime
import requests

kevtut = Flask(__name__)

# setting some variables
today = datetime.date.today()
url = 'http://saallergy.info/'
headers = {'Accept': 'application/json'}
r = requests.get(url, headers=headers)

@kevtut.route('/')
def index():
    return render_template('index.html', date=today, get=r.json())

if __name__ == '__main__':
    kevtut.run(debug=True)