import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langfuse import Langfuse

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

# ==========================================
# API KEYS
# ==========================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

LANGFUSE_PUBLIC_KEY = os.getenv(
    "LANGFUSE_PUBLIC_KEY"
)

LANGFUSE_SECRET_KEY = os.getenv(
    "LANGFUSE_SECRET_KEY"
)

LANGFUSE_HOST = os.getenv(
    "LANGFUSE_HOST"
)

# ==========================================
# LANGFUSE
# ==========================================

langfuse = Langfuse(
    public_key=LANGFUSE_PUBLIC_KEY,
    secret_key=LANGFUSE_SECRET_KEY,
    host=LANGFUSE_HOST
)

# ==========================================
# MODEL
# ==========================================

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

# ==========================================
# FUNCTION
# ==========================================

def get_llm_response(prompt):

    try:

        # LLM Call
        response = llm.invoke(prompt)

        result = response.content

        # Langfuse Logging
        langfuse.score(
            name="jd_skill_extractor",
            value=1,
            comment=result
        )

        langfuse.flush()

        return {
            "success": True,
            "response": result
        }

    except Exception as e:

        return {
            "success": False,
            "response": f"Error: {str(e)}"
        }