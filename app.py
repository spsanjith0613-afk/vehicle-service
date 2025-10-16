from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    model = request.form['model']
    age = request.form['age']
    service_type = request.form['service_type']
    service_time = request.form['service_time']
    return render_template('result.html', model=model, age=age, service_type=service_type, service_time=service_time)

if __name__ == '__main__':
    app.run(debug=True)
