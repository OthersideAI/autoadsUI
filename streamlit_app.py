import streamlit as st
import requests


# Title
st.title("AutoAds")

# Input
text = st.text_area("Enter market to tackle")

if st.button("Generate Ads and Keywords"):
    url = "https://flask-production-b223.up.railway.app/get_ads"
    payload={'market': text}

    response = requests.request("POST", url, data=payload)

    # break up the json response
    response_json = response.json()
    headlines = response_json["Headlines"]
    descriptions = response_json["Descriptions"]
    keywords = response.json["Keywords"]

    # display the translation and reasoning
    st.write('Headlines')
    st.write(headlines)
    st.write('Descriptions')
    st.write(descriptions)
    st.write('Keywords')
    st.write(keywords)
