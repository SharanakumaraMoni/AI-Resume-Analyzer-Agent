from crewai import Crew
from tasks import create_tasks

def run_crew(resume_text, job_desc):
    tasks = create_tasks(resume_text, job_desc)

    crew = Crew(
        agents=[task.agent for task in tasks],
        tasks=tasks,
          verbose=True
    )

    result = crew.kickoff()
    return result