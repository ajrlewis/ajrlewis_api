# sentiment = (
#     "Classify the text into neutral, negative, or positive\nText: {text}.\nSentiment:\n"
# )
# sentiment.format(**{"text":"I hate this place"})
# 'Classify the text into neutral, negative, or positive\nText: I hate this place.\nSentiment:\n'# temperature=1,

# max_tokens=256,
# top_p=1,
# frequency_penalty=0,
# presence_penalty=0


class PromptTemplate:
    def __init__(self, template: str, input_variables: list[str]):
        self.template = template
        self.input_variables = input_variables

    def render(self, **kwargs):
        data = {k: v for k, v in kwargs.items() if k in self.input_variables}
        return self.template.format(**data)


sentiment_prompt_template = PromptTemplate(
    template="Classify the text into neutral, negative, or positive\nText: {text}.\nSentiment:\n",
    input_variables=["text"],
)

print(f'{sentiment_prompt_template.render(text="I hate this place")}')

# sentiment_prompt_template.render()
