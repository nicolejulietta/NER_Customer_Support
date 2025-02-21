from flask import Flask, render_template, request, jsonify
import spacy

app = Flask(__name__)

nlp = spacy.load("trained_ner_model")

@app.route("/", methods=["GET", "POST"])
def index():
    processed_text = ""
    if request.method == "POST":
        text_input = request.form.get("text_input")
        entities = request.form.getlist("entity")

        doc = nlp(text_input)
        processed_text = text_input 

        for ent in doc.ents:
            if ent.label_ in entities:
                processed_text = processed_text.replace(
                    ent.text, f'<span class="highlight">{ent.text}</span>'
                )

    return render_template("index.html", processed_text=processed_text)

@app.route("/process-text", methods=["POST"])
def process_text():
    data = request.get_json()
    text_input = data.get("text_input")
    
    doc = nlp(text_input)
    
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    
    return jsonify(entities)

if __name__ == "__main__":
    app.run(debug=True)
