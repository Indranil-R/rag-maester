import streamlit as st

st.set_page_config(page_title="RAG Maester",layout="centered")

st.title("RAG Maester 📜")
st.write("Your AI Scholar for Research and Learning")


st.sidebar.write("Summon the RAG Maester — and ask your questions. "
        "The Maester shall delve into the depths of knowledge to bring you answers.")
st.sidebar.title("Instructions")

st.sidebar.write("- Just ask your question in the chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask the Maester...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from the RAG chain
    with st.chat_message("assistant"):
        with st.spinner("Consulting the scrolls..."):
            response = rag_chain.invoke({"input": user_input})
            answer = response["answer"]
            st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})
