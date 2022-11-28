from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

#with st.echo(code_location='below'):
pages = ["Home", "Player Exploration", "Predictive Model"]
choice = st.sidebar.selectbox("Select a page:", pages)
if choice == "Home":
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Major_League_Baseball_logo.svg/1200px-Major_League_Baseball_logo.svg.png")
        years = ["2022", "2021", "2020", "2019"]
        year = st.selectbox(" ", years)
elif choice == "Player Exploration":
        st.markdown("Select type of player:")
        st.radio(" ", ["Batter", "Pitcher"], horizontal=True)
        players = ["Mike Trout", "Aaron Judge", "Mookie Betts", "Jose Altuve"]
        st.selectbox("Player:", players)
elif choice == "Predictive Model":
        print("hello")
