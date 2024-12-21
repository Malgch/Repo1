from flask import Flask, render_template, request, jsonify
from calculator import get_exchange_rate
 
app = Flask(__name__)
 
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name
 
 
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
 
@app.route('/convert', methods=['POST'])
def convert():
    try:
        amount = float(request.form['amount'])
        currency_code = request.form['currency_code']
        rate = get_exchange_rate(currency_code)
        if rate is not None:
            converted_amount = amount * rate
            return jsonify({"converted_amount": round(converted_amount, 2)})
        else:
            return jsonify({"error": "Failed to fetch"}), 500
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)