def generate_rest_of_the_text(co, prompt: str):
    """
    Generate the rest of the sentence by starting with prompt
    :param prompt: str
        The prompt that we want to generate the rest
    :param co:
        The Cohere model
    :return:
    """

    response = co.generate(
        model='xlarge',
        prompt=prompt,
        max_tokens=75,
        temperature=0.4)

    output = response.generations[0].text
    print(output)