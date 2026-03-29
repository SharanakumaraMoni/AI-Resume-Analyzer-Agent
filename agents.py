from crewai import Agent, LLM
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Debug check
print("API KEY:", os.getenv("GROQ_API_KEY"))

# Correct LLM setup
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
)

resume_reader = Agent(
    role="Resume Reader",
    goal="Extract skills and experience from resume",
    backstory="Expert in analyzing resumes",
    llm=llm
)

job_analyzer = Agent(
    role="Job Analyzer",
    goal="Extract required skills from job description",
    backstory="Expert in understanding job roles",
    llm=llm
)

matcher = Agent(
    role="Matcher",
    goal="Compare resume with job description and provide match score",
    backstory="Expert in candidate-job matching",
    llm=llm
)