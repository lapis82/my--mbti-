import streamlit as st

st.title("MBTI 클래식 음악 추천기")

mbti = st.selectbox(
    "당신의 MBTI를 선택하세요",
    ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
     "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"]
)

music = {
    "INTJ": "베토벤 - 교향곡 5번 '운명'",
    "INTP": "바흐 - 골드베르크 변주곡",
    "ENTJ": "베토벤 - 교향곡 3번 '영웅'",
    "ENTP": "로시니 - 윌리엄 텔 서곡",
    "INFJ": "드뷔시 - 달빛",
    "INFP": "쇼팽 - 녹턴 Op.9 No.2",
    "ENFJ": "베토벤 - 교향곡 9번 '합창'",
    "ENFP": "비발디 - 사계 중 봄",
    "ISTJ": "바흐 - 브란덴부르크 협주곡 3번",
    "ISFJ": "슈베르트 - 아베마리아",
    "ESTJ": "헨델 - 왕궁의 불꽃놀이",
    "ESFJ": "요한 슈트라우스 2세 - 아름답고 푸른 도나우",
    "ISTP": "파가니니 - 카프리스 24번",
    "ISFP": "라벨 - 물의 유희",
    "ESTP": "비제 - 카르멘 서곡",
    "ESFP": "요한 슈트라우스 2세 - 라데츠키 행진곡",
}

st.write("추천 음악:", music[mbti])
