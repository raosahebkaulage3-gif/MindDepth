हो. खाली चालणारा app.py देतो. हा Streamlit + OpenAI Responses API वापरतो.
app.py
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="MindDepth", page_icon="🧠")

st.title("🧠 MindDepth")
st.caption("Explore any thought deeply")

api_key = st.secrets.get("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY not found in Streamlit secrets.")
    st.stop()

client = OpenAI(api_key=api_key)

question = st.text_area(
    "Enter your question",
    height=150,
    placeholder="Type any question..."
)

depth = st.slider("Depth", 1, 10, 5)

if st.button("Explore"):

    if not question.strip():
        st.warning("Enter a question.")
        st.stop()

    prompt = f"""
You are MindDepth AI.

Question:
{question}

Analyze deeply.

Return in Markdown with sections:

# Core Question

# Assumptions

# Hidden Beliefs

# Possible Mental Barriers

# 5 Why Chain

# Alternative Perspective

# Final Conclusion

Depth = {depth}
"""

    with st.spinner("Thinking..."):

        response = client.responses.create(
            model="gpt-5",
            input=prompt
        )

    st.markdown(response.output_text)
requirements.txt
streamlit
openai
.streamlit/secrets.toml
OPENAI_API_KEY="YOUR_API_KEY"
ही पहिली चालणारी आवृत्ती आहे. GitHub वर टाकून Streamlit Cloud वर deploy केल्यावर ती चालेल.
पुढची आवृत्ती आपण यात:
🌳 Thought Tree
❓ Infinite Why Engine
🧠 Belief Graph
📄 PDF Export
💾 History
🎙️ Voice Input
जोडू शकतो.
