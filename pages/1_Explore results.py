import streamlit as st
from utilities.page_setup import page_setup, page_footer

page_setup()

# Set school
st.session_state.school = 'School A'

st.title('Explore results')

page_footer(st.session_state.school)
