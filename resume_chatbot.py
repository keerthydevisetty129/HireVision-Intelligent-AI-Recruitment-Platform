from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def answer_question(question, document):

    sentences = document.split(". ")

    texts = sentences + [question]

    vectorizer = TfidfVectorizer().fit_transform(texts)

    vectors = vectorizer.toarray()

    question_vector = vectors[-1]

    sentence_vectors = vectors[:-1]

    similarity = cosine_similarity([question_vector], sentence_vectors)

    index = similarity.argmax()

    return sentences[index]