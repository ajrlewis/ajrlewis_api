import json

from fastapi import APIRouter, HTTPException
from huggingkit import chat, client
from loguru import logger
from pydantic import BaseModel, Field


hf_client = client.get_client(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1")


class ContextMessage(BaseModel):
    role: str = Field(
        None, description="The role of the message (e.g. system, user or assistant)."
    )
    content: str = Field(None, description="The content of the message.")


class ExtractInput(BaseModel):
    text: str = Field(None, description="The text to extract from")
    data_points: dict[str, str] = Field(None, description="The data points to extract.")


class ExtractOutput(BaseModel):
    data_points: dict[str, str] = Field(None, description="The extracted data.")


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


# @router.post("/", response_model=ContextMessage)
# async def root(context_messages: list[ContextMessage]) -> ContextMessage:
#     """Returns the next message from a list of context messages."""
#     message = {"role": "assistant", "content": "foobar"}
#     return message


# @router.post("/ask/")
# async def ask(question: str, system: str = "") -> dict[str, str]:
#     """Returns the response to q question."""
#     # content = chat.call_gpt_model(context_messages)
#     return {"answer": "foobar"}


@router.post("/extract/")
async def extract(extract_input: ExtractInput) -> dict[str, str]:
    """Returns the extracted data points from of a piece text."""
    text = extract_input.text
    data_points = extract_input.data_points
    logger.debug(f"{text = } {data_points = }")
    message = chat.extract(client=hf_client, text=text, data_points=data_points)
    logger.debug(f"{message = }")
    content = message["content"]
    logger.debug(f"{content = }")
    data = json.loads(content)
    logger.debug(f"{data = }")
    return data


{
    "role": "assistant",
    "content": ' {\n"full_name": "Mariana Anderson",\n"job_title": "UI / UX Designer",\n"phone_number": "+123-456-7890",\n"email": "hello@reallygreatsite.com",\n"URL": "www.reallygreatsite.com",\n"address": "123 Anywhere St., Any City, ST 12345"\n}',
}
