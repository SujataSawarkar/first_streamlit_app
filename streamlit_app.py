import streamlit
streamlit.title("this is my own file")
streamlit.title("this is my new car and the car is imaginary"
               "this is the reason why i love you")
streamlit.header("very good idea")
streamlit.text("i can do my work properly")


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
