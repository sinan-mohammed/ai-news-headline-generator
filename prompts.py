from langchain_core.prompts import PromptTemplate

headline_prompt = PromptTemplate(
    input_variables=["article"],
    template="""
You are a professional news editor.

Read the article and generate 5 headlines:

1. Breaking News headline
2. SEO headline
3. Social Media headline
4. Short headline
5. Creative headline

Article:
{article}

Return only the headlines as a numbered list.
"""
)