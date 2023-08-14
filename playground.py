import cohere
from models.utils.utils import *
from models.classify import classify
from models.embed import extract_embeding


def main():
    api_key = load_api_key()
    co = cohere.Client(api_key)

    assert co.check_api_key()["valid"], "The api_key is not valid!"

    # prompt = "The best way to become ourselves is"
    # generate_rest_of_the_text(co, prompt)

    # classify(co)

    extract_embeding(co, ["hi this is amin"])

if __name__ == "__main__":
    main()
