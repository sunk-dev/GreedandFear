import fear_and_greed
import streamlit as st
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(page_title="F&G Gauge Widget", layout="centered")

index_data = fear_and_greed.get()
value = int(index_data.value)
status = index_data.description
date = datetime.now().date()

# 2. 상태별 색상 설정
if value < 25: color = "#ff4b4b" # Extreme Fear (빨강)
elif value < 45: color = "#ffa421" # Fear (주황)
elif value < 55: color = "#f1c40f" # Neutral (노랑)
elif value < 75: color = "#2ecc71" # Greed (초록)
else: color = "#0068c9" # Extreme Greed (파랑)

# 3. 위젯 CSS 설정
st.markdown(f"""
    <style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .block-container {{ padding: 10px !important; }}

    h1 {{ font-size: 16px !important; margin-bottom: 10px !important; }}
    
    /* 게이지 바 배경 */
    .gauge-container {{
        background-color: #e0e0e0;
        border-radius: 10px;
        height: 20px;
        width: 100%;
        overflow: hidden;
        margin-top: 5px;
    }}
    /* 실제 게이지 바 */
    .gauge-bar {{
        background-color: {color};
        width: {value}%;
        height: 100%;
        transition: width 0.5s ease-in-out;
    }}
    .status-text {{
        font-size: 14px;
        font-weight: bold;
        margin-top: 8px;
        text-align: right;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. 출력 부분
st.markdown(f"# 📊 F&G Index: {date}")

# 게이지 바 렌더링
st.markdown(f"""
    <div class="gauge-container">
        <div class="gauge-bar"></div>
    </div>
    <div class="status-text" style="color: {color};">
        {status} ({value}/100)
    </div>
    """, unsafe_allow_html=True)
