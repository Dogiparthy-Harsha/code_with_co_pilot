from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
entries = []

@app.route('/')
def index():
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    content = request.form['content']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entries.append({'content': content, 'timestamp': timestamp})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)