from src.prompt.base import PromptMaster
from src.model.base import RequestModel
from src.llm.base import chat_openai
from langchain_core.output_parsers import JsonOutputParser
from src.model.base import AIResponseModel

async def orchestrate_recommendation(req: RequestModel):
  artist = req.artist
  song = req.song

  human_prompt = f"I love the song '{song}' by {artist}. Recommend similar songs to keep the mood going"

  prompt_master = PromptMaster(human_prompt)

  prompt = prompt_master.prompt
  model = chat_openai()
  output_parser = JsonOutputParser(pydantic_object=AIResponseModel)

  chain = prompt | model | output_parser

  response = chain.invoke({})

  return response
