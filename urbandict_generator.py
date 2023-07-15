
import streamlit as st
import requests
import pandas as pd
from io import BytesIO
import base64

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

If you want to sort the DataFrame by the 'thumbs_up' column, you can use the sort_values() function provided by pandas. Here's how you can do this:

python

df1 = df1.sort_values('thumbs_up', ascending=False)

This will sort the DataFrame in descending order by the 'thumbs_up' column. If you want to sort in ascending order, you can set ascending=True.

Here is how your full Streamlit app would look with this change:

python

import streamlit as st
import requests
import pandas as pd
from io import BytesIO
import base64

def get_definition(term):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    headers = {
        "X-RapidAPI-Key": "your_api_key",
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }
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
                df1 = df1.sort_values('thumbs_up', ascending=False)  # Sort the DataFrame by 'thumbs_up'
                st.dataframe(df1)  # Use st.dataframe instead of st.write

                # Convert DataFrame to Excel and create a download button
                towrite = BytesIO()
                df1.to_excel(towrite, index=False, sheet_name='Sheet1')  # write to BytesIO buffer
                towrite.seek(0)  # reset pointer
                b64 = base64.b64encode(towrite.read()).decode()  # read buffer and convert to base64
                href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="your_filename.xlsx">Download Data</a>'
                st.markdown(href, unsafe_allow_html=True)
            else:
                st.write("No definition found.")
        else:
            st.write("Please enter a word.")

if __name__ == "__main__":
    app()
