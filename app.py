import subprocess
import streamlit as st

st.title("Welcome to the PDF Document Search Engine")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with open("docs/uploaded_file.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Upload and Process File"):
        st.write("Processing the uploaded file...")
        progress_bar = st.progress(0)
        result = subprocess.run(["python", "pdfload.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        progress_bar.progress(100)

        if result.returncode != 0:
            st.error(f"Error: {result.stderr}")
        else:
            st.success("File processing complete")

query = st.text_input("Enter your query here:")

if st.button("Search"):
    st.write("Searching the documents...")
    progress_bar = st.progress(0)
    result = subprocess.run(["python", "query.py", query], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    progress_bar.progress(100)

    if result.returncode != 0:
        st.error(f"Error: {result.stderr}")
    else:
        st.success("Search complete")
        st.write(result.stdout)
