# streamlit_app.py
import streamlit as st
import requests

API_BASE = "http://localhost:5000"

st.set_page_config(page_title="Multimodal Chatbot", layout="centered")
st.title("🧠 Multimodal Chatbot (Text + Image)")

mode = st.radio("Query Type", ["Text only", "Image + Text"])

if mode == "Text only":
    question = st.text_input("Ask a question:")
    if st.button("Send Text Query"):
        if not question.strip():
            st.warning("Please type a question first.")
        else:
            try:
                resp = requests.post(f"{API_BASE}/query/text", json={"question": question})
                data = resp.json()
                st.success(data.get("answer", "No answer field in response."))
            except Exception as e:
                st.error(f"Error calling API: {e}")

else:
    image_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    question = st.text_input("Ask something about the image (optional):")
    if st.button("Send Image Query"):
        if image_file is None:
            st.warning("Please upload an image first.")
        else:
            try:
                files = {"image": (image_file.name, image_file.getvalue(), image_file.type)}
                data = {"question": question}
                resp = requests.post(f"{API_BASE}/query/image", files=files, data=data)
                data = resp.json()
                st.image(image_file, caption="Uploaded image", use_column_width=True)
                if "answer" in data:
                    st.success(data["answer"])
                else:
                    st.error(data.get("error", "Unknown error from API."))
            except Exception as e:
                st.error(f"Error calling API: {e}")
