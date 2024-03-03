import re
from utils_r import pairs
import streamlit as st

def eliza(inp: str) -> str:
    for pair in pairs:
        pattern = re.compile(pair[0], re.IGNORECASE)
        match = re.match(pattern, inp)
        if match:
            if match.groups(1):
                return pair[1].format(match.group(1))
            else:
                return pair[1]
    return "Sorry, I didn't understand your question"

def main():
    # Set page title
    st.set_page_config(page_title="ELIZA Chatbot for basic NLP questions", page_icon=":robot_face:")
    
    # Main content
    st.title("ELIZA Chatbot")
    
    # Input
    user_input = st.text_input("You: ")
    
    if st.button("Ask ELIZA"):
        # Process input and get result
        result = eliza(user_input)
        
        # Display ELIZA's response
        st.write(result)

if __name__ == "__main__":
    main()
