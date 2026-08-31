from src.prompt.base import PromptMaster
from src.model.base import RequestModel
from src.llm.base import chat_openai, chat_ollama, chat_groq
from langchain_core.output_parsers import JsonOutputParser
from src.model.base import AIResponseModel

async def orchestrate_recommendation(req: RequestModel):

  category = req.category
  search = req.search

  human_prompt = f"""
  I’m looking for recommendations related to {category}.

  My search or reference is: "{search}"

  Based on this, recommend {category} that are genuinely similar in style, mood,
  theme, atmosphere, or overall appeal.

  Prioritize recommendations that:
  - Closely match what I searched for.
  - Capture the same mood, vibe, or experience.
  - Offer a good balance of familiar and less obvious choices.
  - Are relevant to my apparent taste rather than simply being popular.
  - Give me variety without straying too far from what I’m looking for.

  For each recommendation, briefly explain why it is a good match.

  Do not recommend the exact item I searched for. Focus on discovering
  high-quality alternatives that I’m likely to enjoy.
  """

  prompt_master = PromptMaster(category, human_prompt)



  prompt = prompt_master.prompt
  model = chat_ollama()
  output_parser = JsonOutputParser(pydantic_object=AIResponseModel)

  chain = prompt | model | output_parser

  response = chain.invoke({
    "human_prompt": human_prompt
  })

  return {
    "category": category,
    "response": response
  }
