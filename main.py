from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("Home.html")
@app.route("/about")
def about():    
    return  render_template("About.html")

@app.route("/signup")
def signup():
    return render_template("Signup.html")

@app.route("/login")
def login():
    return  render_template("Login.html")


if __name__ == "__main__":
     app.run(debug=True,host="0.0.0.0",port=5000)