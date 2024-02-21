import streamlit as st
from kailo_beewell_dashboard.page_setup import (
    page_setup, page_footer, blank_lines)
from kailo_beewell_dashboard.reshape_data import get_school_size
from kailo_beewell_dashboard.who_took_part import (
    create_demographic_page_intro, demographic_plots)
import pandas as pd

page_setup('symbol')

# Set school
st.session_state.school = 'School A'

# Use test=True to indent text, which is basically just to prevent me from
# having to redo the line indentation once have added check_password()
test = True
if test:

    # Import data (will need to change this to import from TIDB cloud)
    dem_prop = pd.read_csv('data/survey_data/aggregate_demographic.csv')
    counts = pd.read_csv('data/survey_data/overall_counts.csv')

    # Get total pupil number
    school_size = get_school_size(counts, st.session_state.school, 'symbol')

    # Write title and introduction
    create_demographic_page_intro(school_size)
    blank_lines(1)

    # Create the figures (with their titles and descriptions)
    dem_prop['plot_group'] = dem_prop['measure']
    demographic_plots(dem_prop, st.session_state.school,
                      chosen_group='For your school', survey_type='symbol')

    page_footer(st.session_state.school)
