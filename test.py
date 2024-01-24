from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template("home_test.html")


@app.route("/api/v2/<word>/")
def about(word):
    meaning = df.loc[df['word'] == word]['definition'].squeeze()
    result = {'word': word, 'definition': meaning}
    return meaning


if __name__ == "__main__":
    app.run(debug=True)
