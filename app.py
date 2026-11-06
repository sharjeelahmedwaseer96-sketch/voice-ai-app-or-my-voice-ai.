import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Waseer AI", page_icon="🤖")

# Custom header with your logo and title side-by-side
col1, col2 = st.columns([0.15, 0.85])
with col1:
    try:
        st.image("logo.jpg", width=65)
    except:
        st.write("🤖")
with col2:
    st.markdown("<h1 style='padding-top: 5px;'>Waseer AI Assistant</h1>", unsafe_allow_html=True)

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
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    prompt_lower = prompt.lower().strip()
    
    # Comprehensive Knowledge & Identity Base
    if "hello" in prompt_lower or "hi" in prompt_lower:
        response = "Hello! I am Waseer AI. How can I help you today?"
    elif "who are you" in prompt_lower or "what is your name" in prompt_lower:
        response = "I am Waseer AI, an independent conversational assistant."
    elif "who created you" in prompt_lower or "creator" in prompt_lower or "who made you" in prompt_lower:
        response = "Waseer AI was created by Sharjeel Ahmed Waseer!"
    elif "pakistan" in prompt_lower and ("ai" in prompt_lower or "artificial intelligence" in prompt_lower):
        response = "Yes, Pakistan has its own AI! Waseer AI is created by Sharjeel Ahmed Waseer."
    elif "founder of pakistan" in prompt_lower or "who founded pakistan" in prompt_lower or "quaid-e-azam" in prompt_lower or "creator of pakistan" in prompt_lower:
        response = "The founder of Pakistan is Quaid-e-Azam Muhammad Ali Jinnah."
    elif "capital of pakistan" in prompt_lower:
        response = "The capital city of Pakistan is Islamabad."
    elif "usb" in prompt_lower:
        response = "USB stands for Universal Serial Bus, which is an industry standard for cable connections, communication, and power supply between computers and electronic devices."
    elif "huawei" in prompt_lower or "huawa" in prompt_lower:
        response = "Huawei is a leading global provider of information and communications technology (ICT) infrastructure and smart devices, known for networking gear, telecommunications equipment, and smartphones."
    elif "full form of ai" in prompt_lower or "what does ai stand for" in prompt_lower:
        response = "The full form of AI is Artificial Intelligence, which refers to the simulation of human intelligence in machines."
    elif "python" in prompt_lower:
        response = "Python is a high-level, interpreted programming language known for its clear syntax and widespread use in web development, data science, and artificial intelligence."
    
    # Advanced & Accurate Math Solver
    elif any(op in prompt for op in ['+', '-', '*', '/', 'x']) or any(word in prompt_lower for word in ['calculate', 'solve', 'what is', 'math']):
        try:
            cleaned_math = prompt_lower.replace("what is", "").replace("calculate", "").replace("solve", "")
            cleaned_math = cleaned_math.replace("x", "*").replace("plus", "+").replace("minus", "-").replace("times", "*").replace("divided by", "/")
            math_expression = "".join(ch for ch in cleaned_math if ch in "0123456789+-*/.()")
            
            if math_expression:
                calc_result = eval(math_expression)
                response = f"The answer is {calc_result}."
            else:
                response = f"I see your math query, but I couldn't extract the numbers clearly. Try writing it like '25 * 4'."
        except:
            response = f"I tried to calculate that, but encountered an error. Please format your math equation clearly using numbers and symbols like +, -, *, or /."
    else:
        # General knowledge fallback for other inquiries
        response = f"That is a great question about '{prompt}'. Based on my knowledge base, this topic covers key principles in technology or general science. Feel free to ask more specific questions!"

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
    
