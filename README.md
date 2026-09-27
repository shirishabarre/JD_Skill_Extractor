# 📄 Job Description Skill Extractor

An AI-powered **Job Description Skill Extractor** that extracts structured hiring information from unstructured Job Descriptions using **Generative AI**.

The application can identify **multiple job roles within a single Job Description** and keeps the skills, experience, and education requirements associated with the correct role.

---

## 🎯 Project Overview

Job descriptions are often written as long paragraphs rather than structured fields. A single document may also contain multiple job openings with different requirements.

For example, one document may contain:

- AI/ML Engineer
- Data Analyst
- Backend Developer

Manually identifying and organizing the requirements for each role can be time-consuming and can lead to information being mixed between different positions.

This project automatically analyzes the Job Description and converts the unstructured content into structured, job-wise JSON.

---

## 💡 Problem Statement

Traditional Job Description processing requires manually identifying:

- Job titles
- Required skills
- Experience requirements
- Educational qualifications

The problem becomes more challenging when a single Job Description contains multiple roles and their requirements are written in different paragraphs.

The system should identify each role and maintain the relationship between the role and its corresponding requirements.

---

## 🎯 Objective

The objective of this project is to build an AI-powered information extraction system that:

1. Identifies every distinct job role in a Job Description.
2. Extracts the skills associated with each role.
3. Extracts the required experience for each role.
4. Extracts the educational qualification for each role.
5. Handles unstructured paragraphs without requiring predefined headings.
6. Prevents requirements from different roles from being mixed.
7. Produces validated structured JSON output.

---

# ✨ Key Features

### 1. Multi-Job Detection

The system can identify multiple job roles from a single Job Description.

Example:

```text
We are hiring for AI/ML Engineer and Data Analyst positions.
```

The system identifies:

```text
AI/ML Engineer
Data Analyst
```

---

### 2. Unstructured JD Processing

The system does not require the Job Description to follow a fixed format.

It can process content such as:

```text
We are looking for talented professionals to join our team.
The AI Engineer role requires 2 to 4 years of experience...
The Data Analyst position requires 1 to 3 years...
```

The job title does not have to appear as:

```text
Job Title:
```

---

### 3. Job-Wise Skill Extraction

Skills are maintained separately for each job.

Example:

```text
AI Engineer
Python
TensorFlow
PyTorch
Machine Learning

Data Analyst
SQL
Excel
Power BI
Data Analysis
```

The system does not combine all skills into one list.

---

### 4. Experience Extraction

The system extracts only the experience duration.

For example:

```text
Input:
The candidate should have 2 to 4 years of experience
building machine learning solutions.

Output:
"2 to 4 years"
```

It does not return the entire sentence as the experience value.

---

### 5. Education Extraction

The system extracts the educational qualification associated with each role.

Example:

```text
Bachelor's degree in Computer Science,
Artificial Intelligence or a related field
```

---

### 6. Missing Information Handling

If information is not available for a particular role, the system returns:

```text
not_available
```

For example:

```json
{
    "job_title": "Frontend Developer",
    "skills": [
        "JavaScript",
        "React",
        "HTML",
        "CSS"
    ],
    "experience": "2 to 4 years",
    "education": "not_available"
}
```

The system does not copy education requirements from another job.

---

### 7. Structured JSON Output

The extracted information is converted into structured JSON and validated before being displayed.

---

# 🧠 Example

## Input

```text
We are expanding our technology team and are looking for an
AI Engineer and a Data Analyst.

The AI Engineer should have 2 to 4 years of experience
building machine learning solutions using Python, TensorFlow
and PyTorch. Candidates should have a Bachelor's degree in
Computer Science, Artificial Intelligence or a related field.

The Data Analyst role requires 1 to 3 years of experience
in SQL-based data analysis, Excel and Power BI. A Bachelor's
degree in Statistics, Mathematics or a related discipline
is preferred.
```

## Output

```json
{
    "jobs": [
        {
            "job_title": "AI Engineer",
            "skills": [
                "Python",
                "TensorFlow",
                "PyTorch",
                "Machine Learning"
            ],
            "experience": "2 to 4 years",
            "education": "Bachelor's degree in Computer Science, Artificial Intelligence or a related field"
        },
        {
            "job_title": "Data Analyst",
            "skills": [
                "SQL",
                "Excel",
                "Power BI",
                "Data Analysis"
            ],
            "experience": "1 to 3 years",
            "education": "Bachelor's degree in Statistics, Mathematics or a related discipline"
        }
    ]
}
```

---

# 🏗️ System Architecture

```text
                 Job Description
                        │
                        ▼
              ┌───────────────────┐
              │   Streamlit UI    │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ LangChain Prompt  │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │     Groq LLM      │
              └─────────┬─────────┘
                        │
                        ▼
             Multi-Job JSON Output
                        │
                        ▼
              ┌───────────────────┐
              │   JSON Parsing    │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Pydantic Validate │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Streamlit Output  │
              └───────────────────┘
                        │
                        ▼
              Job-wise Information
```

---

# 🔄 Project Workflow

### Step 1 — User Input

The user pastes an unstructured Job Description into the Streamlit application.

### Step 2 — Prompt Processing

The Job Description is passed to a LangChain `PromptTemplate`.

The prompt instructs the LLM to:

- Detect every job role.
- Extract role-specific skills.
- Extract experience duration.
- Extract education.
- Avoid mixing requirements between roles.
- Return `not_available` when information is missing.
- Return only valid JSON.

