from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/hello-view/<name>')
def load_view(name):
    data = {
        'name': name,
        'last_name': 'no lastname'
    }

    return render_template('hello.html', **data)

@app.route('/json')
def json_data():
    return {
        'health': 'passed',
        'rest': 'unknown'
    }

if __name__ == '__main__':
    app.run()
