import streamlit as st
import json
import html

from prompt import prompt_template
from parser import JobExtraction
from model import get_llm_response


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="JD Skill Extractor",
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
    color: white;
}

.output-text {
    color: #000000 !important;
    font-size: 17px;
    font-weight: 500;
}

.job-title {
    color: #38bdf8 !important;
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 10px;
}

.json-output {
    color: white !important;
    background-color: #0f172a;
    padding: 15px;
    border-radius: 10px;
    font-size: 15px;
    white-space: pre-wrap;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<h1>📄 AI Job Description Skill Extractor</h1>
""", unsafe_allow_html=True)

st.markdown(
    """
    <p style="text-align:center; color:white; font-size:18px;">
    Extract job-wise skills, experience and education from single or multiple roles.
    </p>
    """,
    unsafe_allow_html=True
)


# ==========================================
# INPUT
# ==========================================

jd_input = st.text_area(
    "📥 Paste Job Description",
    height=300,
    placeholder="Paste one or more job descriptions here..."
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

                # ==========================================
                # PROMPT
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
                    # CLEAN RESPONSE
                    # ==========================================

                    cleaned_result = result.strip()

                    cleaned_result = cleaned_result.replace(
                        "```json", ""
                    )

                    cleaned_result = cleaned_result.replace(
                        "```", ""
                    )

                    cleaned_result = cleaned_result.strip()

                    # Find JSON object safely
                    start_index = cleaned_result.find("{")
                    end_index = cleaned_result.rfind("}")

                    if start_index == -1 or end_index == -1:
                        raise ValueError(
                            "The model did not return a valid JSON object."
                        )

                    cleaned_result = cleaned_result[
                        start_index:end_index + 1
                    ]

                    # ==========================================
                    # PARSE JSON
                    # ==========================================

                    parsed_json = json.loads(cleaned_result)

                    # ==========================================
                    # PYDANTIC VALIDATION
                    # ==========================================

                    validated_output = JobExtraction(**parsed_json)

                    st.success(
                        f"✅ Extraction Successful — "
                        f"{len(validated_output.jobs)} job role(s) detected"
                    )

                    # ==========================================
                    # DISPLAY EACH JOB
                    # ==========================================

                    for index, job in enumerate(
                        validated_output.jobs,
                        start=1
                    ):

                        st.markdown(
                            f"""
                            <div class="card">
                                <div class="job-title">
                                    💼 {index}. {html.escape(job.job_title)}
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        col1, col2, col3 = st.columns(3)

                        with col1:

                            st.markdown(
                                """
                                <div class="card">
                                    <h3 style="color:white;">🛠 Skills</h3>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                            for skill in job.skills:

                                st.markdown(
                                    f'<div class="output-text">✅ '
                                    f'{html.escape(skill)}</div>',
                                    unsafe_allow_html=True
                                )

                        with col2:

                            st.markdown(
                                """
                                <div class="card">
                                    <h3 style="color:white;">💼 Experience</h3>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                            st.markdown(
                                f'<div class="output-text">'
                                f'{html.escape(job.experience)}</div>',
                                unsafe_allow_html=True
                            )

                        with col3:

                            st.markdown(
                                """
                                <div class="card">
                                    <h3 style="color:white;">🎓 Education</h3>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                            st.markdown(
                                f'<div class="output-text">'
                                f'{html.escape(job.education)}</div>',
                                unsafe_allow_html=True
                            )

                    # ==========================================
                    # JSON OUTPUT
                    # ==========================================

                    st.markdown(
                        """
                        <div class="card">
                            <h3 style="color:White;">
                                📦 Structured JSON Output
                            </h3>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    json_data = json.dumps(
                         validated_output.model_dump(),
                         indent=4,
                         ensure_ascii=False
                         )
                    st.code(
                        json_data,
                        language="json"
                        )

            except json.JSONDecodeError:
                st.error(
                    "❌ The model returned invalid JSON. "
                    "Please try again."
                )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
