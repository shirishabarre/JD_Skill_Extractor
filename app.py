import streamlit as st
import json

from prompt import prompt_template
from parser import JobDetails
from model import get_llm_response

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI JD Skill Extractor",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

h1 {
    color: #38bdf8;
    text-align: center;
    font-size: 52px;
    font-weight: bold;
}

.stTextArea textarea {
    background-color: #1e293b;
    color: white;
    border-radius: 15px;
    border: 2px solid #38bdf8;
    font-size: 16px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #06b6d4, #3b82f6);
    color: white;
    font-size: 20px;
    border-radius: 15px;
    height: 3.5em;
    border: none;
    font-weight: bold;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 18px;
    margin-top: 20px;
    box-shadow: 0px 0px 18px rgba(56,189,248,0.2);
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<h1>📄 AI Job Description Skill Extractor</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h3>🚀 Intelligent Recruitment AI System</h3>

<p>
Extract Skills, Experience, and Education from Job Descriptions using AI.
</p>



</div>
""", unsafe_allow_html=True)

# ==========================================
# INPUT
# ==========================================

jd_input = st.text_area(
    "Paste Job Description",
    height=250
)

# ==========================================
# BUTTON
# ==========================================

if st.button("✨ Extract Information"):

    if jd_input.strip() == "":
        st.warning("Please enter Job Description")

    else:

        with st.spinner("AI is analyzing Job Description..."):

            try:

                # Prompt
                final_prompt = prompt_template.format(
                    job_description=jd_input
                )

                # Model Response
                response_data = get_llm_response(final_prompt)

                if response_data["success"] is False:

                    st.error(response_data["response"])

                else:

                    result = response_data["response"]

                    # ==========================================
                    # CLEAN RESPONSE
                    # ==========================================

                    cleaned_result = result.strip()

                    cleaned_result = cleaned_result.replace(
                        "```json",
                        ""
                    )

                    cleaned_result = cleaned_result.replace(
                        "```",
                        ""
                    )

                    cleaned_result = cleaned_result.strip()

                    # Extract JSON safely
                    start_index = cleaned_result.find("{")
                    end_index = cleaned_result.rfind("}")

                    cleaned_result = cleaned_result[
                        start_index:end_index + 1
                    ]

                    # Parse JSON
                    parsed_json = json.loads(cleaned_result)

                    # Validate
                    validated_output = JobDetails(**parsed_json)

                    st.success("✅ Extraction Successful")

                    # ==========================================
                    # OUTPUT
                    # ==========================================

                    col1, col2, col3 = st.columns(3)

                    with col1:

                        st.markdown("""
                        <div class="card">
                        <h3>🛠 Skills</h3>
                        </div>
                        """, unsafe_allow_html=True)

                        for skill in validated_output.skills:
                            st.write(f"✅ {skill}")

                    with col2:

                        st.markdown("""
                        <div class="card">
                        <h3>💼 Experience</h3>
                        </div>
                        """, unsafe_allow_html=True)

                        st.write(validated_output.experience)

                    with col3:

                        st.markdown("""
                        <div class="card">
                        <h3>🎓 Education</h3>
                        </div>
                        """, unsafe_allow_html=True)

                        st.write(validated_output.education)

                    # ==========================================
                    # JSON OUTPUT
                    # ==========================================

                    st.markdown("""
                    <div class="card">
                    <h3>📦 Structured JSON Output</h3>
                    </div>
                    """, unsafe_allow_html=True)

                    st.json(validated_output.model_dump())

            except Exception as e:

                st.error(f"❌ Error: {str(e)}")
