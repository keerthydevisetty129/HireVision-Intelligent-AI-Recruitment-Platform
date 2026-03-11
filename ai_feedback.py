def generate_resume_feedback(skills):

    feedback = []

    if len(skills) < 5:
        feedback.append("Consider adding more technical or professional skills.")

    if "communication" not in skills:
        feedback.append("Highlight communication or leadership skills.")

    if "project management" not in skills:
        feedback.append("Add details about projects you have handled.")

    feedback.append("Ensure your resume clearly describes your achievements.")

    return feedback