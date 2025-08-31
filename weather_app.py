#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Your full Streamlit app code goes here\nimport streamlit as st\nimport requests\nfrom datetime import datetime\n\ndef get_weather(city):\n    api_key = "bf056d41d700b0a5342f504b2209a89b" \n    url = "https://api.openweathermap.org/data/2.5/weather"\n    params = {"q": city, "appid": api_key, "units": "metric"}\n    response = requests.get(url, params=params)\n\n    if response.status_code == 200:\n        data = response.json()\n        sunrise = datetime.fromtimestamp(data[\'sys\'][\'sunrise\']).strftime(\'%H:%M:%S\')\n        sunset = datetime.fromtimestamp(data[\'sys\'][\'sunset\']).strftime(\'%H:%M:%S\')\n        report = (\n            f"📍 Weather in {city}\\n"\n            f"🌡 Temp: {data[\'main\'][\'temp\']}°C\\n"\n            f"☁ Condition: {data[\'weather\'][0][\'description\'].capitalize()}\\n"\n            f"💧 Humidity: {data[\'main\'][\'humidity\']}%\\n"\n            f"💨 Wind: {data[\'wind\'][\'speed\']} m/s\\n"\n            f"🔆 Sunrise: {sunrise}\\n"\n            f"🌇 Sunset: {sunset}\\n"\n        )\n        st.markdown(report)\n    else:\n        st.error("City not found.")\n\nst.title("🌦️ Weather App")\ncity = st.text_input("Enter city name")\nif city:\n    get_weather(city)\n')


# In[ ]:


'streamlit run weather_app.py'


# In[ ]:





