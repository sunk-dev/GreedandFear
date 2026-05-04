import fear_and_greed
import streamlit as st
from datetime import datetime

# 1. 데이터 가져오기
index_data = fear_and_greed.get()
value = int(index_data.value)
status = index_data.description
date = datetime.now().date()

# 2. 상태별 동적 색상 설정
if value < 25:
    current_color = "#ff4b4b" # Extreme Fear (강한 빨강)
elif value < 45:
    current_color = "#ffa421" # Fear (주황)
elif value < 55:
    current_color = "#f1c40f" # Neutral (노랑)
elif value < 75:
    current_color = "#2ecc71" # Greed (초록)
else:
    current_color = "#0068c9" # Extreme Greed (파랑 또는 진한 초록)

# 3. 페이지 설정
st.set_page_config(page_title="F&G Gauge Widget", layout="centered")

# 4. 위젯 CSS 설정
st.markdown(f"""
    <style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .block-container {{ padding: 10px !important; }}

    h1 {{ font-size: 16px !important; text-align: center; margin-bottom: 15px !important; }}
    
    /* 게이지 바 레이아웃 */
    .gauge-container {{
        background-color: #e0e0e0;
        border-radius: 10px;
        height: 18px;
        width: 100%;
        overflow: hidden;
    }}
    .gauge-bar {{
        background-color: {current_color};
        width: {value}%;
        height: 100%;
        transition: width 0.5s ease-in-out;
    }}
    
    /* 양끝 라벨 스타일 */
    .label-container {{
        display: flex;
        justify-content: space-between;
        margin-top: 8px;
        font-size: 12px;
        font-weight: bold;
    }}
    .fear-label {{ color: #ff4b4b; }}
    .greed-label {{ color: #2ecc71; }}
    
    /* 중앙 상태 및 지수 폰트 크기 키움 & 동적 색상 적용 */
    .current-status {{
        text-align: center;
        font-size: 22px !important; /* 폰트 크기 확대 */
        font-weight: 800 !important;
        margin-top: 15px;
        color: {current_color} !important; /* 수치에 따른 색상 적용 */
    }}
    </style>
    """, unsafe_allow_html=True)

# 5. 출력 부분
st.markdown(f"# 📊 Fear & Greed Index ({date})")

# 게이지 및 라벨 렌더링
st.markdown(f"""
    <div class="gauge-wrapper">
        <div class="gauge-container">
            <div class="gauge-bar"></div>
        </div>
        <div class="label-container">
            <span class="fear-label">Extreme Fear</span>
            <span class="greed-label">Extreme Greed</span>
        </div>
        <div class="current-status">
            {status} <br>
            <span style="font-size: 30px;">{value}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
