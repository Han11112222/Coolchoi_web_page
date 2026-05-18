import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="Cool-Choi Portfolio", layout="wide")

# 깔끔한 내비게이션 바 스타일링
st.markdown("<h3 style='text-align: right; color: gray;'>About | Milestones | Experience | Contact</h3>", unsafe_allow_html=True)
st.markdown("## **COOL CHOI PORTFOLIO**")
st.write("---")

# 2. 메인 타이틀 영역
st.markdown("<h1 style='font-size: 48px; color: #1E3A8A;'>10년의 흐름, 하나의 궤적.</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color: gray; line-height: 1.6;'>호기심에서 시작해 도전으로, 그리고 빛나는 성취로.<br>시간 순으로 펼쳐본 쿨초이(최시원)의 성장 기록입니다.</h4>", unsafe_allow_html=True)
st.write("")

# 3. 타임라인 및 사진 레이아웃 시작

# ==========================================
# [2023년] 독도 수호 활동 및 언론 보도
# ==========================================
st.write("")
col1, col2, col3 = st.columns([1, 4, 4])

with col1:
    st.markdown("<h3 style='color: #2563EB;'>📍 2023</h3>", unsafe_allow_html=True)
with col2:
    st.markdown("<p style='color: #2563EB; font-weight: bold;'>공동체 정신과 애국심</p>", unsafe_allow_html=True)
    st.markdown("### 독도 수호 행사 참가 및 신문 보도")
    st.write(
        "독도 수호 관련 공식 행사에 참여하여 뜻깊은 기회를 가졌습니다. "
        "행사에서의 활약이 인정되어 영남일보 지면에 당당히 소개되는 영예를 안았습니다. "
        "어릴 때부터 사회적 가치에 관심을 갖고 주도적으로 참여하는 역량을 키웠습니다."
    )
with col3:
    # 가로형 행사 사진과 세로형 신문 기사를 보기 좋게 배치
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        st.image("KakaoTalk_20260518_195539069.jpg", caption="독도 수호 행사 현장", use_container_width=True)
    with sub_col2:
        st.image("KakaoTalk_20260518_195539069_01.jpg", caption="영남일보 언론 보도 기사", use_container_width=True)

st.write("---")

# ==========================================
# [2024년] 마인드스포츠 전국 대회
# ==========================================
st.write("")
col1, col2, col3 = st.columns([1, 4, 4])

with col1:
    st.markdown("<h3 style='color: #2563EB;'>📍 2024</h3>", unsafe_allow_html=True)
with col2:
    st.markdown("<p style='color: #2563EB; font-weight: bold;'>지력과 높은 집중력의 증명</p>", unsafe_allow_html=True)
    st.markdown("### 마인드스포츠 전국 4위 및 명예 국가대표 인증")
    st.write(
        "대한마인드스포츠협회 주관 2025 마인드 스포츠 올림피아드 국가대표 선발전(1학년 부문)에서 "
        "뛰어난 전략과 고도의 집중력을 발휘하여 전국 4위(동상)에 입상했습니다. "
        "이와 함께 대구광역시 명예 국가대표 인증서를 수여받으며 남다른 두뇌 활용 능력을 증명했습니다."
    )
with col3:
    # 포토월 사진과 상장/트로피 상세 사진 배치
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        st.image("KakaoTalk_20260518_195539069_02.jpg", caption="마인드스포츠 시상식 포토월", use_container_width=True)
    with sub_col2:
        st.image("KakaoTalk_20260518_195539069_03.jpg", caption="동상 트로피 및 국가대표 인증서", use_container_width=True)

st.write("---")

# ==========================================
# [2025년] 633km 자전거 국토종주
# ==========================================
st.write("")
st.markdown("<h3 style='color: #2563EB;'>📍 2025 — 극한의 체력과 끈기, 자전거 국토종주</h3>", unsafe_allow_html=True)
st.write("")

# 국토종주 여정 스토리와 주행 사진
col_txt, col_img1, col_img2 = st.columns([4, 3, 3])
with col_txt:
    st.markdown("### 633km 자전거 국토종주 및 4대강 종주 완주")
    st.write(
        "9세의 나이로 대한민국 자전거길 국토종주를 당당히 완주했습니다. "
        "인천-서울 구간의 궂은 빗속 주행부터 시작하여, 국토종주 중 최고 난이도로 꼽히는 "
        "백두대간 이화령의 본 오르막 5km 구간을 포기하지 않고 페달을 밟아 마침내 정복했습니다. "
        "어떠한 역경 앞에서도 꺾이지 않는 강력한 도전 정신과 강인한 체력을 보여주는 증거입니다."
    )
with col_img1:
    st.image("KakaoTalk_20260518_195539069_04.jpg", caption="우천 속 인천-서울 구간 주행", use_container_width=True)
with col_img2:
    st.image("KakaoTalk_20260518_195539069_06.jpg", caption="이화령 고개 오르막 주행", use_container_width=True)

st.write("")

# 이화령 정상 및 최종 인증서 사진 레이아웃 (세로형 사진들 균형 맞추기)
col_blank, col_cert1, col_cert2, col_cert3 = st.columns([1, 3, 3, 3])
with col_cert1:
    st.image("KakaoTalk_20260518_195539069_05.jpg", caption="이화령 인증센터(5.0km) 지점", use_container_width=True)
with col_cert2:
    st.image("KakaoTalk_20260518_195539069_07.jpg", caption="백두대간 이화령 정상 도착", use_container_width=True)
with col_cert3:
    # 종주 인증서 사진들을 탭으로 묶어 깔끔하게 노출
    cert_tab1, cert_tab2 = st.tabs(["국토종주 인증", "4대강종주 인증"])
    with cert_tab1:
        st.image("KakaoTalk_20260518_195539069_08.jpg", caption="대한민국 자전거길 국토종주 인증서", use_container_width=True)
    with cert_tab2:
        st.image("KakaoTalk_20260518_195539069_09.jpg", caption="4대강 자전거길 종주 인증서", use_container_width=True)

st.write("---")

# ==========================================
# [ 미래 스페이스 ]
# ==========================================
st.write("")
col_future1, col_future2 = st.columns([1, 8])
with col_future1:
    st.markdown("<h3 style='color: #ccc;'>📍 2026 ~</h3>", unsafe_allow_html=True)
with col_future2:
    st.markdown("<h3 style='color: #ccc;'>다음 도전은 계속됩니다.</h3>", unsafe_allow_html=True)
    st.write("현재 초등학교 3학년인 시원이의 무한한 가능성과 새로운 스토리들이 이곳에 차곡차곡 채워질 예정입니다.")
