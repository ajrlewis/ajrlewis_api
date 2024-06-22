"""
1. **Keyword Extraction**: This endpoint can extract key phrases or keywords from a given text, helping users quickly identify the main topics or themes discussed in the content. This can be useful for content creators, marketers, and researchers looking to optimize their content for search engines or analyze trends.

2. **Question Answering**: Implement a question-answering endpoint that can provide accurate answers to user queries based on the input text. This can be valuable for customer support services, educational platforms, and FAQ sections on websites, enhancing user engagement and satisfaction.

3. **Named Entity Recognition**: Offer a named entity recognition endpoint that can identify and classify named entities such as people, organizations, locations, dates, and more in a given text. This can be beneficial for businesses looking to extract valuable information from unstructured text data, such as news articles, social media posts, or customer feedback.

4. **Text Generation**: Create a text generation endpoint that can generate coherent and contextually relevant text based on a given prompt. This can be utilized for content generation, chatbots, personalized recommendations, and creative writing applications, attracting users seeking unique and customized content.

5. **Document Classification**: Develop a document classification endpoint that can categorize text documents into predefined classes or topics. This can be advantageous for organizing and managing large volumes of textual data, enabling businesses to automate document sorting, content tagging, and information retrieval processes efficiently.

6. **Text Summarization with Keywords**: Enhance your summarization endpoint by including key phrases or keywords extracted from the summarized text. This can provide users with a quick overview of the main points while highlighting important terms for better understanding and SEO optimization.

7. **Sentiment Analysis for Social Media**: Develop a sentiment analysis endpoint specifically tailored for social media content. This can help businesses monitor and analyze customer sentiment, trends, and feedback on platforms like Twitter, Facebook, and Instagram, enabling targeted marketing campaigns and reputation management.

8. **Language Detection**: Offer a language detection endpoint that can identify the language of a given text. This can be useful for multilingual platforms, translation services, and international businesses looking to personalize content based on user preferences and language preferences.

9. **Text Clustering**: Implement a text clustering endpoint that groups similar documents or texts together based on their content. This can assist businesses in organizing and analyzing large datasets, identifying patterns, and generating insights for market segmentation, content recommendation, and trend analysis.

10. **Text Annotation**: Provide a text annotation endpoint that annotates text with relevant information such as named entities, part-of-speech tags, and sentiment labels. This can streamline data labeling tasks for machine learning models, improve text understanding, and enhance the accuracy of downstream NLP applications.

11. **Text Classification for Customer Feedback**: Create a text classification endpoint that categorizes customer feedback into predefined categories such as product quality, customer service, pricing, and more. This can help businesses prioritize and address customer concerns effectively, leading to improved customer satisfaction and loyalty.

12. **Text-to-Speech Conversion**: Develop a text-to-speech conversion endpoint that converts text input into natural-sounding speech. This can be beneficial for accessibility features, e-learning platforms, and interactive voice response systems, offering users an alternative way to consume content.

13. **Document Summarization**: Offer a document summarization endpoint that condenses lengthy documents into concise summaries, preserving the key information and main points. This can save users time and effort in digesting complex documents, making it ideal for research, news aggregation, and content curation.

14. **Text Generation with Style Transfer**: Enhance your text generation endpoint by incorporating style transfer capabilities, allowing users to generate text in different tones, voices, or writing styles. This can cater to diverse content creation needs, such as marketing copywriting, storytelling, and brand messaging.

15. **Text Similarity for Plagiarism Detection**: Develop a text similarity endpoint that detects similarities between texts to identify potential instances of plagiarism. This can be valuable for educational institutions, publishers, and content creators seeking to uphold originality standards and protect intellectual property rights.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

# from ..utils import chat
from utils import chat


class ContextMessage(BaseModel):
    # id: int = Field(None, description="The id of the message.")
    role: str = Field(
        None, description="The role of the message (e.g. system, user or assistant)."
    )
    content: str = Field(None, description="The content of the message.")


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/", response_model=ContextMessage)
async def root(context_messages: list[ContextMessage]) -> ContextMessage:
    """Returns the next message from a list of context messages."""
    # message = chat.call_openai(context_messages)
    message = {"role": "assistant", "content": "foobar"}
    return message


@router.post("/ask/")
async def ask(question: str, system: str = "") -> dict[str, str]:
    """Returns the response to q question."""
    # content = chat.call_gpt_model(context_messages)
    return {"answer": "foobar"}


@router.post("/sentiment/")
async def sentiment(text: str) -> dict[str, str]:
    """Returns the sentiment of a piece text."""
    return {"sentiment": "neutral"}


@router.post("/summarize/")
async def summarize(text: str) -> dict[str, str]:
    """Returns a summary of the text."""
    return {"summary": "foobar"}


@router.post("/translate/")
async def translate(text: str) -> dict[str, str]:
    """Returns the translation of a piece text."""
    return {"translation": "foobar"}


@router.post("/extract/")
async def extract(text: str) -> dict[str, str]:
    """Returns a JSON object extracted from the text."""
    return {"extract": "foobar"}


@router.post("/similarity/")
async def similarity(text: str) -> dict[str, str]:
    """Returns the similarity between pieces of text."""
    return {"similarity": "foobar"}


@router.post("/function/")
async def function(text: str) -> dict[str, str]:
    """Returns the sentiment of a piece text."""
    # content = chat.call_gpt_model(context_messages)
    return {"function": "foobar"}
