from flask import Flask, render_template

app = Flask(__name__)

posts =[
    {
        "title":"Oraine oota",
        "content":"webaale"
    },

  {
        "title":"Oraine oota",
        "content":"wasibota"
    }

]

@app.route('/')
def home():
    return render_template("home.html", posts=posts)