from crewai import Crew
from tasks import create_tasks
from agents import resume_reader, job_analyzer, matcher
import time

def run_crew(resume_text, job_desc):
    
    # ✅ Create tasks
    tasks = create_tasks(resume_text, job_desc)

    # ✅ Create crew (IMPORTANT)
    crew = Crew(
        agents=[resume_reader, job_analyzer, matcher],
        tasks=tasks,
        verbose=True
    )

    try:
        result = crew.kickoff()
        return result
    except Exception as e:
        if "Rate limit" in str(e):
            time.sleep(12)
            result = crew.kickoff()
            return result
        else:
            raise e