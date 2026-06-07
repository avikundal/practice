from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAi


# setup

client = OpenAI()

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Employees are allowed 20 days of leave per year",
    " To apply for a leave, submit a request in the Keka portal",
    "IT issues should be reported via ticketing system"
]

# build Vector DB

doc_embeddings = embed_model.encode(documents)
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(np.array(doc_embeddings))


# tool 1 : Retrieval

def retrieve(query, k=2):
    query_vec = embed_model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)
    return [documents[i] for i in indices[0]]

# tool 2 : Action (Fake API)

def create_ticket(issue):
    return f"Ticket created for issue: {issue}"

# Agent ( Decision Making)

def agent_decide(query):
    prompt = f"""
    You are an AI agent.
    
    Decide:
    - If Query needs information - say : RETRIEVE 
    - If Query needs action - say : ACTION
    Query: {query}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    decision = response.choices[0].message.content.strip()
    return decision

# Main Agent loop

def run_agent(query):
    decision = agent_decide(query)

    if "RETRIEVE" in decision:
        docs = retrieve(query)
        context = "\n".join(docs)

        final_prompt = f"""
        Answer the question using the context below:
        
        Context:
        {context}
        
        Question:
        {query}
        """

        response = client.chat.completion.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": final_prompt}]
        )
        return response.choices[0].message.content

    elif "ACTION" in decision:
        return create_ticket(query)
    else:
        return "Could not decide"
    
if __name__=="__main__":
    print(run_agent(" How man leave days do i have?"))
    print(run_agent("My laptop is not working"))

    