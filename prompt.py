from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["jd"],
    template="""
You are an intelligent information extraction system.

Extract the following details from the given Job Description:

1. Skills
2. Experience
3. Education

Rules:
- Extract only from the given text
- Do not generate extra information
- Do not assume anything
- If any field is missing return "not_available"
- Return ONLY valid JSON
- No explanation text

Expected JSON Format:

{{
    "skills": ["skill1", "skill2"],
    "experience": "value",
    "education": "value"
}}

Job Description:
{jd}
"""
)