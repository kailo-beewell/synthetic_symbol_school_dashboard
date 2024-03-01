import streamlit as st
from kailo_beewell_dashboard.page_setup import (
    page_setup, page_footer, blank_lines)
from kailo_beewell_dashboard.reshape_data import get_school_size
from kailo_beewell_dashboard.who_took_part import (
    create_demographic_page_intro, demographic_plots)
from kailo_beewell_dashboard.import_data import import_tidb_data
from kailo_beewell_dashboard.authentication import check_password

page_setup('symbol')

if check_password('symbol'):

    # Import the data from TiDB Cloud if not already in session state
    import_tidb_data('symbol')

    # Assign data from the session state
    dem_prop = st.session_state.demographic
    counts = st.session_state.counts

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
