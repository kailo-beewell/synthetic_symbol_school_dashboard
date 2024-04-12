from kailo_beewell_dashboard.authentication import check_password
from kailo_beewell_dashboard.images import get_image_path
from kailo_beewell_dashboard.import_data import import_tidb_data
from kailo_beewell_dashboard.page_setup import (
    blank_lines, page_footer, page_setup)
from kailo_beewell_dashboard.static_report import (
    create_static_symbol_report)
import streamlit as st
from tempfile import NamedTemporaryFile
import weasyprint

page_setup('symbol')

if check_password('symbol'):

    # Import the data from TiDB Cloud if not already in session state
    import_tidb_data('symbol')

    # Title and introduction
    st.title('The #BeeWell Survey')
    st.markdown('''
<p style='text-align: center; font-weight: bold'>
Thank you for taking part in the #BeeWell survey delivered by Kailo.<br>
You can use this dashboard to explore results from pupils at your school.</p>
''', unsafe_allow_html=True)

    # Image
    st.image(get_image_path('home_image_3_transparent.png'),
             use_column_width=True)

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
        if st.button('Generate report - will take around 7 seconds'):
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
