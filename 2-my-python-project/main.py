import streamlit as st
import functions as fu

todos = fu.readFile()


def add_todo():
    todo = st.session_state["new_todo"]
    print("This is New TODO", todo)
    todos.append(todo + "\n")
    fu.writeFile(todos)


st.title("My Todo App")
st.subheader("This is Header")
st.write("This app is to increase your productivity")

for index, to in enumerate(todos):
    checkbox = st.checkbox(to, key=to)
    if checkbox:
        print("Before: ", todos)
        todos.pop(index)
        fu.writeFile(todos)
        print("After: ", todos)
        del st.session_state[to]
        st.rerun()

st.text_input(label="", placeholder="Add new todo....", on_change=add_todo, key='new_todo')
st.session_state