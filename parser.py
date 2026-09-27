from typing import List
from pydantic import BaseModel


class JobDetails(BaseModel):
    job_title: str
    skills: List[str]
    experience: str
    education: str


class JobExtraction(BaseModel):
    jobs: List[JobDetails]
