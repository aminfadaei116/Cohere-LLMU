import cohere
from models.utils.utils import load_api_key


def main():
    api_key = load_api_key()
    co = cohere.Client(api_key)
    prompt = "Hello World is a program that"

    response = co.generate(
        model='xlarge',
        prompt=prompt,
        max_tokens=75,
        temperature=0.4)

    output = response.generations[0].text
    print(output)


if __name__ == "__main__":
    main()
