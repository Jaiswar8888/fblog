from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')

def index():
    first_name = "John"
    favorite_pizza = ["pepperroni","mashroom"]
    return render_template("index.html",first_name=first_name,favorite_pizza=favorite_pizza)

@app.route("/user/<name>")

def user(name):
    return render_template("user.html",user_name=name)


if __name__ == '__main__':
    app.run(debug=True)