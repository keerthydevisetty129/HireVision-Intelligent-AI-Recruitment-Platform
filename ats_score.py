def calculate_ats_score(job_skills,candidate_skills):

    matched = set(job_skills) & set(candidate_skills)

    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0

    return round(score,2)