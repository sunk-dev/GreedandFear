import fear_and_greed
import streamlit as st
from datetime import datetime

# 1. 페이지 설정 및 데이터 가져오기
st.set_page_config(page_title="F&G Index Widget", layout="centered")

index_data = fear_and_greed.get()
value = int(index_data.value)
status = index_data.description
date = datetime.now().date()

# 2. 위젯 전용 스타일 설정 (타이틀 크기 및 여백 압축)
st.markdown(f"""
    <style>
    /* 메뉴 및 푸터 숨기기 */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* 불필요한 패딩 제거 (위젯 최적화) */
    .block-container {{
        padding-top: 5px !important;
        padding-bottom: 5px !important;
        padding-left: 10px !important;
        padding-right: 10px !important;
    }}

    /* 타이틀 크기 조절 (# 사용 시 적용) */
    h1 {{
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #37352f;
        margin-bottom: 15px !important;
        padding-top: 0px !important;
    }}

    /* Metric 레이아웃 압축 */
    [data-testid="stMetric"] {{
        background-color: #f7f6f3;
        padding: 10px;
        border-radius: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. 타이틀 (작은 크기 마크다운)
st.markdown(f"# 📊 Fear & Greed: {date}")

# 4. 상태별 색상 로직 및 메트릭 표시
# 수치에 따라 텍스트 색상을 정하는 헬퍼 변수
color = "red" if value < 45 else "green" if value > 55 else "orange"

# 메트릭 표시 (Label에 상태, Value에 점수)
st.metric(
    label=f"Status: :{color}[{status}]", 
    value=f":{color}[{value}]",
    delta=None # 변화량을 넣고 싶으면 여기에 추가
)
