import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# don't run anything past here while we troubleshoot
# streamlit.stop()




my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

####### streamlit.write('Thanks for adding ', add_my_fruit)
########### my_cur.execute("insert into from FRUIT_LOAD_LIST values ('from streamlit')")

# from urllib.error import URLError

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
#delete this line #streamlit.text(fruityvice_response.json()) # just writes the data to the screen


# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# wouput it the screen as a table
streamlit.dataframe(fruityvice_normalized)



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



