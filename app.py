from flask import Flask, render_template, request, jsonify
import spacy

app = Flask(__name__)

# Load the custom-trained NER model (ensure the "trained_ner_model" folder exists)
nlp = spacy.load("trained_ner_model")

@app.route("/", methods=["GET", "POST"])
def index():
    processed_text = ""
    entities = []            # List of recognized entities as (text, label)
    selected_categories = [] # Categories selected via checkboxes
    if request.method == "POST":
        processed_text = request.form.get("text_input", "")
        # Get the list of selected entity categories
        selected_categories = request.form.getlist("entity")
        if processed_text:
            doc = nlp(processed_text)
            # If checkboxes are selected, filter entities; otherwise return all
            if selected_categories:
                entities = [
                    (ent.text, ent.label_) for ent in doc.ents if ent.label_ in selected_categories
                ]
            else:
                entities = [(ent.text, ent.label_) for ent in doc.ents]
    return render_template("index.html", processed_text=processed_text, entities=entities, selected_categories=selected_categories)

@app.route("/process-text", methods=["POST"])
def process_text():
    data = request.get_json()
    text_input = data.get("text_input")
    doc = nlp(text_input)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return jsonify(entities)

if __name__ == "__main__":
    app.run(debug=True)

