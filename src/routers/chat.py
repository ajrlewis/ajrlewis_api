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


class ChatExtractInput(BaseModel):
    text: str = Field(
        "Commerce on the Internet has come to rely almost exclusively on financial institutions serving as trusted third parties to process electronic payments. While the system works well enough for most transactions, it still suffers from the inherent weaknesses of the trust based model. Completely non-reversible transactions are not really possible, since financial institutions cannot avoid mediating disputes. The cost of mediation increases transaction costs, limiting the minimum practical transaction size and cutting off the possibility for small casual transactions, and there is a broader cost in the loss of ability to make non-reversible payments for nonreversible services. With the possibility of reversal, the need for trust spreads. Merchants must be wary of their customers, hassling them for more information than they would otherwise need. A certain percentage of fraud is accepted as unavoidable. These costs and payment uncertainties can be avoided in person by using physical currency, but no mechanism exists to make payments over a communications channel without a trusted party.",
        description="The text to extract data points from.",
    )
    data_points: dict[str, str] = Field(
        {"summary": "A summary of the text."},
        description="The data points to extract, key-value pairs of the data to extract and a description of that data.",
    )


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


from dependencies import GetDBDep, GetCurrentUserDep


@router.post("/extract/")
async def extract(
    db: GetDBDep, user: GetCurrentUserDep, chat_extract_input: ChatExtractInput
) -> dict[str, str]:
    """Returns the extracted data points from of a piece of text."""
    text = chat_extract_input.text
    data_points = chat_extract_input.data_points
    logger.debug(f"{text = } {data_points = }")
    message = chat.extract(client=hf_client, text=text, data_points=data_points)
    logger.debug(f"{message = }")
    content = message["content"]
    logger.debug(f"{content = }")
    data = json.loads(content)
    logger.debug(f"{data = }")
    return data


@router.post("/ask/")
async def ask(db: GetDBDep, user: GetCurrentUserDep) -> dict[str, str]:
    """Returns the"""
    data = {"foo": "bar"}
    return data
