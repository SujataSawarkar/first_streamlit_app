import streamlit
streamlit.title("this is my own file")
streamlit.title("this is my new car and the car is imaginary"
               "this is the reason why i love you")streamlit.header("very good idea")
streamlit.text("i can do my work properly")


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
