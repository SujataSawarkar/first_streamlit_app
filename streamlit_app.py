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
   fruit_choice = streamlit.'kiwi'('What fruit would you like information about?')
   if not fruit choice:
       streamlit.error("Please select a fruit to get information")
   else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
except URLError as e :
  streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit load list contains:")


streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like add?','jackfruit')
streamlit.write('Thank you for adding ', fruit_choice)
# this will not work properly just go with it 
my_cur.execute("insert into fruit_load_list values('from streamlit')")


