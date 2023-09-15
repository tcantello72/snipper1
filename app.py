"""
created by: Toby Cantello
Date created: 9/13/23
Last updated: 9/13/23
""" 

from flask import render_template
import config

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)