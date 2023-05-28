# Generated from D:/Programming/Universidade/Compiladores/TokenRecognizer\HTMLRecognizer.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HTMLRecognizerParser import HTMLRecognizerParser
else:
    from HTMLRecognizerParser import HTMLRecognizerParser

# This class defines a complete generic visitor for a parse tree produced by HTMLRecognizerParser.

class HTMLRecognizerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HTMLRecognizerParser#htmlTags.
    def visitHtmlTags(self, ctx:HTMLRecognizerParser.HtmlTagsContext):
        return self.visitChildren(ctx)



del HTMLRecognizerParser