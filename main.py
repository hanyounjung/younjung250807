import streamlit as st

st.set_page_config(page_title="MBTI 기반 진로 추천", page_icon="🧭", layout="centered")

# 타이틀
st.title("🧭 MBTI 기반 진로 추천 서비스")
st.markdown("안녕하세요! 😊 당신의 MBTI에 맞는 진로를 추천해드릴게요. \
정확한 선택을 통해 나에게 꼭 맞는 미래를 찾아보세요! 💼💡")

# MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox("📌 나의 MBTI를 선택하세요:", mbti_types)

# 추천 진로 데이터
career_recommendations = {
    "INTJ": {
        "career": "전략 컨설턴트 🧠 / 데이터 과학자 📊",
        "reason": "논리적 사고와 미래지향적인 비전을 가진 당신! 세상을 바꾸는 전략을 구상하고 싶다면 이 분야가 딱이에요."
    },
    "INTP": {
        "career": "AI 연구원 🤖 / 발명가 🔬",
        "reason": "끊임없는 호기심과 분석력으로 무장한 당신! 세상에 없던 것을 창조하는 직업이 잘 어울려요."
    },
    "ENTJ": {
        "career": "CEO 👩‍💼 / 기획자 📈",
        "reason": "리더십이 탁월하고 목표 지향적인 ENTJ! 팀을 이끌고 변화의 중심에 서는 걸 좋아하죠."
    },
    "ENTP": {
        "career": "창업가 🚀 / 광고기획자 🎨",
        "reason": "톡톡 튀는 아이디어와 말솜씨를 가진 ENTP! 변화를 주도하고 새로운 걸 즐기죠."
    },
    "INFJ": {
        "career": "상담심리사 🧘 / 사회운동가 🕊️",
        "reason": "깊은 공감력과 이상주의를 가진 INFJ. 사람들에게 긍정적인 변화를 이끌어내는 일을 잘 해요."
    },
    "INFP": {
        "career": "작가 ✍️ / 일러스트레이터 🎨",
        "reason": "섬세한 감성과 상상력 풍부한 INFP는 감정을 표현하는 예술 분야에서 빛나요!"
    },
    "ENFJ": {
        "career": "교사 👩‍🏫 / 인사담당자 🧑‍💼",
        "reason": "사람들을 이끌고 배려하는 데 천부적인 ENFJ는 교육과 조직문화 분야에 적합해요."
    },
    "ENFP": {
        "career": "콘텐츠 크리에이터 📹 / 이벤트 플래너 🎉",
        "reason": "활기찬 에너지와 창의력이 넘치는 ENFP는 즐거움과 열정을 전달하는 일을 좋아해요."
    },
    "ISTJ": {
        "career": "공무원 🏛️ / 회계사 📑",
        "reason": "책임감 있고 체계적인 ISTJ는 규칙과 정확성이 필요한 분야에 강해요."
    },
    "ISFJ": {
        "career": "간호사 🩺 / 사회복지사 🤝",
        "reason": "헌신적이고 배려심 깊은 ISFJ는 남을 돌보는 직업에서 큰 만족을 느껴요."
    },
    "ESTJ": {
        "career": "경영 관리자 🏢 / 군인 🪖",
        "reason": "현실적이고 조직적인 ESTJ는 명확한 구조와 리더십이 요구되는 분야에서 잘해요."
    },
    "ESFJ": {
        "career": "호텔리어 🏨 / 간호조무사 💉",
        "reason": "사람들과 잘 어울리고 서비스 정신이 뛰어난 ESFJ는 대인관계가 중심인 직업이 잘 맞아요."
    },
    "ISTP": {
        "career": "기계공학자 ⚙️ / 자동차 정비사 🚗",
        "reason": "도구 다루기에 능하고 문제 해결에 강한 ISTP는 손으로 배우는 직업에 재능이 있어요."
    },
    "ISFP": {
        "career": "플로리스트 🌷 / 패션 디자이너 👗",
        "reason": "감각적이고 조용한 예술가 타입인 ISFP는 미적 감각을 살리는 분야에 어울려요."
    },
    "ESTP": {
        "career": "스포츠 트레이너 🏋️ / 경찰관 👮",
        "reason": "빠른 판단과 활동적인 성향의 ESTP는 현장에서 뛰는 직업이 좋아요!"
    },
    "ESFP": {
        "career": "배우 🎭 / 쇼호스트 🎤",
        "reason": "에너지 넘치고 주목받는 걸 좋아하는 ESFP는 무대 위의 스타가 될 준비가 되어 있어요!"
    },
}

if selected_mbti:
    st.markdown("## 🎯 추천 진로")
    st.success(f"**{career_recommendations[selected_mbti]['career']}**")
    st.markdo
