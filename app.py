import streamlit as st

# 1. 페이지 전환 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to_page(page_name):
    st.session_state.page = page_name

# 2. 기본 화면 설정
st.set_page_config(page_title="순천대 틈새시간 요정", page_icon="🧚‍♂️", layout="centered")

# ==========================================
# [Frame 1] 홈 - 대시보드 화면
# ==========================================
if st.session_state.page == 'home':
    st.write("👋 안녕하세요!")
    st.title("순천대 틈새시간 요정 🧚‍♂️")
    st.caption("공식 캠퍼스 맵 연동 서비스")
    
    st.info("🗺️ 캠퍼스 실시간 혼잡도: 여유 (3D 맵 뷰어 준비 중)")
    
    st.markdown("---")
    st.text_input("🔍 어떤 공간을 찾으시나요?", placeholder="예: 조용한 곳, 카페...")
    st.write("단축 태그: `#도서관` `#학생회관` `#조용한곳`")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("내 주변 최적의 휴식처 찾기 ➡️", use_container_width=True, type="primary"):
        go_to_page('filter')

# ==========================================
# [Frame 2] 맞춤 조건 상세 설정 화면
# ==========================================
elif st.session_state.page == 'filter':
    if st.button("⬅️ 뒤로 가기"):
        go_to_page('home')
        
    st.title("맞춤 조건 상세 설정")
    st.markdown("---")
    
    st.session_state.time_left = st.radio("⏱️ 남은 공강 시간", ["1시간 미만", "1시간 이상"], horizontal=True)
    st.session_state.vibe = st.radio("✨ 원하는 분위기", ["💻 노트북/과제", "🛌 수면/휴식", "🗣️ 대화/소통"])
    
    st.toggle("🔌 콘센트 필수", value=True)
    st.toggle("❄️ 냉난방 완비", value=True)
    st.text_input("추가로 필요한 점을 적어주세요", placeholder="예: 팀플 공간")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("맞춤 장소 추천받기", use_container_width=True, type="primary"):
        go_to_page('result')

# ==========================================
# [Frame 3] 추천 결과 상세 화면 (100% 실제 데이터)
# ==========================================
elif st.session_state.page == 'result':
    if st.button("⬅️ 뒤로 가기"):
        go_to_page('filter')
        
    st.title("추천 결과")
    st.success("✨ 현재 가장 완벽한 1순위 추천 공간입니다!")
    
    time = st.session_state.time_left
    vibe = st.session_state.vibe
    
    # 조건에 따른 100% 실제 장소 매칭 로직
    if time == "1시간 미만" and vibe == "💻 노트북/과제":
        title = "C1 도서관 2층 카페형 열람실 및 노트북 존"
        tags = "`#잔잔함` `#음악` `#노트북`"
        desc = "잔잔하게 노트북을 하거나 음악을 들으며 공강을 때우고 싶을 때 유용합니다."
    elif time == "1시간 미만" and vibe == "🛌 수면/휴식":
        title = "C1 도서관 2층 We라운지"
        tags = "`#탁트인_개방형` `#발권없이_자유롭게`"
        desc = "탁 트인 개방형 인프라로 조성된 자유석 휴게 공간입니다. 발권 없이 짧은 공강에 머무르기 좋습니다."
    elif time == "1시간 미만" and vibe == "🗣️ 대화/소통":
        title = "E1 학생회관 1층 이마트24 편의점 옆 휴게실"
        tags = "`#오픈형쉼터` `#간식` `#담소`"
        desc = "간식을 먹으며 편하게 담소를 나눌 수 있는 오픈형 쉼터입니다."
    elif time == "1시간 이상" and vibe == "💻 노트북/과제":
        title = "E8 인문예술대학 1층 스터디카페"
        tags = "`#자연채광` `#바_좌석` `#넓은테이블`"
        desc = "자연 채광이 좋고 창밖을 바라보는 바 좌석이 있어 혼자 조용히 과제를 하기에 아주 좋습니다."
    elif time == "1시간 이상" and vibe == "🛌 수면/휴식":
        title = "E1 학생회관 2층 남/여학생 휴게실"
        tags = "`#침대구비` `#깊은피로` `#아늑함`"
        desc = "소파와 테이블뿐만 아니라 침대까지 구비되어 있어 깊은 피로를 풀거나 잠을 청하기 좋습니다."
    else: # 1시간 이상 + 대화/소통
        title = "A1 대학본부 1층 라운지 & 이디야커피"
        tags = "`#보드게임` `#가벼운게임` `#동기들과`"
        desc = "보드게임 등이 비치되어 있어 동기들과 가벼운 게임을 하거나 대화를 나누며 공강을 보내기 적합합니다."

    st.markdown(f"### 🏢 {title}")
    st.write(tags)
    st.write(desc)
    st.write("👥 현재 여유 🔊 소음: 보통")

    if st.button("📍 빠른 길 안내", use_container_width=True):
        st.info("🗺️ 실시간 캠퍼스 맵을 불러오는 중입니다...")

    st.markdown("---")
    st.markdown("#### 다른 추천 공간")
    
    # 2순위, 3순위 고정 추천 공간 (실제 데이터)
    col1, col2 = st.columns(2)
    with col1:
        st.info("**C1 도서관 3층 301호 상상라운지**\n\n대형 미디어월 감상이 가능한 복합문화공간")
    with col2:
        st.warning("**E1 학생회관 4층 글로컬라운지**\n\n오전 9시~오후 6시 운영 스터디 카페 분위기")
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 다른 조건으로 다시 찾기", use_container_width=True):
        go_to_page('filter')