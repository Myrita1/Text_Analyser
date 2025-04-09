# ILR Multilingual Text Analyzer

This Streamlit app allows users to input text in any language, and the app will:
- Translate the text into English.
- Provide a main idea summary.
- List secondary ideas in bullet points.

The app estimates the **ILR reading level** of the input text based on the Interagency Language Roundtable (ILR) guidelines, ranging from Level 0+ (unable to understand) to Level 5 (mastery).

## Requirements

- Python 3.7 or higher
- Streamlit
- Googletrans for translation
- Hugging Face Transformers for summarization

## Setup Instructions

1. Clone or download the repository.
2. Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

3. To run the app locally, navigate to the project folder and run:

    ```bash
    streamlit run app.py
    ```

4. Open your browser and go to `http://localhost:8501` to use the app.

## How to Use

- Enter text in any language in the input box.
- Click the "Submit" button to process the text.
- The app will display the English translation, main idea summary, secondary ideas, and an estimated ILR level.

## ILR Reading Levels

- **Level 0**: Unable to understand the written language.
- **Level 1**: Understands basic, simple written language.
- **Level 2**: Understands straightforward written material.
- **Level 3**: Understands formal and informal written language.
- **Level 4**: Understands precise written language with accuracy.
- **Level 5**: Mastery of the language, able to understand almost any written text.
