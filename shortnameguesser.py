import os
import sys
import openai as ai

# Variables
ai.api_key = os.getenv("OPENAI_API_KEY")


def predict_long_names(shortname: str):
    # OpenAI prompt to generate the guesses.
    completions = ai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Return only a list of words, separated by newlines, and nothing else. Ensure that the words contain only alphanumeric characters."
            },
            {
                "role": "user",
                "content": f"Make a list of guesses, for what the rest of the word could be from this snippet. Ensure that the snippet is a substring of your guess. Make as many guesses as you can. Snippet: {shortname}"
            },
        ],
    )
    result = completions.choices[0].get("message").get("content").strip()
    return result


for line in sys.stdin:
    # It's probably the host from sns.
    if "http" in line:
        pass
    # Then it's not the host, it's probably the result.
    else:
        shortname = line.strip().split("~")[0]
        longname = predict_long_names(shortname)
        print(longname)
