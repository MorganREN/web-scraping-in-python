#-web scribe the page data of sogo index page

import requests

if __name__ == "__main__":
    # step 1: clear the pointed url
    url = "https://www.sogou.com/"
    # step 2: request
    # The get() method would return a responsing object
    response = requests.get(url=url)
    # step 3: get the reponse data
    page_text = response.text
    print(page_text)
    # step 4: constantly store the data
    with open('./sogo.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print("Finished!")
