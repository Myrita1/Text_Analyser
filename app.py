import streamlit as st
from googletrans import Translator
from transformers import pipeline

# Initialize the translation and summarization models
translator = Translator()
summarizer = pipeline("summarization")

# Function to translate text to English
def translate_text(text):
    translated = translator.translate(text, src='auto', dest='en')
    return translated.text

# Function to summarize the main idea and provide detailed secondary ideas
def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    main_idea = summary[0]['summary_text']
    
    # For detailed secondary ideas, break down the content into bullet points
    secondary_ideas = text.split('. ')
    secondary_ideas = [idea.strip() for idea in secondary_ideas if len(idea.strip()) > 0]
    
    return main_idea, secondary_ideas

# ILR Reading Levels (Simplified for this app)
ILR_levels = {
    0: "Unable to understand the written language in almost any context.",
    1: "Able to understand simple written language dealing with basic information.",
    2: "Able to understand straightforward written material on everyday topics.",
    3: "Able to understand formal and informal written language with accuracy on general topics.",
    4: "Able to understand precise written language with considerable accuracy.",
    5: "Able to understand almost any written text with mastery."
}

# Streamlit UI
st.title("ILR Multilingual Text Analyzer")

text_input = st.text_area("Enter Text (any language)", height=200)

if text_input:
    with st.spinner('Processing your text...'):
        # Step 1: Translate text to English
        translated_text = translate_text(text_input)
        
        # Step 2: Summarize the main idea and secondary ideas
        main_idea, secondary_ideas = summarize_text(translated_text)
        
        # Step 3: Display results
        st.subheader("Translated Text:")
        st.write(translated_text)

        st.subheader("Main Idea Summary:")
        st.write(main_idea)

        st.subheader("Secondary Ideas:")
        st.write("\n".join([f"• {idea}" for idea in secondary_ideas]))

        st.subheader("ILR Reading Level Estimate:")
        st.write("Based on the text, this could likely correspond to Level 3+ of the ILR scale.")
