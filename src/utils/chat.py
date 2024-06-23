import os
import anthropic
import openai


def create_message(role: str, content: str) -> dict[str, str]:
    return {"role": role, "content": content.strip()}


def create_message_from_template(template: str) -> dict[str, str]:
    content = template
    return create_message("user", content)


def call_anthropic():
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


def call_openai(
    context_messages: list[dict],
    model: str = "gpt-3.5-turbo",
    temperature: float = 0.2,
    # max_tokens=256,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0
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
            model=model,
            temperature=temperature,
            messages=context_messages,
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
