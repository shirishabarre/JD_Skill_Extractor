from pydantic import BaseModel
from typing import List

class JobDetails(BaseModel):

    skills: List[str]

    experience: str

    education: str