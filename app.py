from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

# nlp = spacy.load("trained_ner_model")

@app.route("/", methods=["GET", "POST"])
def index():
    entities = []
    if request.method == "POST":
        text = request.form.get("text_input")
        if text:
            doc = nlp(text)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
    return render_template("index.html", entities=entities)

if __name__ == "__main__":
    app.run(debug=True)
