import streamlit as st
from kailo_beewell_dashboard.page_setup import page_setup, page_footer
from kailo_beewell_dashboard.stylable_container import header_container
from kailo_beewell_dashboard.reuse_text import text_how_use

# Set page configuration
page_setup('symbol')

# Set school
st.session_state.school = 'School A'

# Use test=True to indent text, which is basically just to prevent me from
# having to redo the line indentation once have added check_password()
test = True
if test:
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
the survey. To give context to these results, we've added comparisons against
pupils from schools across Northern Devon.

The survey responses were combined with data shared by the local authority such
as free school meal eligibility and special education needs to give further
insight into responses.''')

    with st.expander('How should we use these results?', expanded=expand):
        st.markdown(text_how_use())
        st.image('images/thinking.png')

    with st.expander('Can I access this dashboard on different devices?',
                     expanded=expand):
        st.markdown('''
Yes - this dashboard will resize so you should be able to access it on a range
of devices (computer/laptop, tablet, phone, etc).''')
        st.image('images/devices.png')

    with st.expander('''
Will there be support available for interpreting and actioning on the dashboard
results?''', expanded=expand):
        st.markdown('''
Yes - Child Outcomes Research Consortium (CORC) has been funded to provide
seminars and 1:1 support to schools in Northern Devon, to help you understand
how to navigate the dashboard, interpret results, and suggest feedback in the
development of action plans. You should receive information about this via
email, but if you have not or have any questions, please contact us at
kailobeewell@dartington.org.uk.''')

    header_container('yellow_container', '😌 Wellbeing', '#FFF3B3')

    with st.expander('''
What do we already know about young people's wellbeing?''', expanded=expand):
        st.markdown('''
* The peak age of onset of mental health difficulties is 14.5 years.<sup>[1]
</sup>
* Mental health and wellbeing in adolescence predicts adult health, labour
market and other important outcomes.<sup>[2]</sup>
* The wellbeing of adolescents has decreased in the last two decades, while the
prevalence of mental health difficulties among them has increased.<sup>[3,4]
</sup>
* A recent international study ranked the UK’s young people fourth from bottom
across nearly 80 countries in terms of life satisfaction.<sup>[5,6]</sup>
* Young people’s mental health and wellbeing can be influenced by multiple
drivers, including their health and routines, hobbies and entertainment,
relationships, school, environment and society, and how they feel about their
future.<sup>[7]</sup>

<p style='font-size: 12px;'>
References:<br>
[1] Solmi, M. et al (2021). Age at onset of mental disorders worldwide:
large-scale meta-analysis of 192 epidemiological studies. Molecular Psychiatry,
Online First. Available at: https://www.nature.com/articles/s41380-021-01161-7
<br>
[2] Goodman A, Joshi H, Nasim B, Tyler C (2015). Social and emotional skills in
childhood and their long-term effects on adult life. London: EIF. Available at:
https://www.eif.org.uk/report/social-and-emotional-skills-in-childhood-and-thei
r-long-term-effects-on-adult-life.<br>
[3] Children’s Society (2021). The Good Childhood Report 2021. London:
Children's Society. Available at: https://www.childrenssociety.org.uk/informati
on/professionals/resources/good-childhood-report-2021<br>
[4] NHS Digital (2021). Mental health of children and young people in England,
2021 – wave 2 follow up to the 2017 survey. London: NHS Digital. Available at:
https://digital.nhs.uk/data-and-information/publications/statistical/mental-hea
lth-of-children-and-young-people-in-england/2021-follow-up-to-the-2017-survey
<br>
[5] Office for Economic Cooperation and Development (2019). Programme for
International Student Assessment (PISA) results. Paris: OECD. Available at:
https://www.oecd.org/publications/pisa-2018-results-volume-iii-acd78851-en.htm
<br>
[6] Marquez J, Long, E (2021). A Global Decline in Adolescents' Subjective
Well-Being: a Comparative Study Exploring Patterns of Change in the Life
Satisfaction of 15-Year-Old Students in 46 Countries. Child Ind Res 14,
1251–1292 (2021). Available at: https://doi.org/10.1007/s12187-020-09788-8<br>
[7] #BeeWell Programme Team (2021). #BeeWell survey. Manchester: University of
Manchester. Available at: https://gmbeewell.org/wp-content/uploads/2021/09/BeeW
ell-Questionnaires-Booklet.pdf</p>''', unsafe_allow_html=True)

    page_footer(st.session_state.school)
