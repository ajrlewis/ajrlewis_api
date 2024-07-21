import os
import anthropic
import openai


def create_message(role: str, content: str) -> dict[str, str]:
    return {"role": role, "content": content.strip()}


def create_message_from_template(template: str) -> dict[str, str]:
    content = template
    return create_message("user", content)


def call_anthropic(context_messages: list[dict]):
    """https://platform.openai.com/docs/guides/chat/introduction"""
    content = ""
    try:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        client = anthropic.Anthropic(api_key=api_key)
    except Exception as e:
        print(e)
        return content
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": [{"type": "text", "text": "Why is the ocean salty?"}],
            }
        ],
    )
    print(message.content)


class Website:
    url = "https://example.com"
    text = ""
    scraped_on = ""
    is_reachable = False
    error = ""


class Model:
    name = "gpt-3.5-turbo"


class ModelConfig:
    # How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.
    temperature = 0.2
    # The maximum number of tokens to generate shared between the prompt and completion. The exact limit varies by model. (One token is roughly 4 characters for standard English text)
    max_tokens = 256
    # Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered.
    top_p = 1
    # How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.
    frequency_penalty = 0
    # How much to penalize new tokens based on whether they appear in the text so far. Increases the model's likelihood to talk about new topics.
    presence_penalty = 0


# PromptResponse


def call_openai(
    context_messages: list[dict],
    model_name: str = "gpt-3.5-turbo",
    model_config: dict = {
        "temperature": 0.2,  # How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.
        "max_tokens": 256,  # The maximum number of tokens to generate shared between the prompt and completion. The exact limit varies by model. (One token is roughly 4 characters for standard English text)
        "top_p": 1,  # Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered.
        "frequency_penalty": 0,  # How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.
        "presence_penalty": 0,  # How much to penalize new tokens based on whether they appear in the text so far. Increases the model's likelihood to talk about new topics.
    },
) -> str:
    """https://platform.openai.com/docs/guides/chat/introduction"""
    content = ""
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        client = openai.OpenAI(api_key=api_key)
    except Exception as e:
        print()
        return content
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=context_messages,
            **model_config,
        )
        content = response.choices[0].message.content
    except openai.BadRequestError as e:
        print(f"Error 400: {e}")
    except openai.AuthenticationError as e:
        print(f"Error 401: {e}")
    except openai.PermissionDeniedError as e:
        print(f"Error 403: {e}")
    except openai.NotFoundError as e:
        print(f"Error 404: {e}")
    except openai.UnprocessableEntityError as e:
        print(f"Error 422: {e}")
    except openai.RateLimitError as e:
        print(f"Error 429: {e}")
    except openai.InternalServerError as e:
        print(f"Error >=500: {e}")
    except openai.APIConnectionError as e:
        print(f"API connection error: {e}")
    return content
