import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langfuse import get_client


# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()


# ==========================================
# API KEYS
# ==========================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST")


# ==========================================
# LANGFUSE
# ==========================================

langfuse = get_client()


print("Langfuse Host:", LANGFUSE_HOST)

if LANGFUSE_PUBLIC_KEY:
    print("Langfuse Public Key:", LANGFUSE_PUBLIC_KEY[:10])


# ==========================================
# MODEL
# ==========================================

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="openai/gpt-oss-120b",
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

            # Call LLM
            response = llm.invoke(prompt)

            result = response.content

            # Store output in Langfuse
            span.update(
                output=result
            )

        # Send trace data
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
