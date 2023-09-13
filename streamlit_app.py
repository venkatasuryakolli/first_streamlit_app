import streamlit

import pandas

# import requests

# import snowflake.connector

# from urllib.error import URLError

 
# def get_fruityvice_data(this_fruit_choice):

#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)

#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#     return fruityvice_normalized

 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
#streamlit.dataframe(fruits_to_show)

# my_fruit_list = my_fruit_list.set_index('Fruit')

 


streamlit.title('My parents New Heathly Diner')

 

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 and Blueberry oatmeal')

streamlit.text('🥗Kale, Spinach and Rocket Smoothie')

streamlit.text('🐔Hard-Boiled and Free-Range egg')

streamlit.text('🥑🍞Avocado Toast')

 

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

 


# fruits_to_show = my_fruit_list.loc[fruits_selected]

 

# streamlit.dataframe(fruits_to_show)

 ########################### /*

#streamlit.header("Fruityvice Fruit Advice!")

#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')

#streamlit.write('The user entered ', fruit_choice)

 

#bring in fruityvice:

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Now we normalize the json:

#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# And here we convert to dataframe:

#streamlit.dataframe(fruityvice_normalized)

 

#new section to display fruityvice api response:
############ */ 

