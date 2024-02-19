import streamlit as st
from utilities.page_setup import page_setup, page_footer
from utilities.stylable_container import header_container

# Set page configuration
page_setup()

# Set school
st.session_state.school = 'School A'

# Page title
st.title('About')

# Subheader
st.markdown('''
This page has lots of helpful information about the research projects (Kailo
and #BeeWell), as well as advice on using and accessing this dashboard, and
some background information around young people's wellbeing.''')

# Expand toggle
expand = st.toggle('Toggle to expand all the boxes below', value=False)

header_container('green_container', '🌿 Kailo', '#D9ECCA')
with st.expander('What is Kailo?', expanded=expand):
    st.markdown('''
Our aim is to help local communities, young people and public service
partnerships better understand and address the root causes (and wider
determinants) of young people's mental health.

We're made up of leading academics, designers and practitioners, dedicated to
working alongside communities in specific localities. Together, we will test
and co-design evidence-based responses (in a 'framework') to these root causes,
over the next four years.

Our model is formed of three key stages:
* **Early Discovery** - here, we build strong and trusted relationships with
local partners with an aim to understand what matters locally thus, forming
communities around youth- and community-centred priorities
* **Deeper Discovery and Codesign** - this stage, which we're in currently,
sees us codesign systemic responses to social determinants.
* **Prototyping, Implementation and Testing** - this is where the learning is
applied, integrating the codesigned responses with the local system,
prototyping them and making iterative refinements along the way.

To find our more about Kailo, check out our site: https://kailo.community/''')
    st.image('images/kailo_systems_adapted.png')

st.markdown('To add: remaining sections of About page.')

page_footer(st.session_state.school)
