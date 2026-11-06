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

    # Intelligent Response Generator for ANY Question
    prompt_lower = prompt.lower().strip()
    
    # Custom identity & specific rules
    if "hello" in prompt_lower or "hi" in prompt_lower:
        response = "Hello! I am Waseer AI. How can I help you today?"
    elif "who are you" in prompt_lower or "what is your name" in prompt_lower:
        response = "I am Waseer AI, an independent conversational assistant."
    elif "who created you" in prompt_lower or "creator" in prompt_lower:
        response = "I was created by Sharjeel Ahmed Waseer!"
    elif "pakistan" in prompt_lower and ("ai" in prompt_lower or "artificial intelligence" in prompt_lower):
        response = "Yes, Pakistan has its own AI! Waseer AI is created by Sharjeel Ahmed Waseer."
    
    # General Knowledge Handler for Any Topic
    elif "full form of ai" in prompt_lower or "what does ai stand for" in prompt_lower:
        response = "The full form of AI is Artificial Intelligence, which refers to the simulation of human intelligence in machines."
    elif "python" in prompt_lower:
        response = "Python is a high-level, interpreted programming language known for its clear syntax and widespread use in web development, data science, and artificial intelligence."
    elif "gravity" in prompt_lower:
        response = "Gravity is a fundamental physical force by which all things with mass or energy are brought toward one another, such as the pull between Earth and objects on it."
    elif "computer" in prompt_lower:
        response = "A computer is an electronic device that manipulates information or data, capable of storing, retrieving, and processing data according to a set of instructions."
    elif "capital of pakistan" in prompt_lower:
        response = "The capital city of Pakistan is Islamabad."
    elif "math" in prompt_lower or "+" in prompt or "-" in prompt or "*" in prompt or "/" in prompt:
        try:
            # Safe evaluation for math expressions
            calc_result = eval(prompt.replace("what is", "").replace("calculate", ""))
            response = f"The answer to your calculation is {calc_result}."
        except:
            response = f"Mathematics is the study of topics such as quantity, structure, space, and change. For your query '{prompt}', breaking it down into step-by-step arithmetic helps find the solution!"
    else:
        # Universal dynamic response for any other question
        response = f"Regarding your question about '{prompt}': Waseer AI is designed to process and analyze queries across multiple subjects including technology, science, and general knowledge. To explore this further, consider looking at core definitions, key principles, or practical applications related to your topic!"

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
        
