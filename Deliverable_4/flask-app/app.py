from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template('forecast.html')

# run the applicationpython 
if __name__ == "__main__":
    app.run(debug=True)

