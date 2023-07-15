
import streamlit as st
import requests
import pandas as pd

def get_definition(term):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    #term = input("Please enter a term: ")
    #querystring = {"term": term}
  
    headers = {
	  "X-RapidAPI-Key": "7fd977a6b5msh913fd194d1d0ec3p162a93jsn6293361adae4",
	  "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }

    #response = requests.get(url, headers=headers, params=querystring)
    response = requests.get(url, headers=headers, params={"term": term})
    data = response.json()
    return data

def app():
    st.set_page_config(layout="wide")  # Use the full page instead of a narrow central column
    st.title("Urban Dictionary Definition Generator")
    term = st.text_input("Enter a word to search its definition")
    if st.button('Search'):
        if term:
            data = get_definition(term)
            if 'list' in data:
                df = pd.DataFrame(data['list'])
                df1 = df[['word','definition','example','thumbs_up','thumbs_down']]
                st.write(df1)
            else:
                st.write("No definition found.")
        else:
            st.write("Please enter a word.")

if __name__ == "__main__":
    app()
