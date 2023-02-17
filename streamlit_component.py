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
        
from xai_components.base import InArg, OutArg, InCompArg, Component, BaseComponent, xai_component
import streamlit as st
import numpy as np
import pandas as pd

@xai_component
class DataFrameFromCsv(Component):
    file: InArg[str]
    data_frame: OutArg[pd.DataFrame]

    def __init__(self):
        self.done = False
        self.file = InArg.empty()
        self.data_frame = OutArg.empty()

    def execute(self, ctx) -> None:
        self.data_frame.value = pd.read_csv(self.file.value)

@xai_component
class StreamlitMainLayout(Component):
    module: OutArg[any]

    def __init__(self):
        self.done = False
        self.module = OutArg.empty()

    def execute(self, ctx) -> None:
        self.module.value = st

@xai_component
class StreamlitSidebarLayout(Component):
    sidebar: OutArg[any]

    def __init__(self):
        self.done = False
        self.sidebar = OutArg.empty()

    def execute(self, ctx) -> None:
        self.sidebar.value = st.sidebar

@xai_component
class StreamlitMakeColumns(Component):
    count: InArg[int]
    columns: OutArg[list]

    def __init__(self):
        self.done = False
        self.count = InArg.empty()
        self.columns = OutArg.empty()

    def execute(self, ctx) -> None:
        self.columns.value = st.columns(self.count.value)


@xai_component
class StreamlitWrite(Component):
    layout: InArg[any]
    object: InArg[any]
    layout_out: OutArg[any]

    def __init__(self):
        self.done = False
        self.layout = InArg.empty()
        self.object = InArg.empty()
        self.layout_out = OutArg.empty()

    def execute(self, ctx) -> None:
        if self.layout.value is None:
            st.write(self.object.value)
        else:
            with self.layout.value:
                st.write(self.object.value)

            self.layout_out.value = self.layout.value

@xai_component
class StreamlitDataFrame(Component):
    layout: InArg[any]
    data_frame: InArg[pd.DataFrame]
    layout_out: OutArg[any]

    def __init__(self):
        self.done = False
        self.layout = InArg.empty()
        self.data_frame = InArg.empty()
        self.layout_out = OutArg.empty()

    def execute(self, ctx) -> None:
        if self.layout.value is None:
            st.dataframe(self.data_frame.value)
        else:
            with self.layout.value:
                st.dataframe(self.data_frame.value)

            self.layout_out.value = self.layout.value

@xai_component
class StreamlitTable(Component):
    layout: InArg[any]
    data_frame: InArg[pd.DataFrame]
    layout_out: OutArg[any]

    def __init__(self):
        self.done = False
        self.layout = InArg.empty()
        self.data_frame = InArg.empty()
        self.layout_out = OutArg.empty()

    def execute(self, ctx) -> None:
        if self.layout.value is None:
            st.table(self.data_frame.value)
        else:
            with self.layout.value:
                st.table(self.data_frame.value)

            self.layout_out.value = self.layout.value


@xai_component
class StreamlitLineChart(Component):
    layout: InArg[any]
    data_frame: InArg[pd.DataFrame]
    layout_out: OutArg[any]

    def __init__(self):
        self.done = False
        self.layout = InArg.empty()
        self.data_frame = InArg.empty()
        self.layout_out = OutArg.empty()

    def execute(self, ctx) -> None:
        if self.layout.value is None:
            st.line_chart(self.data_frame.value)
        else:
            with self.layout.value:
                st.line_chart(self.data_frame.value)

            self.layout_out.value = self.layout.value

@xai_component
class StreamlitMap(Component):
    layout: InArg[any]
    data_frame: InArg[pd.DataFrame]
    layout_out: OutArg[any]

    def __init__(self):
        self.done = False
        self.layout = InArg.empty()
        self.data_frame = InArg.empty()
        self.layout_out = OutArg.empty()

    def execute(self, ctx) -> None:
        if self.layout.value is None:
            st.map(self.data_frame.value)
        else:
            with self.layout.value:
                st.map(self.data_frame.value)

            self.layout_out.value = self.layout.value

@xai_component
class StreamlitSlider(Component):
    layout: InArg[any]
    name: InArg[str]
    description: InArg[str]
    code: InArg[str]
    layout_out: OutArg[any]

    def __init__(self):
        self.done = False
        self.layout = InArg.empty()
        self.name = InArg.empty()
        self.description = InArg.empty()
        self.code = InArg.empty()
        self.layout_out = OutArg.empty()

    def execute(self, ctx) -> None:
        slider = st.slider(self.name.value)

        if self.layout.value is None:
            st.write(slider, self.description.value, eval(code))
        else:
            with self.layout.value:
                st.write(slider, self.description.value, eval(code))

            self.layout_out.value = self.layout.value

@xai_component
class StreamlitTextInput(Component):
    layout: InArg[any]
    label: InArg[str]
    name: InArg[str]
    layout_out: OutArg[any]

    def __init__(self):
        self.done = False
        self.layout = InArg.empty()
        self.label = InArg.empty()
        self.name = InArg.empty()
        self.layout_out = OutArg.empty()

    def execute(self, ctx) -> None:
        if self.layout.value is None:
            st.text_input(self.label.value, key=self.name.value)
        else:
            with self.layout.value:
                st.text_input(self.layout.value, key=self.name.value)

            self.layout_out.value = self.layout.value

@xai_component
class StreamlitRadio(Component):
    layout: InArg[any]
    label: InArg[str]
    values: InArg[list]
    variable: OutArg[any]
    layout_out: OutArg[any]

    def __init__(self):
        self.done = False
        self.layout = InArg.empty()
        self.label = InArg.empty()
        self.values = InArg.empty()
        self.variable = OutArg.empty()
        self.layout_out = OutArg.empty()

    def execute(self, ctx) -> None:
        if self.layout.value is None:
            self.variable.value = st.radio(self.label.value, self.values.value)
        else:
            with self.layout.value:
                self.variable.value = st.radio(self.label.value, self.values.value)

            self.layout_out.value = self.layout.value


@xai_component
class StreamlitReadVariable(Component):
    name: InArg[str]
    value: OutArg[any]

    def __init__(self):
        self.done = False
        self.name = InArg.empty()
        self.value = OutArg.empty()

    def execute(self, ctx) -> None:
        self.value.value = getattr(st.session_state, self.name.value)

@xai_component
class StreamlitMarkdown(Component):
    layout: InArg[any]
    markdown: InArg[str]
    layout_out: OutArg[any]

    def __init__(self):
        self.done = False
        self.layout = InArg.empty()
        self.markdown = InArg.empty()
        self.layout_out = OutArg.empty()

    def execute(self, ctx) -> None:
        if self.layout.value is None:
            st.markdown(self.markdown.value)
        else:
            with self.layout.value:
                st.markdown(self.markdown.value)
            self.layout_out.value = self.layout.value
