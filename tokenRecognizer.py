import json

from antlr4 import *

from gen.HTMLRecognizerLexer import HTMLRecognizerLexer
from gen.HTMLRecognizerParser import HTMLRecognizerParser


def getHTMLTokens(htmlText):
    dados = InputStream(htmlText)
    lexer = HTMLRecognizerLexer(dados)

    tokensText = []
    tokenTagType = 7
    for tok in lexer.getAllTokens():
        if tok.type == tokenTagType:
            tokensText.append(tok.text)
    lexer.reset()

    validHTMLTags = []
    with open('htmlTags.json', 'r') as file:
        validHTMLTags = json.load(file)

    validHTMLTokens = [token for token in tokensText if token in validHTMLTags]

    return validHTMLTokens, tokensText

    # stream = CommonTokenStream(lexer)
    # parser = HTMLRecognizerParser(stream)
    #
    # tree = parser.htmlTags()
    # print(tree.toStringTree())
