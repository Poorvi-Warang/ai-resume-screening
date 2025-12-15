import openai

def generate_suggestions(resume_text, job_text, api_key):
    openai.api_key = api_key

    prompt = f"""
    Resume:
    {resume_text}

    Job Description:
    {job_text}

    Identify missing skills and suggest improvements.
    

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message["content"]

