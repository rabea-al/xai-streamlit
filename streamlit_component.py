from xai_components.base import InArg, OutArg, InCompArg, Component, xai_component

@xai_component(color="red")
class Streamlit_Component(Component):
    """The simplest streamlit component. 
    """
    DATE_COLUMN: InArg[str]
    data_url: InArg[str]


    def __init__(self):

        self.done = False
        self.date_column = InArg.empty()
        self.data_url = InArg.empty()
        
    def execute(self, ctx) -> None:

        import streamlit as st
        import pandas as pd
        import numpy as np

        st.title('Uber pickups in NYC')

        date_column = self.date_column.value
        data_url = self.data_url.value

        
        @st.cache
        def load_data(nrows):
            data = pd.read_csv(data_url, nrows=nrows)
            lowercase = lambda x: str(x).lower()
            data.rename(lowercase, axis='columns', inplace=True)
            data[date_column] = pd.to_datetime(data[date_column])
            return data

        data_load_state = st.text('Loading data...')
        data = load_data(10000)
        data_load_state.text("Done! (using st.cache)")

        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(data)

        st.subheader('Number of pickups by hour')
        hist_values = np.histogram(data[date_column].dt.hour, bins=24, range=(0,24))[0]
        st.bar_chart(hist_values)

        # Some number in the range 0-23
        hour_to_filter = st.slider('hour', 0, 23, 17)
        filtered_data = data[data[date_column].dt.hour == hour_to_filter]

        st.subheader('Map of all pickups at %s:00' % hour_to_filter)
        st.map(filtered_data)