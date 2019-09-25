import os

import requests
from flask import Flask, send_file, Response, redirect
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

@app.route('/')
def home():
    url = 'https://hidden-journey-62459.herokuapp.com/piglatinize'
    #header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)'}
    fact = get_fact()
    payload = {'input_text': fact}
    #response = requests.post(url, headers=header, data=payload, allow_redirects=False)
    response = requests.post(url, data=payload, allow_redirects=False)
    return redirect(response.url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

