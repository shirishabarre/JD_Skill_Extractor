import streamlit as st
import json

from prompt import prompt_template
from parser import JobDetails
from model import get_llm_response



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
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #3b82f6, #06b6d4);
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



# ==========================================
# INPUT
# ==========================================

jd_input = st.text_area(
    "📥 Paste Job Description",
    height=250,
    placeholder="Paste the complete Job Description here..."
)

# ==========================================
# BUTTON
# ==========================================

if st.button("✨ Extract Information"):

    if jd_input.strip() == "":
        st.warning("⚠ Please enter Job Description")

    else:

        with st.spinner("🤖 AI is analyzing Job Description..."):

            try:

                # ==========================================
                # CREATE PROMPT
                # ==========================================

                final_prompt = prompt_template.format(
                    job_description=jd_input
                )

                # ==========================================
                # MODEL RESPONSE
                # ==========================================

                response_data = get_llm_response(final_prompt)

                if response_data["success"] is False:

                    st.error(response_data["response"])

                else:

                    result = response_data["response"]

                    # ==========================================
                    # RAW RESPONSE
                    # ==========================================

                    with st.expander("🔍 View Raw AI Response"):

                        st.code(result)

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

                    # ==========================================
                    # EXTRACT JSON
                    # ==========================================

                    start_index = cleaned_result.find("{")
                    end_index = cleaned_result.rfind("}")

                    if start_index == -1 or end_index == -1:

                        raise ValueError(
                            "No valid JSON found in model response"
                        )

                    cleaned_result = cleaned_result[
                        start_index:end_index + 1
                    ]

                    # ==========================================
                    # PARSE JSON
                    # ==========================================

                    parsed_json = json.loads(cleaned_result)

                    # ==========================================
                    # VALIDATE OUTPUT
                    # ==========================================

                    validated_output = JobDetails(**parsed_json)

                    st.success("✅ Extraction Successful")

                    # ==========================================
                    # OUTPUT SECTION
                    # ==========================================

                    col1, col2, col3 = st.columns(3)

                    # Skills
                    with col1:

                        st.markdown("""
                        <div class="card">
                        <h3>🛠 Skills</h3>
                        </div>
                        """, unsafe_allow_html=True)

                        for skill in validated_output.skills:

                            st.write(f"✅ {skill}")

                    # Experience
                    with col2:

                        st.markdown("""
                        <div class="card">
                        <h3>💼 Experience</h3>
                        </div>
                        """, unsafe_allow_html=True)

                        st.write(validated_output.experience)

                    # Education
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
