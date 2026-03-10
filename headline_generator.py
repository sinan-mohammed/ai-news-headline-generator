from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from prompts import headline_prompt


pipe = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_length=200
)

llm = HuggingFacePipeline(pipeline=pipe)


def generate_headlines(article):

    prompt = headline_prompt.format(article=article)

    response = llm.invoke(prompt)

    headlines = response.split("\n")

    cleaned = []

    for h in headlines:
        if h.strip():
            cleaned.append(h.split(".",1)[-1].strip())

    return cleaned