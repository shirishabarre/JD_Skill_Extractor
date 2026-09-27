from langchain_core.prompts import PromptTemplate


prompt_template = PromptTemplate(
    input_variables=["job_description"],

    template="""
You are an expert AI information extraction system.

Your task is to identify EVERY DISTINCT JOB ROLE mentioned in the Job Description
and extract ONLY the information that belongs to each specific role.

For EACH job role, extract:

1. job_title
2. skills
3. experience
4. education


========================================
IMPORTANT EXTRACTION RULES
========================================

JOB TITLE:
- Extract only the job title.
- Do not include extra words such as "role", "position", "opening", or "candidate".
- Example:
  "We are hiring for the Data Analyst position"
  → "Data Analyst"


SKILLS:
- Extract individual skills, technologies, tools, frameworks,
  programming languages, platforms, methodologies, and technical
  competencies.
- Each skill must be a short item.
- Do NOT copy complete sentences or paragraphs.
- Do NOT include explanations of what the candidate will do.
- Do NOT include experience or education as skills.
- Remove duplicate skills.
- Example:
  "strong programming skills in Python and experience with TensorFlow"
  → ["Python", "TensorFlow"]


EXPERIENCE:
- Extract ONLY the required experience duration.
- Return ONLY the duration, not the complete sentence.
- Examples:
  "2 to 4 years of experience building machine learning solutions"
  → "2 to 4 years"

  "The candidate should have 3-5 years of professional experience"
  → "3-5 years"

  "Freshers are welcome"
  → "Fresher"

- NEVER include responsibilities, technologies, skills, or explanations
  in the experience field.


EDUCATION:
- Extract only the educational qualification.
- Remove phrases such as "candidates should have",
  "candidates must hold", "is required", "is preferred", etc.
- Example:
  "Candidates should have a Bachelor's degree in Computer Science"
  → "Bachelor's degree in Computer Science"

- Do not include the entire sentence.


========================================
MULTI-JOB RULES
========================================

- Identify every distinct job role mentioned in the input.
- Job titles may appear as headings or naturally inside paragraphs.
- Multiple job titles may be introduced in the same sentence.
- Treat every distinct job role as a separate object.
- Associate information ONLY with the correct job role.
- NEVER combine skills from different roles.
- NEVER combine experience from different roles.
- NEVER combine education from different roles.
- NEVER copy information from one role to another.
- If a field is not explicitly available for a particular role,
  return "not_available".
- Do not invent or assume missing information.
- If only one job role exists, still return it inside the "jobs" list.


========================================
OUTPUT RULES
========================================

- Return ONLY valid JSON.
- No explanation.
- No markdown.
- No extra text.
- Use double quotes.
- No trailing commas.
- Skills must be short individual items.
- Experience must contain ONLY the duration.
- Education must contain ONLY the qualification.
- Job title must contain ONLY the title.


========================================
EXPECTED JSON FORMAT
========================================

{{
  "jobs": [
    {{
      "job_title": "AI Engineer",
      "skills": [
        "Python",
        "TensorFlow",
        "PyTorch"
      ],
      "experience": "2 to 4 years",
      "education": "Bachelor's degree in Computer Science"
    }}
  ]
}}


Job Description:
{job_description}
"""
)
