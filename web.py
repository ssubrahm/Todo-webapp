import streamlit as st
import functions
from datetime import date

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + '\n'
    todos.append(todo_local)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


today = date.today().strftime("%B %d, %Y")
today_stamp = f'<p style="font-size:26px; color:yellow;">{today} </p>'
st.write(today_stamp, unsafe_allow_html=True)

st.title("My Todo WebApp")
st.subheader("A tool to increase my Productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Please enter a todo",
              on_change=add_todo, key="new_todo")
