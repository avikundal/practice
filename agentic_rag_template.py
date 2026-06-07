from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI


# =========================
# 1. SETUP
# =========================

client = OpenAI()

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Employees are allowed 20 days of leave per year.",
    "To apply for leave, submit a request in the Keka portal.",
    "IT issues should be reported via the ticketing system."
]


# =========================
# 2. BUILD VECTOR DB
# =========================

doc_embeddings = embed_model.encode(documents)
doc_embeddings = np.array(doc_embeddings, dtype="float32")

index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)


# =========================
# 3. TOOL 1 : RETRIEVAL
# =========================

def retrieve(query, k=2):
    query_vec = embed_model.encode([query])
    query_vec = np.array(query_vec, dtype="float32")

    distances, indices = index.search(query_vec, k)

    results = []
    for i in indices[0]:
        results.append(documents[i])

    return results


# =========================
# 4. TOOL 2 : ACTION
# =========================

def create_ticket(issue):
    return f"Ticket created for issue: {issue}"


# =========================
# 5. AGENT DECISION MAKING
# =========================

def agent_decide(query):
    prompt = f"""
You are an AI agent.

Your job is to classify the user query.

Return only one word:
RETRIEVE
or
ACTION

Rules:
- If the query is asking for information, policy, or knowledge, return RETRIEVE
- If the query is asking to perform an action or report an issue, return ACTION

Query: {query}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    decision = response.choices[0].message.content.strip().upper()
    return decision


# =========================
# 6. FINAL ANSWER GENERATION
# =========================

def answer_from_docs(query, docs):
    context = "\n".join(docs)

    final_prompt = f"""
Answer the question using ONLY the context below.

If the answer is not present in the context, say:
"I could not find that in the documents."

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": final_prompt}
        ]
    )

    return response.choices[0].message.content


# =========================
# 7. MAIN AGENT LOOP
# =========================

def run_agent(query):
    decision = agent_decide(query)

    if "RETRIEVE" in decision:
        docs = retrieve(query)
        answer = answer_from_docs(query, docs)
        return answer

    elif "ACTION" in decision:
        return create_ticket(query)

    else:
        return "Could not decide"


# =========================
# 8. TEST
# =========================

if __name__ == "__main__":
    print(run_agent("How many leave days do I have?"))
    print(run_agent("How do I apply for leave?"))
    print(run_agent("My laptop is not working"))