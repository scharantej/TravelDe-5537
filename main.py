
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for destinations
destinations = [
    {
        "name": "Berlin",
        "attractions": ["Brandenburg Gate", "Reichstag Building", "Museum Island"],
        "accommodation": ["The Ritz-Carlton, Berlin", "The Mandala Hotel", "Hotel de Rome"],
        "transportation": ["Berlin Brandenburg Airport", "Berlin Hauptbahnhof", "Berlin Südkreuz"]
    },
    {
        "name": "Munich",
        "attractions": ["Hofbräuhaus", "Deutsches Museum", "Englischer Garten"],
        "accommodation": ["The Bayerischer Hof", "The Mandarin Oriental, Munich", "The Hotel Vier Jahreszeiten Kempinski München"],
        "transportation": ["Munich Airport", "Munich Hauptbahnhof", "Munich Ostbahnhof"]
    },
    {
        "name": "Hamburg",
        "attractions": ["Miniatur Wunderland", "Elbphilharmonie", "Reeperbahn"],
        "accommodation": ["The Fontenay", "The Park Hyatt Hamburg", "The Hotel Atlantic Kempinski Hamburg"],
        "transportation": ["Hamburg Airport", "Hamburg Hauptbahnhof", "Hamburg Altona"]
    }
]

# Route to render index page
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle user input and redirect to destinations page
@app.route("/destinations", methods=["GET", "POST"])
def destinations():
    if request.method == "POST":
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        destination_preferences = request.form.getlist("destination_preferences")
        return redirect(url_for("destination_details", start_date=start_date, end_date=end_date, destination_preferences=destination_preferences))
    else:
        return render_template("index.html")

# Route to render destinations page
@app.route("/destinations/<start_date>/<end_date>/<destination_preferences>")
def destination_details(start_date, end_date, destination_preferences):
    filtered_destinations = [destination for destination in destinations if destination["name"] in destination_preferences]
    return render_template("destinations.html", start_date=start_date, end_date=end_date, destinations=filtered_destinations)

# Error route
@app.errorhandler(404)
def error(e):
    return render_template("error.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
