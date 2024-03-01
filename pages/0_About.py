import streamlit as st
from kailo_beewell_dashboard.page_setup import page_setup, page_footer
from kailo_beewell_dashboard.stylable_container import header_container
from kailo_beewell_dashboard.reuse_text import reuse_text
from kailo_beewell_dashboard.authentication import check_password

# Set page configuration
page_setup('symbol')

if check_password('symbol'):
    # Page title
    st.title('About')

    # Subheader
    st.markdown(reuse_text['about_intro'])

    # Expand toggle
    expand = st.toggle('Toggle to expand all the boxes below', value=False)

    header_container('green_container', '🌿 Kailo', '#D9ECCA')
    with st.expander('What is Kailo?', expanded=expand):
        st.markdown(reuse_text['kailo'])
        st.image('images/kailo_systems_adapted.png')

    header_container('orange_container', '🐝 The #BeeWell survey', '#F7DCC8')
    with st.expander('Who took part in the #BeeWell survey in Devon?',
                     expanded=expand):
        st.markdown('''
This years, pupils in Years 7 to 11 at **two non-mainstream schools** in North
Devon and Torridge completed the symbol version of the #BeeWell survey.

A longer, standard version of the survey was also completed by pupils in Years
8 and 10 at **seven mainstream secondary schools** in Northern Devon.''')
        st.image('images/northern_devon.png')

    with st.expander('What questions did the survey ask?', expanded=expand):
        st.markdown('''The survey contained ten questions which use the Widgit
                    symbol system. These were:''')
        # Add the images (they are the same as those used for the survey, but
        # cropped to height of 340 to remove the 'choose one' from each)
        st.image('images/survey/family_crop.png')
        st.image('images/survey/home_crop.png')
        st.image('images/survey/friends_crop.png')
        st.image('images/survey/choice_crop.png')
        st.image('images/survey/things_crop.png')
        st.image('images/survey/health_crop.png')
        st.image('images/survey/future_crop.png')
        st.image('images/survey/school_crop.png')
        st.image('images/survey/free_time_crop.png')
        st.image('images/survey/life_crop.png')
        st.markdown('For each questions, pupils had three response options:')
        st.image('images/survey/choose_one.png')
        cols = st.columns(3)
        with cols[0]:
            st.image('images/survey/happy.png')
        with cols[1]:
            st.image('images/survey/ok.png')
        with cols[2]:
            st.image('images/survey/sad.png')

    with st.expander('How was the survey designed?', expanded=expand):
        st.markdown('''
The survey delivered in Northern Devon is the same as that first designed and
delivered by the #BeeWell team in Greater Manchester. They worked with staff
in special school settings to co-design a symbol version of the #BeeWell survey
that would be accessible to young people with severe learning difficulties or
profound and multiple learning disabilities. Using The Children's Society's
'Good Childhood Index' for inspiration, they created a 10-item survey using the
Widgit symbol system with simplified response options.''')

    with st.expander('Where else have these surveys been completed?',
                     expanded=expand):
        st.markdown('''
#BeeWell surveys have also been completed by pupils at schools in Hampshire,
Greater Manchester, the London borough of Havering, and Milton Keynes. You can
find out more about other sites at https://beewellprogramme.org/.''')
        st.image('images/beewell_map.png')

    header_container('blue_container', '📊 Dashboard', '#D0C9FF')

    with st.expander('What data has been used in this dashboard?',
                     expanded=expand):
        st.markdown('''
This dashboard presents the results from pupils at your school who completed
the survey.

The survey responses were combined with data shared by the local authority such
as free school meal eligibility and special education needs to give further
insight into responses.''')

    with st.expander('How should we use these results?', expanded=expand):
        st.markdown(reuse_text['how_to_use_results'])
        st.image('images/thinking.png')

    with st.expander('Can I access this dashboard on different devices?',
                     expanded=expand):
        st.markdown(reuse_text['view_devices'])
        st.image('images/devices.png')

    with st.expander('''
Will there be support available for interpreting and actioning on the dashboard
results?''', expanded=expand):
        st.markdown(reuse_text['dashboard_support'])

    header_container('yellow_container', '😌 Wellbeing', '#FFF3B3')

    with st.expander('''
What do we already know about young people's wellbeing?''', expanded=expand):
        st.markdown(reuse_text['wellbeing_context'], unsafe_allow_html=True)

    page_footer(st.session_state.school)
