import fear_and_greed
import streamlit as st
from datetime import datetime
def get_fing_data():
    index_data = fear_and_greed.get()
    return index_data
# return data


# page setting
st.set_page_config(page_title="F&G Index Wiget", layout="centered")
index_data=fear_and_greed.get()
value=int(index_data.value)
status=index_data.description

#wiget design
date=datetime.now()
st.title(f"Fear& Greed Index: {date.date()}")
if value<25 or (value>25 and value<45):
    # st.error("Extreme Fear")
    st.metric(label=f"Status: :red[{status}]",value=value)

elif value>75 or (value>55 and value<75):
    # st.success("Extreme Greed")
    st.metric(label=f"Status: :green{status}",value=value)

