from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

app = Flask(__name__)


# Define the route for the API
@app.route("/", methods=["GET"])
def index():
    try:
        # Get the user input from the query parameter in the URL
        user_input = request.args.get("query")

        # Load the tokenizer and model for named entity recognition (NER)
        tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
        model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

        # Create a pipeline for NER using the loaded tokenizer and model
        nlp = pipeline("ner", model=model, tokenizer=tokenizer)

        # Perform NER on the user input
        ner_results = {"input": user_input, "output": nlp(user_input)}

        # Return the NER results as JSON
        return jsonify(str(ner_results))

    except Exception as e:
        # Return an error message if an exception occurs during NER processing
        return jsonify({"error": "An error occurred: {}".format(str(e))})


if __name__ == "__main__":
    # Run the Flask app on localhost:5000
    app.run(debug=True)
