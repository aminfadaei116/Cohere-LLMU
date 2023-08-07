import cohere


import json

with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['api_key']

# Now you can use the 'api_key' variable in your code


def main():
    co = cohere.Client()
    print(co)



if __name__ == "__main__":
    main()