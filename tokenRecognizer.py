import json

from antlr4 import *

from gen.HTMLRecognizerLexer import HTMLRecognizerLexer

tokens_name = {
    1: {'name': 'OPENTAG', 'color': 'red'},
    2: {'name': 'CLOSETAG', 'color': 'blue'},
    3: {'name': 'ENDTAG', 'color': 'green'},
    4: {'name': 'ATTRIBUTION', 'color': 'orange'},
    5: {'name': 'QUOTES', 'color': 'yellow'},
    6: {'name': 'SIMPLEQUOTES', 'color': 'purple'},
    7: {'name': 'LINK', 'color': 'magenta'},
    8: {'name': 'TEXT', 'color': 'pink'}
}


def getHTMLTokens(htmlText):
    dados = InputStream(htmlText)
    lexer = HTMLRecognizerLexer(dados)

    tokens_and_type = []
    tokensText = []
    tokenTagType = 8
    for tok in lexer.getAllTokens():
        tokens_and_type.append({'type': tok.type, 'text': tok.text})
        if tok.type == tokenTagType:
            tokensText.append(tok.text)
    lexer.reset()

    validHTMLTags = []
    with open('htmlTags.json', 'r') as file:
        validHTMLTags = json.load(file)

    validHTMLTokens = []
    for token in tokensText:
        tokenLowercase = token.lower()
        if tokenLowercase in validHTMLTags:
            validHTMLTokens.append(token)

    return validHTMLTokens, tokens_and_type
