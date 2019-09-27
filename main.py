import os

import requests
from flask import Flask, send_file, Response, redirect, url_for
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get('http://unkno.com')

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find('div', id='content').getText().strip()

    #facts = soup.find_all("div", id="content")
    #return facts[0].getText()


@app.route('/')
def home():

    url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    fact = get_fact()
    payload = {'input_text': fact}
    response = requests.post(url, data=payload)
    return redirect(response.url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

