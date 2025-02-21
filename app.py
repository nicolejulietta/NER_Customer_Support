from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    processed_text = ""
    if request.method == "POST":
        text = request.form.get("text_input")
        if text:
            processed_text = text
    return render_template("index.html", processed_text=processed_text)

if __name__ == "__main__":
    app.run(debug=True)
