import re
from utils_r import pairs
import streamlit as st

def eliza(inp: str, show_regex: bool) -> str:
    for pair in pairs:
        pattern = re.compile(pair[0], re.IGNORECASE)
        match = re.search(pattern, inp)
        if match:
            if match.groups(1):
                if show_regex:
                    st.code(f"Regex Pattern: {pair[0]}", language='plaintext')
                return pair[1].format(match.group(1))
            else:
                if show_regex:
                    st.code(f"Regex Pattern: {pair[0]}", language='plaintext')
                return pair[1]
    return "Sorry, I didn't understand your question"

def main():
    # Set page title
    st.set_page_config(page_title="ELIZA Chatbot", page_icon=":robot_face:")
    
    # Main content
    st.title("ELIZA Chatbot for basic NLP questions")
    
    # Input
    user_input = st.text_input("You: ")
    
    # Boolean option to show regex
    show_regex = st.checkbox("Show Regex")
    
    if st.button("Ask ELIZA"):
        # Process input and get result
        result = eliza(user_input, show_regex)
        
        # Display ELIZA's response
        st.write(result)

if __name__ == "__main__":
    main()
