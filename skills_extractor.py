skills_db = [

# programming
"python","java","c++","sql","javascript","react","node","html","css",

# data science
"machine learning","deep learning","nlp","pandas","numpy","tensorflow","pytorch",

# business / mba
"marketing","finance","accounting","business analysis","project management",

# general professional skills
"communication","leadership","teamwork","problem solving","critical thinking",

# tools
"excel","power bi","tableau","git","docker","aws","azure"
]

def extract_skills(text):

    found = []

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return list(set(found))