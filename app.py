import streamlit as st
from inference_logic import truncate_input, get_response  # Importă logica de inferență

# Streamlit app configurations
st.title("Chatbot Starter")

# Initialize chat history
if "user_messages" not in st.session_state:
    st.session_state.user_messages = [] 
if "assistant_responses" not in st.session_state:
    st.session_state.assistant_responses = [] 


# Display user messages and assistant responses
for user_msg, assistant_resp in zip(st.session_state.user_messages, st.session_state.assistant_responses):
    with st.chat_message("user", avatar="☺️"):
        st.markdown(user_msg)
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(assistant_resp)


# Input de la utilizator
if prompt := st.chat_input("Say something..."):
    # Display user message in chat message container
    with st.chat_message("user", avatar="☺️"):
        st.markdown(prompt)

    # Get response from the chatbot
    with st.spinner("Generate response..."):
       # prompt = truncate_input(prompt)
        response = get_response(prompt)


    # Save user message and assistant response in separate lists
    st.session_state.user_messages.append(prompt)
    st.session_state.assistant_responses.append(response)

  
    with st.spinner("Generate response..."):
        response = get_response(prompt)
    #st.success(response)
    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(response)
    