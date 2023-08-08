import cohere
from models.utils.utils import load_api_key


def main():
    api_key = load_api_key()
    co = cohere.Client(api_key)
    print(co)
    

if __name__ == "__main__":
    main()
