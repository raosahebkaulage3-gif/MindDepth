import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="MindDepth",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 MindDepth")
st.write("Ask any question and explore it deeply with AI.")

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    st.error("OPENAI_API_KEY not found in Streamlit Secrets.")
    st.stop()

question = st.text_area(
    "Enter your question",
    height=150
)

depth = st.slider(
    "Depth",
    1,
    10,
    5
)

if st.button("Explore"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    prompt = f"""
You are an expert thinker.

Analyze this question deeply.

Question:
{question}

Return the answer in Markdown using these headings:

# Core Question

# Assumptions

# Hidden Beliefs

# Mental Barriers

# Five Why Analysis

# Alternative Perspective

# Final Conclusion

Depth: {depth}
"""

    with st.spinner("Thinking..."):

        response = client.responses.create(
            model="gpt-5",
            input=prompt
        )

    st.markdown(response.output_text)
यानंतर:
Commit changes कर.
Streamlit आपोआप पुन्हा Deploy होईल.
जर पुन्हा एरर आली तर नवीन स्क्रीनशॉट पाठव.
हा कोड आधीच्या 🌳 Syntax Error पेक्षा स्वच्छ आहे आणि त्या त्रुटी येणार नाहीत.
