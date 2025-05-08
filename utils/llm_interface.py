from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_huggingface import HuggingFacePipeline

def generate_flashcards(context: str, topic: str) -> str:
    MODEL_ID = "google/flan-t5-base"

    prompt = PromptTemplate.from_template(

"""

You are an expert at generating study flashcards from source text.



Context (multiple excerpts):

{context}



Instructions:

1. Identify the 5 most important facts about "{topic}" in the context.

2. For each fact, write a concise flashcard with:

Q: a question that tests understanding of that fact.

A: the precise answer, using only information from the context.

3. Use this exact format (no extra text):



Flashcard 1:

Q: <question>

A: <answer>



Flashcard 2:

Q: <question>

A: <answer>

... up to Flashcard 5.

"""

)



    hf_pipeline = HuggingFacePipeline.from_model_id(
model_id=MODEL_ID,
task="text2text-generation",
pipeline_kwargs={"max_new_tokens": 300, "temperature": 0.2})

    chain = LLMChain(llm=hf_pipeline, prompt=prompt)
    return chain.run(context=context, topic=topic)