from crewai import Task
from agents import resume_reader, job_analyzer, matcher

def create_tasks(resume_text, job_desc):

    task1 = Task(
        description=f"Extract skills from resume: {resume_text}",
        agent=resume_reader,
        expected_output="List of skills and experience"
    )

    task2 = Task(
        description=f"Analyze job description: {job_desc}",
        agent=job_analyzer,
        expected_output="Required skills and job expectations"
    )

    task3 = Task(
        description="Match resume with job description",
        agent=matcher,
        expected_output="Match score and suggestions"
    )

    return [task1, task2, task3]