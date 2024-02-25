# Named Entity Recognition (NER) API using Hugging Face Transformers and Flask

This Flask API provides a simple web service for performing Named Entity Recognition (NER) using pre-trained models from the Hugging Face Transformers library.


## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/ner-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ner-api
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the API using a web browser or an HTTP client like cURL or Postman.

   Example:

   - Open a web browser and visit `http://localhost:5000/?query=Your%20text%20here` replacing `Your%20text%20here` with the text you want to perform NER on.
   - Alternatively, you can use cURL:

      ```bash
      curl "http://localhost:5000/?query=Your%20text%20here"
      ```

## API Endpoint

- **GET /:**
  - Params:
    - query: The text to perform NER on.
  - Returns:
    - JSON response containing the input text and NER results.

## Model Details

This API uses the `dslim/bert-base-NER` model from Hugging Face's model hub for named entity recognition. You can replace it with any other model supported by the Transformers library.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

