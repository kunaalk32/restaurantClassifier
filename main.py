import sys
import requests
from bs4 import BeautifulSoup
import openai

openai.api_key = ""


def main():
    if len(sys.argv) < 2:
        print("Please provide a URL as an argument.")
        return

    url = sys.argv[1]
    page = get_webpage_content(url)
    if page is None:
        return
    print(classify_webpage(page))


def get_webpage_content(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the webpage. HTTP Status Code: {response.status_code}")
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.prettify()
    except:
        print("There was an error with the URL")
        return None


def classify_webpage(page):
    prompt_text = f"Based on the following HTML content of a restaurant webpage, what cuisine does the restaurant serve?\n\n{page}\n\nAnswer:"
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt_text,
        max_tokens=5
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    main()
