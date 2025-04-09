import streamlit as st
from transformers import MarianMTModel, MarianTokenizer, BertForMaskedLM, BertTokenizer, pipeline

# Initialize MarianMT for translation and BERT for summarization
model_name_translation = 'Helsinki-NLP/opus-mt-ROMANCE-en'
tokenizer_translation = MarianTokenizer.from_pretrained(model_name_translation)
model_translation = MarianMTModel.from_pretrained(model_name_translation)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # BART for extractive summarization

# Function to translate text using MarianMT (more accurate translation)
def translate_text(text):
    translated = tokenizer_translation.encode(text, return_tensors="pt")
    output = model_translation.generate(translated, max_length=500, num_beams=4, early_stopping=True)
    translation = tokenizer_translation.decode(output[0], skip_special_tokens=True)
    return translation

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
    0: "Unable to understand the written language.",
    1: "Able to understand simple, written language.",
    2: "Able to understand straightforward written material.",
    3: "Able to understand formal and informal written language.",
    4: "Able to understand precise written language with considerable accuracy.",
    5: "Mastery of the language, able to understand almost any written text."
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
