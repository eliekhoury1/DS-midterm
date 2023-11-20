from flask import Flask, render_template
from flask import jsonify
import prob_calculator
from unittest import main

app = Flask(__name__)

# Your existing code for probability calculation
prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)

# Define a route for the web interface
@app.route('/')
def index():
    return render_template('index.html', probability=probability)

# Define an API endpoint for retrieving the probability
@app.route('/api/probability')
def get_probability():
    return jsonify({'probability': probability})

# Run unit tests automatically
main(module='test_module', exit=False)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
