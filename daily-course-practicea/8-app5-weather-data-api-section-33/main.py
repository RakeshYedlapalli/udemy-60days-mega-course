from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]
# filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
# df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])

@app.route("/")
def home():
    return render_template("home.html", dynamicData=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperate = 20
    # df = pd.read_csv("data_small/TG_STAID000001.txt", skiprows=20)
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    print("Station name is ->", station)
    # print(df[10:20])
    # list1 = [{"rakes": "rakes", "dsaf": "fadfa"}]
    return {"station": station, "date": date, "temperature": temperature}


@app.route("/api/v1/word/<wordname>")
def words(wordname):
    temperate = 20
    data = [{"definition": "cushion placed under the head for sleeping", "word": "pillow"},
            {
                "definition": "a device that determines the presence and properties of a substance by measuring the light it absorbs or emits.",
                "word": "spectrophotometer"},
            {"definition": "a horse kept for breeding", "word": "stallion"}]

    found_object = find_word(data, wordname)

    if found_object:
        return found_object
    else:
        return "NO Object found with given name"


def find_word(data, word):
    for item in data:
        if item["word"] == word:
            return item
    return None


if __name__ == "__main__":
    app.run(debug=True, port=4001)
