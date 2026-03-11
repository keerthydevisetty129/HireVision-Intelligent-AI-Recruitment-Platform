from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description,resumes):

    documents = [job_description] + resumes

    vectorizer = TfidfVectorizer().fit_transform(documents)

    vectors = vectorizer.toarray()

    job_vector = vectors[0]

    resume_vectors = vectors[1:]

    similarity = cosine_similarity([job_vector],resume_vectors).flatten()

    scores = (similarity*100).round(2)

    return scores