import streamlit as st
import streamlit_chat as sc
from text_summarizer import summarizer
from streamlit_chat import message

st.set_page_config(
    page_title="Summarizer",
    page_icon=":robot:"
)



st.header("Summarizer")
st.markdown("[Github](https://github.com/Phynxxx/Text-Summarizer)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

message("Hello, I am a chat summarizer that can summarize paragraphs!")



def get_text():
    input_text = st.text_input("You: ", key="input", placeholder="Enter the original text")
    return input_text 

user_input = get_text()

if user_input:
    output_summary, output_org_word_count, output_summary_word_count = summarizer(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output_summary)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

