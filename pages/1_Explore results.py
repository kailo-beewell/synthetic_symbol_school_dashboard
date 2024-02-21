import pandas as pd
import streamlit as st
from kailo_beewell_dashboard.page_setup import (
    page_setup, page_footer, blank_lines)
from kailo_beewell_dashboard.explore_results import (
    write_page_title,
    get_chosen_result,
    create_bar_charts)

page_setup('symbol')

# Set school
st.session_state.school = 'School A'

# Use test=True to indent text, which is basically just to prevent me from
# having to redo the line indentation once have added check_password()
test = True
if test:

    # Import data (will need to change this to import from TIDB cloud)
    counts = pd.read_csv('data/survey_data/overall_counts.csv')
    df_prop = pd.read_csv('data/survey_data/aggregate_responses.csv')

    # Add title and introduction
    write_page_title(survey_type='symbol')

    # Select pupils to view results for
    chosen_group = st.selectbox(
        '**View results:**', [
            'For all pupils', 'By year group', 'By gender', 'By FSM'])
    blank_lines(2)

    # Set chosen_variable and chosen_variable lab, and add to dataframe
    # (We don't currently have any groupings, all on once page, so only adding
    # this for simplicity in compatability with the bar chart functions
    # used across the standard and symbol survey dashboards)
    chosen_variable = 'symbol'
    chosen_variable_lab = 'symbol'
    df_prop['group'] = chosen_variable

    # Extract results for the chosen school and group
    chosen_result = get_chosen_result(
        chosen_variable, chosen_group, df_prop, st.session_state.school,
        survey_type='symbol')

    # Produce bar charts w/ accompanying chart section descriptions and titles
    create_bar_charts(chosen_variable, chosen_result)


page_footer(st.session_state.school)
