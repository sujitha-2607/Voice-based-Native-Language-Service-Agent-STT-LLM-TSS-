from eligibility import job_eligibility, scheme_eligibility

def tool_check_job(data):
    age = data.get("age")
    edu = data.get("education")
    gender = data.get("gender")
    return job_eligibility(age, edu, gender)

def tool_check_schemes(data):
    age = data.get("age")
    edu = data.get("education")
    gender = data.get("gender")
    return scheme_eligibility(age, edu, gender)

TOOLS = {
    "check_jobs": tool_check_job,
    "check_schemes": tool_check_schemes
}
