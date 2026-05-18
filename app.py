import streamlit as st
from PIL import Image

# 1. 페이지 기본 설정 (넓은 화면, 제목)
st.set_page_config(page_title="Cool-Choi Portfolio", layout="wide")

# 2. 상단 헤더 및 메뉴 (심플하게 구현)
st.markdown("<h3 style='text-align: right; color: gray;'>About | Milestones | Experience | Skills | Contact</h3>", unsafe_allow_html=True)
st.markdown("## **COOL CHOI**")
st.write("---")

# 3. 메인 타이틀 영역 (image_bf3ce6.png 스타일)
st.markdown("<h1 style='font-size: 50px; color: #1E3A8A;'>10년의 흐름, <br>하나의 궤적.</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color: gray;'>호기심에서 시작해 도전으로, 그리고 빛나는 성취로.<br>시간 순으로 펼쳐본 쿨초이(최시원)의 여정.</h4>", unsafe_allow_html=True)
st.write("")
st.write("")

# 4. 타임라인 영역 (연도 - 설명 - 사진 구조)

# [2024년 기록]
col1, col2, col3 = st.columns([1, 4, 3])
with col1:
    # 연도를 강조하는 마커 느낌
    st.markdown("<h3 style='color: #3B82F6;'>📍 2024</h3>", unsafe_allow_html=True)
with col2:
    st.markdown("<p style='color: #3B82F6; font-weight: bold;'>지력과 집중력의 증명</p>", unsafe_allow_html=True)
    st.markdown("### 마인드스포츠 전국 4위 및 국가대표 인증")
    st.write("대한마인드스포츠협회 주관 대회에서 뛰어난 집중력과 전략을 발휘하여 동상을 수상하고, 명예 국가대표 인증서를 수여받았습니다. 사소한 보드게임에서 시작된 흥미가 전국 단위의 성과로 이어졌습니다.")
with col3:
    # 실제 실행 시 형님의 이미지 경로로 변경하세요. (예: "KakaoTalk_20260518_195539069_03.jpg")
    st.info("🖼️ 여기에 [마인드스포츠 트로피/인증서 사진]이 들어갑니다.\n\n`st.image('이미지경로.jpg')` 코드를 사용하세요.")
    
st.write("---")

# [2025년 기록]
col1, col2, col3 = st.columns([1, 4, 3])
with col1:
    st.markdown("<h3 style='color: #3B82F6;'>📍 2025</h3>", unsafe_allow_html=True)
with col2:
    st.markdown("<p style='color: #3B82F6; font-weight: bold;'>극한의 체력과 끈기</p>", unsafe_allow_html=True)
    st.markdown("### 633km 자전거 국토종주 완주")
    st.write("어린 나이에 인천에서 서울 구간을 거쳐, 최고 난이도인 이화령 5km 오르막 구간을 포기하지 않고 정복했습니다. 비가 오는 궂은 날씨 속에서도 페달을 밟아 마침내 국토종주 및 4대강 종주 인증을 이뤄낸 값진 땀방울의 기록입니다.")
with col3:
    # 갤러리 형태로 여러 장을 작게 넣을 수도 있습니다.
    st.info("🖼️ 여기에 [이화령 정상 도착 사진 및 종주 인증서 사진]이 들어갑니다.\n\n`st.image('이미지경로.jpg')` 코드를 사용하세요.")

st.write("---")

# [2026년 이후 기록을 위한 공간]
col1, col2, col3 = st.columns([1, 4, 3])
with col1:
    st.markdown("<h3 style='color: #ccc;'>📍 2026 ~</h3>", unsafe_allow_html=True)
with col2:
    st.markdown("### 다음 도전은 계속됩니다.")
    st.write("쿨초이의 무한한 가능성과 새로운 이야기들이 이곳에 채워질 예정입니다.")
with col3:
    st.empty()
