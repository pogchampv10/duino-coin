from flask import Flask, redirect, render_template_string
from flaskwebgui import FlaskUI #get the FlaskUI class


app = Flask(__name__)

ui = FlaskUI(app)


@app.route("/")
def Home():
    return render_template_string("""<h1>Welcome</h1><hr><a href="https://explorer.duinocoin.com/">Duco Explorer</a>""")
    # return redirect("https://explorer.duinocoin.com/")


# call the 'run' method
ui.run()
