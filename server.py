from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    #document.body.contendEditable=true pozwala na edycje storny na żywo w przeglądarce(wpisać w konsoli chrome dev tools)
