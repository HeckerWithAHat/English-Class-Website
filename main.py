from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/author")
def author():
    return render_template("author.html")


@app.route("/character")
def character():
    return render_template("characters.html")


@app.route("/glossary")
def glossary():
    return render_template("glossary.html")


@app.route("/litlum")
def litlum():
    return render_template("litlum.html")

@app.route("/purpose")
def purpose():
    return render_template("purpose.html")

@app.route("/summary")
def summary():
    return render_template("summary.html")

@app.route("/research")
def research():
    return render_template("researcher.html")


@app.route("/file/<path:filename>")
def serve_file(filename):
    if (filename == "main.py"):
        return "Access Denied", 403
    return send_from_directory("static/", filename)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
