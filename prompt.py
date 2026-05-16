from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(

    input_variables=["job_description"],

    template="""
You are an expert AI information extraction system.

Extract ONLY:

1. skills
2. experience
3. education

STRICT RULES:
- Return ONLY valid JSON
- No explanation
- No markdown
- No extra text
- Use double quotes only
- No trailing commas
- Do not hallucinate
- If any value missing use "not_available"

Expected JSON Format:

{{
  "skills": [],
  "experience": "",
  "education": ""
}}

Job Description:
{job_description}
"""
)