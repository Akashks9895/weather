import streamlit as st
import requests
API_KEY = "xxxxxxxxxxx"

def convert_to_celcius(temp_k):
    return temp_k-273.15




def find_current_weather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_data = requests.get(base_url).json()
    try:
        general =weather_data['weather'][0]['main']
        icon_id =weather_data['weather'][0]['icon']
        temperature =round(convert_to_celcius(weather_data['main']['temp']))
        icon = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("city not found")
        st.stop()   
    return general,temperature,icon     




def main():
    st.header("Find the weather")
    city= st.text_input("enter the city").lower()
    if st.button("Find"):
        general,temperature,icon =find_current_weather(city)
    st.write(general)
    st.metric(label="Temperature",value=f"{temperature}°C")
    st.image(icon)    


if __name__== '__main__':
    main()    