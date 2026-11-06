import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Voice & Text AI", page_icon="🗣️")
st.title("🗣️ My Voice & Text AI Assistant")
st.write("Ask me anything! I will answer in both text and voice.")

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
        response = "Hello! How can I help you today?"
    elif "who are you" in prompt_lower:
        response = "I am your custom voice and text AI assistant!"
    elif "how are you" in prompt_lower:
        response = "I am doing great and ready to answer your questions!"
    else:
        response = f"You asked about '{prompt}'. I am your custom-built AI!"

    # Display AI text response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # JavaScript to make the browser speak the AI's response automatically out loud
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
  
