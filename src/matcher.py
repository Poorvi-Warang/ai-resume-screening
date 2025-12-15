from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text, job_text):
    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    match_percentage = round(similarity * 100, 2)

    # Extract skills (top keywords)
    feature_names = vectorizer.get_feature_names_out()
    resume_vector = tfidf_matrix[0].toarray()[0]
    job_vector = tfidf_matrix[1].toarray()[0]

    matched_skills = [
        feature_names[i]
        for i in range(len(feature_names))
        if resume_vector[i] > 0 and job_vector[i] > 0
    ]

    missing_skills = [
        feature_names[i]
        for i in range(len(feature_names))
        if resume_vector[i] == 0 and job_vector[i] > 0
    ]

    return {
        "match_percentage": match_percentage,
        "matched_skills": matched_skills[:10],
        "missing_skills": missing_skills[:10],
    }
