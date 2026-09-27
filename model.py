import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langfuse import get_client


# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()


# ==========================================
# API KEY
# ==========================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not configured in the .env file.")


# ==========================================
# LANGFUSE
# ==========================================

langfuse = get_client()


# ==========================================
# MODEL
# ==========================================

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="openai/gpt-oss-120b",
    temperature=0
)


# ==========================================
# FUNCTION
# ==========================================

def get_llm_response(prompt):

    try:

        with langfuse.start_as_current_observation(
            as_type="span",
            name="jd_skill_extractor"
        ) as span:

            span.update(
                input=prompt
            )

            response = llm.invoke(prompt)

            result = response.content

            span.update(
                output=result
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
