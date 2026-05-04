import fear_and_greed
import streamlit as st
def get_fing_data():
    index_data = fear_and_greed.get()
    return index_data
# return data
'''
FearGreedIndex(value=66.6, description='greed', last_update=datetime.datetime(2026, 5, 1, 23, 59, 39, tzinfo=datetime.timezone.utc))
'''

# page setting
st.set_page_config(page_title="F&G Index Wiget", layout="centered")
index_data=fear_and_greed.get()
value=int(index_data.value)
status=index_data.description

#wiget design
st.title("Feat& Greed Index")
st.metric(label=f"Status: {status}",value=value)
if value<25:
    st.error("Extreme Fear")
elif value>75:
    st.success("Extreme Greed")
