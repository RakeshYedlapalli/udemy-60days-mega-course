from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperate = 20
    list1 = [{"rakes": "rakes", "dsaf": "fadfa"}]
    return {"station": station, "date": date, "temperature": temperate}


if __name__ == "__main__":
    app.run(debug=True)
