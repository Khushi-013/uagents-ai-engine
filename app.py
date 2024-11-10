import streamlit as st
from ai_engine.chitchat import ChitChatDialogue  # Correct import path here
from ai_engine.types import UAgentResponse, UAgentResponseType, KeyValue

# Initialize the Dialogue instance once during app launch
if 'dialogue' not in st.session_state:
    st.session_state.dialogue = ChitChatDialogue(version="0.1")
    st.session_state.conversation = []
    st.session_state.session_ended = False  # Track session state for ending the session

# Function to send a message and get a response
def get_agent_response(user_message):
    # Get response from the dialogue system
    response = st.session_state.dialogue.on_continue_dialogue(user_message)
    
    # Store conversation history in session state
    st.session_state.conversation.append(f"You: {user_message}")
    st.session_state.conversation.append(f"Agent: {response.message}")
    
    # Check if the session is ended based on the agent's response
    if "Goodbye" in response.message:
        st.session_state.session_ended = True
    
    return response.message

# Streamlit layout
st.title("Chat with Your Assistant")

# Display the previous conversation
if st.session_state.conversation:
    for message in st.session_state.conversation:
        st.write(message)

# Handle user input and display the agent's response
if st.session_state.session_ended:
    st.write("Session has ended. Thank you!")
else:
    # User message input
    user_input = st.text_input("You:", "")

    # Button to send the message
    if st.button("Send"):
        if user_input:
            agent_response = get_agent_response(user_input)
            st.write(f"Agent: {agent_response}")
        else:
            st.write("Please enter a message.")
