from flask import Flask, render_template


#create a Flask instance
app = Flask(__name__)

@app.route('/')  # app routes to various html pages that we have assigned it to
def home():
    return render_template("test2.html")


@app.route('/eventpage/')
def eventpage():
    return render_template("eventpage.html")


if __name__ == "__main__":
#runs the application on the repl development server
    app.run(debug=True, port='5002')
    app.run(debug=True, port="5001", host="127.0.0.1")


