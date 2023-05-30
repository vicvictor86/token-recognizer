import requests
import json
from bs4 import BeautifulSoup


def getValidHTMLTags():
    url = "https://way2tutorial.com/html/tag/index.php"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    tagTables = soup.find("table")

    htmlTags = []
    for row in tagTables.find_all("tr")[1:]:
        columns = row.find_all("td")

        tagsWithBrackets = columns[0].text.strip()
        tagsWithoutBrackets = tagsWithBrackets.replace('<', '').replace('>', '')

        htmlTags.append(tagsWithoutBrackets)
    with open('htmlTags.json', 'w') as file:
        json.dump(htmlTags, file, indent=4)

    return htmlTags
