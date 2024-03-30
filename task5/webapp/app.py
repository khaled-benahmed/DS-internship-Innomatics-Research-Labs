# app.py

from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex']
        matches = re.findall(regex_pattern, test_string)
        return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)
    return render_template('index.html', matches=None)

# Bonus: Email validation route
@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    email_validated = False
    is_valid = False
    if request.method == 'POST':
        email = request.form['email']
        # Basic regex pattern for validating an email address
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        is_valid = re.match(regex, email) is not None
        email_validated = True
    return render_template('index.html', email_validated=email_validated, is_valid=is_valid)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