### Step 3 — LLM Processing

The prompt is sent to the Groq-hosted LLM.

### Step 4 — JSON Extraction

The model response is cleaned and converted into a Python JSON object.

### Step 5 — Pydantic Validation

The extracted response is validated against the defined Pydantic schema.

### Step 6 — Job-Wise Display

The Streamlit application displays each detected job separately.

### Step 7 — Structured JSON

The complete validated result is displayed as formatted JSON.

---

# 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| **Python** | Core application development |
| **Streamlit** | Web interface |
| **LangChain** | Prompt management |
| **Groq** | LLM inference |
| **LLM** | Job role and requirement extraction |
| **Prompt Engineering** | Controlled information extraction |
| **Pydantic** | Structured output validation |
| **JSON** | Structured data representation |
| **Langfuse** | LLM observability |
| **python-dotenv** | Environment variable management |

---

# 📁 Project Structure

```text
JD-Skill-Extractor/
│
├── app.py
├── model.py
├── prompt.py
├── parser.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### `app.py`

Responsible for:

- Streamlit UI
- Job Description input
- Calling the extraction pipeline
- JSON processing
- Pydantic validation
- Job-wise result display
- Structured JSON display

### `prompt.py`

Contains the LangChain prompt responsible for:

- Multi-job detection
- Skill extraction
- Experience extraction
- Education extraction
- Role-specific requirement association
- Output formatting instructions

### `model.py`

Responsible for:

- Groq LLM configuration
- LLM invocation
- Langfuse observability
- Environment variable loading

### `parser.py`

Contains the Pydantic models used to validate the structured output.

```python
class JobDetails(BaseModel):
    job_title: str
    skills: List[str]
    experience: str
    education: str


class JobExtraction(BaseModel):
    jobs: List[JobDetails]
```

### `requirements.txt`

Contains the Python dependencies required to run the application.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/JD-Skill-Extractor.git
```

```bash
cd JD-Skill-Extractor
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key

LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

⚠️ **Never upload `.env` or API keys to GitHub.**

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🧪 Testing Scenarios

The application should be tested with:

### Test 1 — Single Job

One Job Description containing one role.

### Test 2 — Multiple Jobs

One document containing:

```text
AI Engineer
Data Analyst
Backend Developer
```

### Test 3 — Unstructured Roles

Job titles mentioned naturally inside paragraphs.

### Test 4 — Missing Education

A role without an education requirement should return:

```text
not_available
```

### Test 5 — Missing Experience

A role without an experience requirement should return:

```text
not_available
```

### Test 6 — Shared Skills

If two different roles both require Python, Python should appear under both roles.

### Test 7 — Different Requirements

Skills, experience and education should never be transferred from one role to another.

### Test 8 — Multiple Roles in Introduction

Example:

```text
We are hiring for AI/ML Engineer, Data Analyst
and Backend Developer positions.
```

The system should detect all three roles even if their detailed requirements appear later in separate paragraphs.

---

# 🧩 Important Extraction Rules

The project follows these core rules:

### Rule 1 — Every role is independent

Each job gets its own:

```text
Job Title
Skills
Experience
Education
```

### Rule 2 — No requirement mixing

Requirements belonging to one role must never be assigned to another role.

### Rule 3 — Concise experience

The experience field contains only the duration.

```text
2 to 4 years
```

not:

```text
2 to 4 years of experience developing machine learning solutions using Python...
```

### Rule 4 — Individual skills

Skills are extracted as individual items.

```text
Python
TensorFlow
Machine Learning
```

rather than copying entire sentences.

### Rule 5 — No hallucination

The system does not assume missing information.

Missing fields return:

```text
not_available
```

---

# 💼 Business Use Cases

The project can be used for:

- Recruitment automation
- Job Description analysis
- HR information extraction
- Job requirement standardization
- Resume-job matching
- Candidate screening
- Skill-gap analysis
- Recruitment analytics
- Job market analysis

---

# 🚀 Future Enhancements

The current project focuses on **Phase 1: Multi-Job Extraction**.

Future phases can include:

### Phase 2 — Advanced JD Analysis

- Required vs Preferred skills
- Responsibilities extraction
- Job seniority detection
- Job location
- Employment type
- Job summary
- Skill categorization

### Phase 3 — Resume Matching

Allow users to upload a resume and compare it against a selected job.

Example:

```text
Overall Match: 82%

Matched Skills
✓ Python
✓ SQL
✓ Machine Learning

Missing Skills
✗ AWS
✗ Docker
```

### Phase 4 — Skill Gap Analysis

Identify the skills a candidate needs to develop for a particular role.

### Phase 5 — Recruitment Dashboard

Add:

- Job history
- Candidate matching
- Match scores
- Skill analytics
- CSV/Excel export
- PDF reports

---

# 📌 Project Highlights

- Built an end-to-end **Generative AI information extraction application**
- Handles **multiple job roles from a single unstructured Job Description**
- Uses **prompt engineering** for controlled extraction
- Maintains role-specific relationships between requirements
- Uses **Pydantic for structured validation**
- Uses **Groq for LLM inference**
- Uses **LangChain for prompt management**
- Uses **Langfuse for LLM observability**
- Uses **Streamlit for the interactive UI**
- Handles missing information using `not_available`
- Produces clean, structured JSON output

---

# 👨‍💻 Author

**Shirisha Barre**

B.Tech — Computer Science & Engineering (AI & ML)

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Generative AI
- Large Language Models
- RAG
- AI Agents
- Python
