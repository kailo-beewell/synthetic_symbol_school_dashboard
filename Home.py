import streamlit as st
from utilities.page_setup import page_setup, page_footer, blank_lines

page_setup()

# Set school
st.session_state.school = 'School A'

# Title and introduction
st.title('The #BeeWell Survey')
st.markdown('''
<p style='text-align: center; font-weight: bold'>
Thank you for taking part in the #BeeWell survey delivered by Kailo.<br>
You can use this dashboard to explore results from pupils at your school.</p>
''', unsafe_allow_html=True)

# Image
st.image('images/home_image_3_transparent.png', use_column_width=True)

# Pages of the dashboard
st.subheader('What each page of the dashboard can tell you')
st.markdown('''
There are four pages to see on this dashboard, which you can navigate to using
the sidebar on the left. These are:
* **About** - Read information on the #BeeWell survey, Kailo, and this
dashboard
* **Explore results** - Explore how your pupils responded to each survey
question, and see further information on how the summary page's comparison to
other schools was generated
* **Who took part** - See the characteristics of the pupils who took part in
the survey''')

blank_lines(2)

# Section for downloading PDF report
st.subheader('Download PDF report')
st.markdown('To add')

blank_lines(2)

# #BeeWell pupil video
st.subheader('Introduction to the survey')
st.markdown('''
If you're unfamiliar with the #BeeWell survey or would like a reminder, you can
check out the video below. This video (which was designed for pupils) explains
what pupils could expect from taking part in the survey. For more information,
see the 'About' page of the dashboard.''')
st.video('https://youtu.be/jmYH7F2Bd4Q')

page_footer(st.session_state.school)
