import fear_and_greed
import streamlit as st
from datetime import datetime

# 1. 데이터 가져오기
index_data = fear_and_greed.get()
value = int(index_data.value)
status = index_data.description
date = datetime.now().date()

# 2. 페이지 설정
st.set_page_config(page_title="F&G Gauge Widget", layout="centered")

# 3. 위젯 CSS 설정
st.markdown(f"""
    <style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .block-container {{ padding: 10px !important; }}

    h1 {{ font-size: 16px !important; text-align: center; margin-bottom: 15px !important; }}
    
    /* 게이지 바 레이아웃 */
    .gauge-wrapper {{
        width: 100%;
        margin: 0 auto;
    }}
    .gauge-container {{
        background-color: #e0e0e0;
        border-radius: 10px;
        height: 15px;
        width: 100%;
        overflow: hidden;
    }}
    .gauge-bar {{
        background-color: {"#ff4b4b" if value < 50 else "#2ecc71"};
        width: {value}%;
        height: 100%;
        transition: width 0.5s ease-in-out;
    }}
    
    /* 양끝 라벨 스타일 */
    .label-container {{
        display: flex;
        justify-content: space-between;
        margin-top: 5px;
        font-size: 11px;
        font-weight: bold;
    }}
    .fear-label {{ color: #ff4b4b; }}
    .greed-label {{ color: #2ecc71; }}
    
    /* 현재 점수 중앙 표시 */
    .current-status {{
        text-align: center;
        font-size: 15px;
        font-weight: bold;
        margin-top: 10px;
        color: #37352f;
    }}
    </style>
    """, unsafe_allow_html=True)

# 4. 출력 부분
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
            {status} ({value}/100)
        </div>
    </div>
    """, unsafe_allow_html=True)
