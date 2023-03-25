from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_regex', methods=['POST'])
def check_regex():
    regex = request.form['regex']
    text = request.form['text']
    if re.search(regex, text):
        result = "matches"
    else:
        result = "does not match"
    return render_template('result.html', regex=regex, text=text, result=result)

if __name__ == '__main__':
    app.run(debug=True)
