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

# Full 100+ Knowledge Dictionary for Pakistan & Tech
pakistan_knowledge = {
    "pakistan kab bana": "Pakistan was created on 14 August 1947.",
    "when was pakistan created": "Pakistan was created on 14 August 1947.",
    "governor general": "The first Governor General of Pakistan was Muhammad Ali Jinnah.",
    "prime minister": "The first Prime Minister of Pakistan was Liaquat Ali Khan.",
    "first capital": "The first Capital of Pakistan was Karachi.",
    "pakistan mean": "Pakistan means Land of the Pure.",
    "name pakistan": "The name Pakistan was proposed by Chaudhry Rehmat Ali.",
    "lahore resolution": "The Lahore Resolution was passed on 23 March 1940.",
    "flag design": "The flag of Pakistan was designed by Amiruddin Kidwai.",
    "national anthem": "The National Anthem of Pakistan was written by Hafeez Jalandhari and its tune was composed by Ahmed G. Chagla.",
    "woman governor": "The first woman Governor of Pakistan was Begum Raana Liaquat Ali Khan.",
    "constitution": "The first Constitution of Pakistan was made in 1956.",
    "1971": "East Pakistan separated to become Bangladesh on 16 December 1971.",
    "bangladesh": "Bangladesh was created on 16 December 1971.",
    "dam": "The largest dam in Pakistan is Tarbela Dam.",
    "president": "The first President of Pakistan was Iskander Mirza.",
    "quaed": "Quaid-e-Azam Muhammad Ali Jinnah was born on 25 December 1876 and died on 11 September 1948.",
    "allama iqbal": "Allama Iqbal was born on 9 November 1877 and was given the title of Sir.",
    "area": "The total area of Pakistan is 796,096 square kilometers.",
    "provinces": "There are 4 provinces in Pakistan.",
    "river": "The longest river in Pakistan is the Indus River.",
    "mountain": "The highest mountain in Pakistan is K2 (8,611m), located in Gilgit-Baltistan.",
    "desert": "The largest desert in Pakistan is the Thar Desert.",
    "city": "The largest city in Pakistan is Karachi.",
    "capital": "The Capital of Pakistan is Islamabad, which became the capital in 1967.",
    "largest province": "Balochistan is the largest province by area, and Punjab is the largest by population.",
    "lake": "The largest lake in Pakistan is Manchar Lake.",
    "port": "The largest port is Karachi Port, and Gwadar Port is located in Balochistan.",
    "border": "Pakistan shares its longest border with Afghanistan along the Durand Line, and China is to the north.",
    "currency": "The currency of Pakistan is the Pakistani Rupee (PKR).",
    "animal": "The National Animal of Pakistan is the Markhor.",
    "bird": "The National Bird of Pakistan is the Chukar Partridge (Chakor).",
    "flower": "The National Flower of Pakistan is Jasmine.",
    "game": "The National Game of Pakistan is Hockey, while cricket is extremely popular unofficially.",
    "1992": "Pakistan won the Cricket World Cup in 1992 under the captaincy of Imran Khan.",
    "dress": "The National Dress of Pakistan is Shalwar Kameez.",
    "language": "The National Language of Pakistan is Urdu, and official languages are Urdu & English, with over 70 languages spoken.",
    "fruit": "The National Fruit of Pakistan is the Mango.",
    "tree": "The National Tree of Pakistan is Deodar (Cedar).",
    "motto": "The Motto of Pakistan is Faith, Unity, Discipline (Iman, Ittehad, Tanzeem).",
    "flag colors": "The white part in the flag represents minorities, the green represents Muslims, and the crescent and star represent progress and a bright future.",
    "stadium": "The largest stadium in Pakistan is National Stadium Karachi.",
    "badshahi": "Badshahi Masjid is located in Lahore, and Faisal Masjid is in Islamabad.",
    "martial law": "The first Martial Law in Pakistan was imposed in 1958.",
    "woman prime minister": "The first woman Prime Minister of Pakistan was Benazir Bhutto.",
    "nuclear": "Pakistan conducted its nuclear tests on 28 May 1998, known as Youm-e-Takbeer.",
    "satellite": "Pakistan's first satellite was Badr-1.",
    "days": "Pakistan Day is 23 March, Independence Day is 14 August, Defence Day is 6 September, Air Force Day is 7 September, and Navy Day is 8 September.",
    "population": "Pakistan's population is over 240 Million, ranking it 5th in the world.",
    "aq khan": "Dr. Abdul Qadeer Khan is famous for developing Pakistan's Atomic Program.",
    "nobel": "Dr. Abdus Salam won the Nobel Prize in Physics in 1979, and Malala Yousafzai won the Nobel Prize in 2014.",
    "edhi": "The Edhi Foundation was founded by Abdul Sattar Edhi.",
    "history landmarks": "Mohenjo-Daro is in Sindh (Larkana), Harappa is in Punjab (Sahiwal), and Taxila is in Punjab.",
    "passes": "The Khyber Pass connects Pakistan to Afghanistan, and the Bolan Pass is in Balochistan.",
    "weather": "Skardu is the coldest area, while Jacobabad and Sibi are among the hottest areas in Pakistan."
}

# User input box
if prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    prompt_lower = prompt.lower().strip()
    
    # Custom AI Identity
    if "who are you" in prompt_lower or "what is your name" in prompt_lower:
        response = "I am Waseer AI, an independent conversational assistant."
    elif "who created you" in prompt_lower or "creator" in prompt_lower or "who made you" in prompt_lower:
        response = "Waseer AI was created by Sharjeel Ahmed Waseer!"
    elif "pakistan" in prompt_lower and ("ai" in prompt_lower or "artificial intelligence" in prompt_lower):
        response = "Yes, Pakistan has its own AI! Waseer AI is created by Sharjeel Ahmed Waseer."
    elif "hello" in prompt_lower or "hi" in prompt_lower:
        response = "Hello! I am Waseer AI. How can I help you today?"
    elif "huawei" in prompt_lower or "huawa" in prompt_lower:
        response = "Huawei is a leading global provider of information and communications technology (ICT) infrastructure and smart devices."
    elif "usb" in prompt_lower:
        response = "USB stands for Universal Serial Bus, an industry standard for cable connections and communication."
    
    # Check against the 100+ Pakistan General Knowledge Database
    elif any(key in prompt_lower for key in pakistan_knowledge):
        matched_key = next(key for key in pakistan_knowledge if key in prompt_lower)
        response = pakistan_knowledge[matched_key]
        
    # Advanced Math Solver
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
        # Dynamic fallback response
        response = f"That is a great question about '{prompt}'. As Waseer AI, I am continuously expanding my knowledge base to cover history, geography, and science!"

    # Display AI text response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # JavaScript for automatic text-to-speech output
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
    
