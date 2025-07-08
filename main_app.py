'''# main_app.py
import streamlit as st
from crop_recommendation.crop_recommend import recommend_crop
from crop_disease_detection.predict_disease import predict_disease
from weather_forecasting.weather_api import get_weather

st.title("🌾 Crop Monitoring Dashboard")

st.sidebar.title("Features")
feature = st.sidebar.selectbox("Choose Feature", ["Crop Recommendation", "Crop Disease Detection", "Weather Forecasting"])

if feature == "Crop Recommendation":
    st.subheader("🧪 Enter Soil Parameters")
    n = st.number_input("Nitrogen")
    p = st.number_input("Phosphorus")
    k = st.number_input("Potassium")
    temp = st.number_input("Temperature (°C)")
    humidity = st.number_input("Humidity (%)")
    ph = st.number_input("Soil pH")
    rainfall = st.number_input("Rainfall (mm)")

    if st.button("Recommend Crop"):
        crop = recommend_crop([n, p, k, temp, humidity, ph, rainfall])
        st.success(f"✅ Recommended Crop: **{crop}**")

elif feature == "Crop Disease Detection":
    st.subheader("📷 Upload Leaf Image")
    uploaded = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    if uploaded:
        st.image(uploaded, use_column_width=True)
        with open("temp.jpg", "wb") as f:
            f.write(uploaded.read())
        disease = predict_disease("temp.jpg")
        st.success(f"🔍 Predicted Disease Label: **{disease}**")

elif feature == "Weather Forecasting":
    st.subheader("🌦️ Enter Location")
    city = st.text_input("City Name")
    api_key = st.secrets["openweather_api_key"]  # Add this to .streamlit/secrets.toml
    if st.button("Get Weather"):
        weather = get_weather(city, api_key)
        st.json(weather)
'''
import sys
import os

from chatbot.chatbot import generate_response
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# main_app.py
import streamlit as st

from crop_recommendation.crop_recommend import recommend_crop
from crop_disease_detection.predict_disease import predict_disease
from weather_forecasting.weather_api import get_weather
# Background image and text color
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/previews/032/514/918/non_2x/illustration-of-crop-monitoring-via-smart-device-vector.jpg");
        background-attachment: fixed;
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        color: black !important;
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 1rem;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.7);
    }

    section[data-testid="stSidebar"] .css-1cpxqw2 {
        color: white !important;
        font-weight: 700;
    }

    section[data-testid="stSidebar"] .css-16huue1 {
        color: white !important;
    }

    section[data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 600;
    }

    h1, h2, h3, h4, h5, h6, label, p {
        color: black !important;
    }

    /* ✅ BUTTON STYLING */
    div.stButton > button {
        color: white !important;
        background-color: #2e8b57 !important;
        border: none;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1rem;
    }

    div.stButton > button:hover {
        background-color: #246b46 !important;
        color: #ffffff !important;
    }
    /* Style chat text for better look */
.markdown-text-container {
    background-color: rgba(255,255,255,0.85);
    padding: 0.75rem;
    border-radius: 8px;
    margin-bottom: 0.5rem;
}

    </style>
    """,
    unsafe_allow_html=True
)


st.set_page_config(page_title="Crop Monitoring Dashboard", page_icon="🌾", layout="wide")

st.markdown("<h1 style='text-align: center; color: green;'>🌾 Smart Crop Monitoring System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Empowering Farmers with AI - Crop Recommendation, Disease Detection & Weather Forecasting</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📌 Select a Feature")
feature = st.sidebar.radio("Choose Feature", ["🌱 Crop Recommendation", "🍂 Crop Disease Detection", "☁️ Weather Forecasting", "🤖 Chatbot"])

# Feature 1: Crop Recommendation
if feature == "🌱 Crop Recommendation":
     st.markdown("### 🧪 Enter Soil Parameters")

    st.markdown("""
        <style>
        label, .stNumberInput label {
            color: black !important;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        k = st.number_input("Potassium (K)", min_value=0.0, max_value=1000.0, value=0.0, step=1.0)
        p = st.number_input("Phosphorus (P)", min_value=0.0, max_value=1000.0, value=0.0, step=1.0)
    with col2:
        n = st.number_input("Nitrogen (N)", min_value=0.0, max_value=1000.0, value=0.0, step=1.0)
        temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0, step=0.5)
    with col3:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)
        ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=50.0, step=1.0)

    if st.button("🌿 Recommend Best Crop"):
        with st.spinner("Analyzing..."):
            crop = recommend_crop([n, p, k, temp, humidity, ph, rainfall])
        st.markdown(f"""
        <div style='background-color: rgba(0, 0, 0, 0.6); padding: 1rem; border-radius: 10px; color: white; font-size: 20px;'>
            ✅ <b>Recommended Crop:</b> {crop}
        </div>
        """, unsafe_allow_html=True)
# Feature 2: Crop Disease Detection
elif feature == "🍂 Crop Disease Detection":
    st.markdown("### 📷 Upload a Leaf Image")
    uploaded = st.file_uploader("Choose a leaf image (jpg/png/jpeg)", type=["jpg", "png", "jpeg"])
    if uploaded:
        st.image(uploaded, use_column_width=True, caption="Uploaded Leaf")
        with open("temp.jpg", "wb") as f:
            f.write(uploaded.read())
        with st.spinner("Detecting Disease..."):
            disease = predict_disease("temp.jpg")
        st.markdown(f"""
    <div style='background-color: rgba(0, 0, 0, 0.6); padding: 1rem; border-radius: 10px; color: white; font-size: 20px;'>
        🔍 <b>Predicted Disease:</b> {disease}
    </div>
""", unsafe_allow_html=True)


# Feature 3: Weather Forecasting
elif feature == "☁️ Weather Forecasting":
    st.markdown("### 🌦️ Enter City Name for Weather Info")
    city = st.text_input("City Name")
    
    # Check if API key is available
    if "openweather_api_key" not in st.secrets:
        st.error("❌ OpenWeather API key not configured. Please add your API key to Streamlit secrets.")
    else:
        api_key = st.secrets["openweather_api_key"]

        if st.button("📡 Get Weather Update"):
            if city.strip() == "":
                st.warning("Please enter a valid city name.")
            else:
                with st.spinner(f"Fetching weather data for {city}..."):
                    weather = get_weather(city, api_key)
                
                # Check if there's an error in the response
                if "error" in weather:
                    st.error(f"❌ {weather['error']}")
                elif weather:
                    temperature = weather.get("Temperature", "N/A")
                    humidity = weather.get("Humidity", "N/A")
                    condition = weather.get("Weather", "N/A").title()

                    st.markdown(f"""
                    <div style='background-color: rgba(0, 0, 0, 0.6); padding: 1rem; border-radius: 10px; color: white; font-size: 18px;'>
                        <b>📍 Weather Forecast</b><br><br>
                        🌡️ Temperature: {temperature} °C<br>
                        💧 Humidity: {humidity}%<br>
                        ☁️ Weather: {condition}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error("❌ Unable to retrieve weather data.")

# Inside the feature switch:
elif feature == "🤖 Chatbot":
    st.markdown("### 🤖 Smart Farming Assistant (Groq LLaMA 3)")

    from chatbot.chatbot import generate_response

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask your question here 👇", key="chat_input")

    if user_input:
        with st.spinner("Thinking..."):
            reply = generate_response(user_input)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", reply))

    # Display Chat
    for sender, message in reversed(st.session_state.chat_history):
        if sender == "You":
            st.markdown(f"🧑‍🌾 **You:** {message}")
        else:
            st.markdown(f"🤖 **Bot:** {message}")
