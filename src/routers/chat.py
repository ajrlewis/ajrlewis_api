import json

from fastapi import APIRouter, HTTPException
from huggingkit import chat, client
from loguru import logger
from pydantic import BaseModel, Field

from dependencies import GetDBDep, GetCurrentUserDep
from schemas.chat import (
    ChatContextMessage,
    ChatContextMessages,
    ChatExtractInput,
    ChatExtractOutput,
)

hf_client = client.get_client(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1")


router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
async def root(
    db: GetDBDep, user: GetCurrentUserDep, context_messages: ChatContextMessages
) -> ChatContextMessage:
    """Returns the next message from a list of context messages."""
    message = {"role": "assistant", "content": "foobar"}
    return message


@router.post("/extract")
async def extract(
    db: GetDBDep, user: GetCurrentUserDep, chat_extract_input: ChatExtractInput
) -> ChatExtractOutput:
    """Returns the extracted data points from of a piece of text."""
    text = chat_extract_input.text
    data_points = chat_extract_input.data_points
    logger.debug(f"{text = } {data_points = }")
    message = chat.extract(client=hf_client, text=text, data_points=data_points)
    logger.debug(f"{message = }")
    content = message["content"]
    logger.debug(f"{content = }")
    cleaned_content = content.replace("\\", "")
    logger.debug(f"{cleaned_content = }")
    data = json.loads(cleaned_content)
    logger.debug(f"{data = }")
    return data
