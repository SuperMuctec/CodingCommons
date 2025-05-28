from flask import *
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    cards = [
        {
            "title": "Community Building",
            "description": "Keep it friendly and accessible for everyone",
            "tags": [
                { "label": "SFW", "bg": "bg-green-100", "text": "text-red-700" },
                { "label": "Friends", "bg": "bg-blue-100", "text": "text-yellow-700" },
            ],
        },
        {
            "title": "Interaction",
            "description": "Providing a platform for people to meet new people and make new friends.",
            "tags": [
                { "label": "Community", "bg": "bg-blue-100", "text": "text-blue-700" },
                { "label": "Socializing", "bg": "bg-cyan-100", "text": "text-fuchsia-700" },
                { "label": "Talking", "bg": "bg-fuchsia-100", "text": "text-fuchsia-700" },
            ],
        }
    ]
    current_year = datetime.now().year
    return render_template("Home.html", current_year=current_year, cards=cards)


app.run(debug=True)