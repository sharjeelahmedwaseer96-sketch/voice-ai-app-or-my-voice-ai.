import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Waseer AI", page_icon="🤖")
st.title("🤖 Waseer AI Assistant")
st.write("Hello! I am Waseer AI, your custom-built assistant. Ask me anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
if prompt := st.chat_input("Type your question here..."):
    # Add user message to state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response Logic
    prompt_lower = prompt.lower()
    if "hello" in prompt_lower or "hi" in prompt_lower:
        response = "Hello! I am Waseer AI. How can I help you today?"
    elif "who are you" in prompt_lower or "what is your name" in prompt_lower:
        response = "I am Waseer AI, an independent conversational assistant."
    elif "who created you" in prompt_lower or "creator" in prompt_lower:
        response = "I was created by Sharjeel Ahmed Waseer!"
    elif "pakistan" in prompt_lower and ("ai" in prompt_lower or "artificial intelligence" in prompt_lower):
        response = "Yes, Pakistan has its own AI! Waseer AI is created by Sharjeel Ahmed Waseer."
    elif "how are you" in prompt_lower:
        response = "I am operating at full capacity and ready to assist you!"
    else:
        response = f"You asked about '{prompt}'. As Waseer AI, I am here to help answer your questions!"

    # Display AI text response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # JavaScript to make the browser speak out loud automatically
    speech_code = f"""
    <script>
        function speakText() {{
            if ('speechSynthesis' in window) {{
                window.speechSynthesis.cancel();
                let utterance = new SpeechSynthesisUtterance({repr(response)});
                utterance.rate = 1.0;
                utterance.pitch = 1.0;
                window.speechSynthesis.speak(utterance);
            }}
        }}
        speakText();
    </script>
    """
    components.html(speech_code, height=0)
    
