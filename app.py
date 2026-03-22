import streamlit as st

# إعدادات واجهة البرنامج
st.set_page_config(page_title="Nona-Glow", page_icon="✨")

# التصميم
st.title("✨ نونا جلو | Nona-Glow")
st.subheader("دليلك الذكي للرشاقة والصيام المتقطع")

# مدخلات المستخدم
with st.form("user_data"):
    name = st.text_input("ما هو اسمكِ؟")
    age = st.number_input("العمر", 10, 80, 20)
    gender = st.selectbox("الجنس", ["أنثى", "ذكر"])
    weight = st.number_input("الوزن (كجم)", 30, 200, 70)
    height = st.number_input("الطول (سم)", 100, 220, 160)
    submit = st.form_submit_button("احسبي نتيجتي الآن! 🔥")

if submit:
    # المعادلات
    if gender == "أنثى":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    
    target = (bmr * 1.2) - 500
    water = round(weight * 0.035, 1)

    st.balloons()
    st.success(f"أهلاً يا {name}! إليكِ خطتك الشخصية:")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("حرقك الأساسي", f"{int(bmr)}")
    c2.metric("هدف السعرات", f"{int(target)}")
    c3.metric("لتر ماء يومياً", f"{water}")
    
    st.info("💡 نصيحة نونا: ابدئي صيام 16:8، واشربي كوب ماء قبل كل وجبة!")
