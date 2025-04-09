import streamlit as st
from googletrans import Translator  # Google Translate API
from transformers import pipeline    # Hugging Face model pipeline
import spacy
import nltk
from nltk.tokenize import sent_tokenize

# Initialize spaCy for language processing (used for ILR level assessment)
nlp = spacy.load("en_core_web_sm")

# Initialize the Hugging Face summarization pipeline
summarizer = pipeline("summarization")

# Google Translate API
translator = Translator()

# Function to translate text into English
def translate_text(input_text, target_language='en'):
    """Translate text to the target language (default: English)."""
    translation = translator.translate(input_text, dest=target_language)
    return translation.text

# Function to summarize the main idea of the text
def summarize_text(input_text):
    """Summarize the main idea of the text."""
    summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Function to extract secondary ideas from the text
def extract_secondary_ideas(input_text):
    """Extract secondary ideas from the text."""
    sentences = sent_tokenize(input_text)
    ideas = sentences[:5]  # Limit to first 5 ideas for simplicity
    return ideas

# Function to assess ILR level based on the complexity of the text
def assess_ilr_level(text):
    """Assess ILR level based on the complexity of the text."""
    doc = nlp(text)
    
    # A basic rule-based approach to categorize the text length into ILR levels
    if len(doc) < 100:
        return 'Level 1: Basic comprehension'
    elif len(doc) < 200:
        return 'Level 2: Basic understanding of simple materials'
    elif len(doc) < 500:
        return 'Level 3: Adequate comprehension of general content'
    elif len(doc) < 800:
        return 'Level 4: Advanced comprehension of nuanced content'
    else:
        return 'Level 5: Mastery in understanding complex texts'

# Streamlit interface
st.title('ILR Multilingual Text Analyzer')

# Input text
text_input = st.text_area('Enter text for analysis', '')

if text_input:
    # Translate the text to English
    translated_text = translate_text(text_input)

    # Summarize the main idea
    main_idea = summarize_text(translated_text)

    # Extract secondary ideas
    secondary_ideas = extract_secondary_ideas(translated_text)

    # Assess the ILR level of the text
    ilr_level = assess_ilr_level(translated_text)

    # Display results
    st.subheader('Translated Text:')
    st.write(translated_text)

    st.subheader('Main Idea:')
    st.write(main_idea)

    st.subheader('Secondary Ideas:')
    for idea in secondary_ideas:
        st.write(f"- {idea}")

    st.subheader('ILR Level Assessment:')
    st.write(ilr_level)
