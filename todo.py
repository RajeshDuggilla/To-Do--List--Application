import streamlit as st
import csv
import os

CSV_FILE = "tasks.csv"

def load_tasks():
    """Load tasks from the CSV file."""
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, "r") as f:
        return [row[0] for row in csv.reader(f)]

def save_tasks(task_list):
    """Save tasks to the CSV file."""
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([[task] for task in task_list])

def display_tasks(task_list):
    """Display tasks in the UI."""
    if not task_list:
        st.info("No tasks added yet.")
    else:
        st.subheader("Current Tasks")
        for i, task in enumerate(task_list, 1):
            st.write(f"{i}. {task}")

def set_background():
    """Apply custom background image."""
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg");
            background-attachment: fixed;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    st.set_page_config(page_title="To-Do List", layout="centered")
    set_background()
    st.title("📝 To-Do List")

    tasks = load_tasks()

    # Add task
    with st.form("add_task_form", clear_on_submit=True):
        task = st.text_input("Add a new task:")
        submitted = st.form_submit_button("Add Task")
        if submitted and task:
            tasks.append(task)
            save_tasks(tasks)
            st.success("Task added!")

    # Clear tasks
    if st.button("🗑️ Clear All Tasks"):
        tasks.clear()
        save_tasks(tasks)
        st.warning("All tasks cleared!")

    display_tasks(tasks)

if __name__ == "__main__":
    main()
