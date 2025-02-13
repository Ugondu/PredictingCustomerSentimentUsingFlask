import streamlit as st
import requests

def get_sentiment(text):
    url = "http://127.0.0.1:5003/analyze"
    payload = {'text':text}
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        
# Writing Streamlit function

def main():
    st.title("Customer review sentiment analyser using SVC model")
    user_text = st.text_input("Kindly enter your opinion here: ")
    if st.button ("OKAY"):
        if user_text:
            sentiment = get_sentiment(user_text)
        if sentiment:
            st.write(f"Sentiment: {sentiment['sentiment']}")
        else:
            st.warning("Do you mind inputting a text, please.")

if __name__ == "__main__":
    main()
        