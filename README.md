# shortnameguesser
A hacky tool to guess the rest of the IIS shortnames. This plugs directly into the output of [sns](https://github.com/sw33tLie/sns).

Quick and dirty one-liner:

`sns -u <target URL> --nocolor --silent | python3 shortnameguesser.py > guesses.txt && ffuf -u "<target URL>/FUZZ" -w guesses.txt`

# Requirements:
- Configure the `OPENAI_API_KEY` environment variable with your API key.
