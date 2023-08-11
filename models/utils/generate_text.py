def generate_rest_of_the_text(cohere_models, prompt: str):
    """
    Generate the rest of the sentence by starting with prompt
    :param prompt: str
        The prompt that we want to generate the rest
    :param cohere_models:
        The Cohere model
    :return:
    """

    response = cohere_models.generate(
        model='xlarge',
        prompt=prompt,
        max_tokens=75,
        temperature=0.4)

    output = response.generations[0].text
    print(output)