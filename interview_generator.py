def generate_questions(skills):

    questions = []

    # technical roles
    if "python" in skills:
        questions.append("Explain Python decorators.")
        questions.append("What are Python generators?")

    if "machine learning" in skills:
        questions.append("What is overfitting in machine learning?")
        questions.append("Explain bias vs variance.")

    if "sql" in skills:
        questions.append("Explain different types of SQL joins.")

    # business roles
    if "marketing" in skills:
        questions.append("How would you design a marketing strategy for a new product?")

    if "finance" in skills:
        questions.append("Explain the concept of ROI.")

    if "project management" in skills:
        questions.append("How do you manage project risks?")

    # general professional questions
    if len(questions) == 0:
        questions.extend([
            "Tell me about yourself.",
            "Explain your most recent project.",
            "Describe a challenging problem you solved.",
            "How do you work in a team?",
            "What motivates you in your career?"
        ])

    return questions