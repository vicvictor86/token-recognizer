# Generated from D:/Programming/Universidade/Compiladores/TokenRecognizer\HTMLRecognizer.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,12,2,0,7,0,1,0,1,0,5,0,5,8,0,10,0,12,0,8,9,0,3,0,10,8,0,1,
        0,0,0,1,0,0,1,1,0,1,7,12,0,9,1,0,0,0,2,10,1,0,0,0,3,5,7,0,0,0,4,
        3,1,0,0,0,5,8,1,0,0,0,6,4,1,0,0,0,6,7,1,0,0,0,7,10,1,0,0,0,8,6,1,
        0,0,0,9,2,1,0,0,0,9,6,1,0,0,0,10,1,1,0,0,0,2,6,9
    ]

class HTMLRecognizerParser ( Parser ):

    grammarFileName = "HTMLRecognizer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'/>'", "'='", "'\"'", "'''" ]

    symbolicNames = [ "<INVALID>", "OPENTAG", "CLOSETAG", "ENDTAG", "ATTRIBUTION", 
                      "ASPAS", "SIMPLEASPAS", "TEXT", "WS" ]

    RULE_htmlTags = 0

    ruleNames =  [ "htmlTags" ]

    EOF = Token.EOF
    OPENTAG=1
    CLOSETAG=2
    ENDTAG=3
    ATTRIBUTION=4
    ASPAS=5
    SIMPLEASPAS=6
    TEXT=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class HtmlTagsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENTAG(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLRecognizerParser.OPENTAG)
            else:
                return self.getToken(HTMLRecognizerParser.OPENTAG, i)

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLRecognizerParser.TEXT)
            else:
                return self.getToken(HTMLRecognizerParser.TEXT, i)

        def CLOSETAG(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLRecognizerParser.CLOSETAG)
            else:
                return self.getToken(HTMLRecognizerParser.CLOSETAG, i)

        def ENDTAG(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLRecognizerParser.ENDTAG)
            else:
                return self.getToken(HTMLRecognizerParser.ENDTAG, i)

        def ATTRIBUTION(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLRecognizerParser.ATTRIBUTION)
            else:
                return self.getToken(HTMLRecognizerParser.ATTRIBUTION, i)

        def ASPAS(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLRecognizerParser.ASPAS)
            else:
                return self.getToken(HTMLRecognizerParser.ASPAS, i)

        def SIMPLEASPAS(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLRecognizerParser.SIMPLEASPAS)
            else:
                return self.getToken(HTMLRecognizerParser.SIMPLEASPAS, i)

        def getRuleIndex(self):
            return HTMLRecognizerParser.RULE_htmlTags

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlTags" ):
                listener.enterHtmlTags(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlTags" ):
                listener.exitHtmlTags(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHtmlTags" ):
                return visitor.visitHtmlTags(self)
            else:
                return visitor.visitChildren(self)




    def htmlTags(self):

        localctx = HTMLRecognizerParser.HtmlTagsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_htmlTags)
        self._la = 0 # Token type
        try:
            self.state = 9
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 6
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0):
                    self.state = 3
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 254) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 8
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





