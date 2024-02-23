import streamlit as st
from kailo_beewell_dashboard.page_setup import (
    page_setup, page_footer, blank_lines)
from kailo_beewell_dashboard.static_report import (
    create_static_symbol_report)
import weasyprint
from tempfile import NamedTemporaryFile
import pandas as pd

page_setup('symbol')

# Set school
st.session_state.school = 'School A'

# Import data
st.session_state.responses = pd.read_csv(
    'data/survey_data/aggregate_responses.csv')
st.session_state.counts = pd.read_csv(
    'data/survey_data/overall_counts.csv')
st.session_state.demographic = pd.read_csv(
    'data/survey_data/aggregate_demographic.csv')

# Use test=True to indent text, which is basically just to prevent me from
# having to redo the line indentation once have added check_password()
test = True
if test:
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
    st.markdown('''
You can use the interactive dashboard to explore results for your school. We
also provide the option of downloading a PDF version of your results below.''')

    # If report had not be generated, show generate report button
    if 'pdf_report' not in st.session_state:
        # If this button is clicked...
        if st.button('Generate report - will take around 5 seconds'):
            # Show spinner whilst operation occurs
            with st.spinner('Generating report'):
                # Produce the HTML for the report
                st.session_state.html_content = create_static_symbol_report(
                    chosen_school=st.session_state.school,
                    df_prop=st.session_state.responses,
                    counts=st.session_state.counts,
                    dem_prop=st.session_state.demographic,
                    pdf_title='#BeeWell Kailo School Report 2024')
                # Convert to temporary PDF file, then read PDF back into
                # environment and store report in the session state
                with NamedTemporaryFile(suffix='.pdf') as temp:
                    weasyprint.HTML(
                        string=st.session_state.html_content).write_pdf(temp)
                    temp.seek(0)
                    st.session_state['pdf_report'] = open(temp.name, 'rb')
            # Re-run script, so the generate button is removed
            st.rerun()
    # If report has been generated for this group, show download button
    elif 'pdf_report' in st.session_state:
        st.download_button(
            label='Download report',
            data=st.session_state['pdf_report'],
            file_name='kailo_beewell_school_report.pdf',
            mime='application/pdf')

    # BeeWell pupil video
    blank_lines(2)
    st.subheader('Introduction to the survey')
    st.markdown('''
If you're unfamiliar with the #BeeWell survey or would like a reminder, you can
check out the video below. This video (which was designed for pupils) explains
what pupils could expect from taking part in the survey. For more information,
see the 'About' page of the dashboard.''')
    st.video('https://youtu.be/jmYH7F2Bd4Q')

    page_footer(st.session_state.school)
