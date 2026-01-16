from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        expression = data['expression']
        result = eval(expression)  # Use safer parser in production
        return jsonify({'result': result})
    except:
        return jsonify({'result': 'tum se na ho payega'})

if __name__ == '__main__':
    app.run(debug=True)
