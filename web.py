import streamlit as st
import functions
from datetime import date
import pandas as pd

FILE_PATH = "todos.txt"


def add_todo(person="Srinath"):
    """
    This function gets called when a new todo is added as a callback triggered by onchange
    Input: Person for whom a new todo needs to be added
    Output:  Displays teh new todo and adds it to the person's todo file
    """
    todos = functions.get_todos(filepath=person + '_' + FILE_PATH)
    todo_local = st.session_state["new_todo"] + '\n'
    todos.append(todo_local)
    functions.write_todos(todos, filepath=person + '_' + FILE_PATH)
    st.session_state["new_todo"] = ""


def person_todo(person="Srinath", filepath="Srinath_todos.txt"):
    """
    A function to display the todos list for the specific family member and teh ability to add or delete a todo
    Input: person as chosen by the radio button, filepath of the person's todofile
    output:  Display the current todos for the person and the option to add/delete a todo
    """
    todos = functions.get_todos(filepath=person + '_' + FILE_PATH)
    if todos:
        for index, todo in enumerate(todos):
            checkbox = st.checkbox(todo, key=todo)
            if checkbox:
                todos.pop(index)
                functions.write_todos(todos, filepath=person + '_' + FILE_PATH)
                del st.session_state[todo]
                st.experimental_rerun()

    st.text_input(label="", placeholder="Please enter a todo",
                  on_change=add_todo, args=[person], key="new_todo")


today = date.today().strftime("%B %d, %Y")
today_stamp = f'<p style="font-size:26px; color:yellow; text-align:center">{today} </p>'
st.write(today_stamp, unsafe_allow_html=True)

st.title("My Todo WebApp")
st.subheader("A tool to increase my Productivity")

# Set a radio button for the family reading from a file
# with open("family.csv", "r") as file:
#     choices = file.readlines()
#     choices = [choice.strip("\n") for choice in choices]
#     print(choices)

df = pd.read_csv("family.csv", sep=',')

person = st.radio('Choose the family member for Todo display', options=df['Name'],
                  # captions=[":orange[The Daughter@work]", ":blue[The Daddy@work]", ":violet[The Mommy@work]"],
                  captions=df['Caption'],
                  horizontal=True)

# Display todos based on the chosen person in the family
if person == "Srinath":
    person_todo(person, filepath=person + '_' + FILE_PATH)
elif person == "Ammu":
    person_todo(person, filepath=person + '_' + FILE_PATH)
elif person == "Roopa":
    person_todo(person, filepath=person + '_' + FILE_PATH)
elif person == "Guest":
    person_todo(person, filepath=person + '_' + FILE_PATH)
else:
    st.info("Not a valid person for Todos...")
