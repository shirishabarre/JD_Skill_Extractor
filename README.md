# 📄 Job Description Skill Extractor

An AI-powered **Job Description Skill Extractor** that automatically extracts **skills, experience, and education requirements** from unstructured Job Descriptions and presents them in a structured JSON format.

The application uses an LLM through **Groq**, **LangChain PromptTemplate** for prompt management, **Pydantic** for structured output validation, and **Streamlit** for the user interface.

---

## 🚀 Project Overview

Job Descriptions often contain important hiring requirements inside long paragraphs, making it time-consuming to manually identify the required skills, experience, and educational qualifications.

This project solves that problem by allowing a user to paste a Job Description into a simple web interface. The application sends the Job Description to an LLM with a structured extraction prompt and returns:

* 🛠️ Required Skills
* 💼 Required Experience
* 🎓 Required Education
* 📦 Structured JSON Output

---

## 🎯 Objective

The main objective of this project is to automatically convert an **unstructured Job Description into structured hiring information**.

### Input

```text
We are looking for a Python Developer with 2 years
of experience. The candidate should have knowledge
of Python, SQL and Machine Learning.

A Bachelor's degree in Computer Science or a
related field is preferred.
```

### Output

```json
{
    "skills": [
        "Python",
        "SQL",
        "Machine Learning"
    ],
    "experience": "2 years",
    "education": "Bachelor's degree in Computer Science or related field"
}
```

---

## ✨ Features

* 📄 Paste any Job Description
* 🤖 AI-powered information extraction
* 🛠️ Extract required technical skills
* 💼 Extract required experience
* 🎓 Extract educational qualifications
* 📦 Generate structured JSON output
* ✅ Validate output using Pydantic
* 🚫 Reduce hallucination using strict prompt instructions
* 📊 LLM observability using Langfuse
* 🎨 User-friendly Streamlit interface
* ⚡ Fast LLM inference using Groq

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Streamlit UI      │
                    │      app.py         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ LangChain Prompt    │
                    │    prompt.py        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Groq LLM        │
                    │  LLM Processing     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    JSON Response    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  JSON Parsing       │
                    │      app.py         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Pydantic Validation │
                    │     parser.py       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Structured Output   │
                    │ Skills / Experience │
                    │ / Education / JSON  │
                    └─────────────────────┘

                 ┌───────────────────────┐
                 │       Langfuse        │
                 │ LLM Observability     │
                 └───────────────────────┘
```

---

## 🔄 Workflow

The application follows this workflow:

### 1. User Input

The user pastes a Job Description into the Streamlit interface.

### 2. Prompt Creation

The Job Description is inserted into a predefined LangChain `PromptTemplate`.

The prompt instructs the LLM to extract only:

```text
1. Skills
2. Experience
3. Education
```

It also instructs the model to:

* Return only valid JSON
* Avoid explanations
* Avoid Markdown
* Avoid hallucination
* Use `not_available` when information is missing

### 3. LLM Processing

The formatted prompt is sent to the Groq-hosted LLM.

### 4. JSON Processing

The application cleans the model response and extracts the JSON object.

### 5. Pydantic Validation

The JSON response is validated against the following schema:

```python
class JobDetails(BaseModel):
    skills: List[str]
    experience: str
    education: str
```

### 6. Display Results

The validated information is displayed in the Streamlit application.

---

## 🛠️ Tech Stack

| Technology             | Purpose                                      |
| ---------------------- | -------------------------------------------- |
| **Python**             | Core programming language                    |
| **Streamlit**          | Web UI                                       |
| **LangChain**          | Prompt management                            |
| **Groq**               | LLM inference                                |
| **LLM**                | Job Description understanding and extraction |
| **Prompt Engineering** | Controlled information extraction            |
| **Pydantic**           | Output validation                            |
| **JSON**               | Structured output format                     |
| **Langfuse**           | LLM observability and tracing                |
| **python-dotenv**      | Environment variable management              |

---

## 📁 Project Structure

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

* Streamlit interface
* User input
* Calling the extraction pipeline
* JSON parsing
* Pydantic validation
* Displaying results

### `model.py`

Responsible for:

* Groq LLM configuration
* LLM invocation
* Langfuse observability
* API configuration

### `prompt.py`

Contains the LangChain `PromptTemplate` used to instruct the LLM.

### `parser.py`

Contains the Pydantic model used to validate the extracted information.

### `requirements.txt`

Contains the Python dependencies required to run the project.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/JD-Skill-Extractor.git
```

```bash
cd JD-Skill-Extractor
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key

LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

> ⚠️ Never upload your `.env` file or API keys to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Example

### Input

```text
Job Title: AI/ML Engineer

We are looking for an AI/ML Engineer with 1-2 years
of experience in Machine Learning and Artificial
Intelligence.

The candidate should have strong programming skills
in Python and SQL. Knowledge of Machine Learning,
Deep Learning, NLP and Generative AI is required.

Experience with LLMs, Prompt Engineering, RAG,
embeddings and vector databases is preferred.

Bachelor's degree in Computer Science, Information
Technology, Artificial Intelligence or a related field
is required.
```

### Extracted Skills

```text
Python
SQL
Machine Learning
Deep Learning
NLP
Generative AI
LLMs
Prompt Engineering
RAG
Embeddings
Vector Databases
```

### Experience

```text
1-2 years
```

### Education

```text
Bachelor's degree in Computer Science, Information
Technology, Artificial Intelligence or related field
```

### Structured JSON

```json
{
    "skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Generative AI",
        "LLMs",
        "Prompt Engineering",
        "RAG",
        "Embeddings",
        "Vector Databases"
    ],
    "experience": "1-2 years",
    "education": "Bachelor's degree in Computer Science, Information Technology, Artificial Intelligence or related field"
}
```

---

## 🧠 Key Technical Concepts

### Prompt Engineering

The project uses a strict extraction prompt to control the LLM response.

Instead of allowing the LLM to generate a conversational answer, the prompt defines the exact fields and expected JSON structure.

### Structured Output

The application converts unstructured Job Description text into structured data:

```text
Unstructured JD
       ↓
     LLM
       ↓
Structured JSON
```

### Pydantic Validation

Pydantic ensures that the extracted response follows the expected schema before displaying it to the user.

### LLM Observability

Langfuse is integrated to provide visibility into LLM interactions and help with debugging and monitoring.

---

## 💡 Use Cases

This application can be useful for:

* 👨‍💼 Recruiters
* 🏢 HR teams
* 📄 Resume screening systems
* 🔎 Job matching applications
* 🤖 Recruitment automation
* 📊 Job market analysis
* 🧑‍💻 Candidate-job matching systems

---

## 🔮 Future Enhancements

Potential future improvements include:

* Resume vs Job Description matching
* Candidate ranking
* Multiple Job Description comparison
* Export results to CSV/Excel
* Database storage for extracted JDs
* Salary and location extraction
* Semantic skill matching

---

## 📌 Project Highlights

* Built an end-to-end **LLM-powered information extraction application**
* Implemented **prompt engineering** for controlled output
* Used **structured JSON generation**
* Implemented **Pydantic validation**
* Integrated **Groq LLM inference**
* Added **Langfuse observability**
* Developed an interactive **Streamlit UI**
* Designed the system to handle missing information without hallucinating

---

## 👨‍💻 Author

**Shirisha Barre**

B.Tech – Computer Science & Engineering (AI & ML)

### Areas of Interest

* Artificial Intelligence
* Machine Learning
* Generative AI
* Large Language Models
* RAG
* AI Agents
* Python

---

## ⭐ If you find this project useful

Feel free to star ⭐ the repository and explore the project.
