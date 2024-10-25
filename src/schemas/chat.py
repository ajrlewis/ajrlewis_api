import datetime
from typing import Union

from pydantic import BaseModel, Field


class ChatContextMessage(BaseModel):
    role: str = Field(
        description="The role of the message (e.g. system, user or assistant)."
    )
    content: str = Field(None, description="The content of the message.")


ChatContextMessages = list[ChatContextMessage]


class ChatExtractInput(BaseModel):
    text: str = Field(
        "Commerce on the Internet has come to rely almost exclusively on financial institutions serving as trusted third parties to process electronic payments. While the system works well enough for most transactions, it still suffers from the inherent weaknesses of the trust based model. Completely non-reversible transactions are not really possible, since financial institutions cannot avoid mediating disputes. The cost of mediation increases transaction costs, limiting the minimum practical transaction size and cutting off the possibility for small casual transactions, and there is a broader cost in the loss of ability to make non-reversible payments for nonreversible services. With the possibility of reversal, the need for trust spreads. Merchants must be wary of their customers, hassling them for more information than they would otherwise need. A certain percentage of fraud is accepted as unavoidable. These costs and payment uncertainties can be avoided in person by using physical currency, but no mechanism exists to make payments over a communications channel without a trusted party.",
        description="The text to extract data points from.",
    )
    data_points: dict[str, str] = Field(
        {"summary": "A summary of the text."},
        description="The data points to extract, key-value pairs of the data to extract and a description of that data.",
    )


ChatExtractOutput = dict
