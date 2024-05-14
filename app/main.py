# Import packages
from flask import Flask, render_template, request

# Import custom packages
from my_api.music_video import get_api_data

# Initialise app
my_app = Flask(__name__)

# Decorator to define route for the app
@my_app.route("/home")
def index():
    # Get data from api
    data = get_api_data()

    # Filter data on given search query
    search_query = request.args.get("q", None)

    if search_query:
        data = filter(lambda d: search_query.lower() in d["name"].lower(), data)

    # Sort data by "score" column in descending order
    data = sorted(data,
                  key=lambda x: x["score"],
                  reverse=True)

    return render_template("index.html", items=data)

# Run application
if __name__ == "__main__":
    my_app.run(debug=True)