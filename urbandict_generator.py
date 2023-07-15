
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
    st.set_page_config(layout="wide")
    
    # Custom CSS styles
    st.markdown(
        """
        <style>
        .title {
            color: #FF9900;
        }
        .header-row th {
            background-color: #333333;
            color: #FFFFFF;
        }
        .text-button {
            color: #FFFFFF;
            background-color: #FF9900;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Title with custom class
    st.markdown('<h1 class="title">Urban Dictionary Definition Generator</h1>', unsafe_allow_html=True)
    
    term = st.text_input("Enter a word to search its definition")
    if st.button('Search', key='search-button'):
        if term:
            data = get_definition(term)
            if 'list' in data:
                df = pd.DataFrame(data['list'])
                df1 = df[['word','definition','example','thumbs_up','thumbs_down']]
                df1 = df1.sort_values('thumbs_up', ascending=False)
                
                # Table with custom class
                st.dataframe(df1, 0)
                
                # Download button with custom class
                # st.markdown(href, unsafe_allow_html=True)
            else:
                st.write("No definition found.")
        else:
            st.write("Please enter a word.")

if __name__ == "__main__":
    app()
