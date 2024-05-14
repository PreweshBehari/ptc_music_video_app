# Import packages
from flask import Flask, render_template

# Import custom packages
from my_api.music_video import get_api_data

# Initialise app
my_app = Flask(__name__)


@my_app.route("/home")
def index():
    # Get data from api
    data = get_api_data()

    return render_template("index.html", items=data)

# Run application
if __name__ == "__main__":
    my_app.run(debug=True)