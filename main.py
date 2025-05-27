from flask import *
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("Home.html", current_year=current_year)


app.run(debug=True)