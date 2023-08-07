import streamlit

import pandas

import requests

import snowflake.connector

from urllib.error import URLError
streamlit.title("this is my own file")
streamlit.title("this is my new car and the car is imaginary"
               "this is the reason why i love you")
streamlit.header("very good idea")
streamlit.text("i can do my work properly")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])


streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error("Please select a fruit to get information")
   else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
except URLError as e :
  streamlit.stop()


streamlit.header("The Fruit load list contains:")
#snowflake related function
def fruit_load_list():
  with my_cnx.cursor as my_cur:
       my_cur.execute("selct * from fruit_load_list")
       return  my_cur.fetchall()
#add button to load fruit list
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

# allow the end user to add fruit
def insert_row_Snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
       my_cur.execute("insert into fruit_load_list values('from stramlit')")
       return "thanks for adding" + new_fruit    

add_my_fruit = streamlit.text_input('What fruit would you like add?')
if stramlit.button('Add a Fruit to the list'):
   
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    Back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(Back_from_function)


