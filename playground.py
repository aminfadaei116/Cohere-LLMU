import cohere
from models.utils.utils import *


def main():
    api_key = load_api_key()
    co = cohere.Client(api_key)

    # prompt = "The best way to become ourselves is"
    # generate_rest_of_the_text(co, prompt)


    classify(co)



if __name__ == "__main__":
    main()
