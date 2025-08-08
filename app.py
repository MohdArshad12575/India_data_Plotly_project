import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from IPython.terminal.shortcuts.filters import pass_through

st.set_page_config(layout="wide")

df = pd.read_csv('india_data.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,"Overall India")

st.sidebar.title("India Data Vizualization")
selected_state = st.sidebar.selectbox("Select a state",list_of_states)

primary = st.sidebar.selectbox("Select Primary Parameter",list(df.columns[[5,11,12,13,14,15,16,18,19,20,21,27,28,29,30]]))
secondary = st.sidebar.selectbox("Select Secondary Parameter",list(df.columns[[5,11,12,13,14,15,16,18,19,20,21,27,28,29,30]]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.subheader("Size Represents Primary Parameter")
    st.subheader("Color Represents Secondary Parameter")
    if selected_state == "Overall India":
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", zoom=3, mapbox_style="carto-positron"
                                ,size = primary,color=secondary,color_continuous_scale=["#FF0000",  "#FFA500", "#800080"]
                                ,size_max=20,width=1000,height=600,hover_name="District")
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df["State"] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", zoom=6, mapbox_style="carto-positron"
                                , size=primary, color=secondary,
                                color_continuous_scale=["#FF0000", "#FFA500", "#800080"], size_max=15, width=1000,
                                height=600,hover_name="District")
        st.plotly_chart(fig, use_container_width=True)
