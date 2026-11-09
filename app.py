
import streamlit as st

st.set_page_config(
    page_title="LUMORA AI",
    page_icon="💡",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.main {
    background-color: #f5f6fc;
}
[data-testid="stSidebar"] {
    background-color: #171b35;
}
[data-testid="stSidebar"] * {
    color: white;
}
.hero {
    padding: 30px;
    border-radius: 15px;
    background: linear-gradient(120deg, #252b59, #7654b5);
    color: white;
}
.feature {
    padding: 22px;
    border-radius: 12px;
    background: white;
    border: 1px solid #e5e7f0;
    min-height: 130px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("💡 LUMORA AI")
st.sidebar.caption("Intelligent Learning Assistant")

page = st.sidebar.radio(
    "NAVIGATION",
    ["Dashboard", "AI Notes", "Quiz Generator", "Topic Explainer"]
)

st.sidebar.divider()
st.sidebar.caption("Learn smarter. Every day.")

# Dashboard
if page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>Welcome to LUMORA AI ✨</h1>
        <p>Your personal intelligent learning companion.</p>
        <p>Learn • Understand • Practice • Improve</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("Your Learning Workspace")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="feature"><h3>📚 AI Notes</h3>'
            '<p>Create simple study notes.</p></div>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="feature"><h3>📝 Quiz Generator</h3>'
            '<p>Practice with questions.</p></div>',
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="feature"><h3>🧠 Topic Explainer</h3>'
            '<p>Understand difficult topics.</p></div>',
            unsafe_allow_html=True
        )

    st.write("")
    st.subheader("Learning Overview")

    a, b, c = st.columns(3)
    a.metric("Learning Tools", "3")
    b.metric("Platform", "LUMORA AI")
    c.metric("Status", "Ready")

# Other pages
elif page == "AI Notes":
    st.title("📚 AI Notes Generator")
    st.write("Create easy-to-understand study notes.")

elif page == "Quiz Generator":
    st.title("📝 AI Quiz Generator")
    st.write("Prepare yourself with practice questions.")

elif page == "Topic Explainer":
    st.title("🧠 AI Topic Explainer")
    st.write("Learn difficult concepts in simple English.")
