import streamlit as st
import WAFunctions

task_list = WAFunctions.get_task_list()
def add_task():
    new_task = st.session_state["New Task"] + "\n"
    task_list.append(new_task)
    WAFunctions.write_task_list(task_list)

st.title("My To-Do List")
st.subheader("You Got This!")

for index, task in enumerate(task_list):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        task_list.pop(index)
        WAFunctions.write_task_list(task_list)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label="Enter a Task", placeholder="Enter a Task.....",
              on_change=add_task, key="New Task")
