from flask import Flask,request,render_template
import main


from flask.helpers import url_for

from werkzeug.utils import redirect

app = Flask(__name__)

user = main.Users()


@app.route('/')
def home():
    return redirect(url_for("login"))
    
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        name = request.form['username']
        user.login(name)
        email = request.form['email']
        return redirect(url_for("main", usr=name))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def main(usr):
    user.ReadFromFile(usr)
    return render_template("main.html", username = usr)


if __name__ == '__main__':
    app.run()