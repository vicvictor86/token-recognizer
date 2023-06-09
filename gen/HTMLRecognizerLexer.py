# Generated from D:/Programming/Universidade/Compiladores/TokenRecognizer\HTMLRecognizer.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,39,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,
        5,1,6,4,6,32,8,6,11,6,12,6,33,1,7,1,7,1,7,1,7,0,0,8,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,1,0,2,7,0,33,33,35,35,37,38,44,59,63,90,95,
        95,97,122,3,0,9,10,13,13,32,32,39,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,1,17,1,0,0,0,3,19,1,0,0,0,5,21,1,0,0,0,7,24,1,0,0,0,9,26,1,0,
        0,0,11,28,1,0,0,0,13,31,1,0,0,0,15,35,1,0,0,0,17,18,5,60,0,0,18,
        2,1,0,0,0,19,20,5,62,0,0,20,4,1,0,0,0,21,22,5,47,0,0,22,23,5,62,
        0,0,23,6,1,0,0,0,24,25,5,61,0,0,25,8,1,0,0,0,26,27,5,34,0,0,27,10,
        1,0,0,0,28,29,5,39,0,0,29,12,1,0,0,0,30,32,7,0,0,0,31,30,1,0,0,0,
        32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,14,1,0,0,0,35,36,7,
        1,0,0,36,37,1,0,0,0,37,38,6,7,0,0,38,16,1,0,0,0,2,0,33,1,6,0,0
    ]

class HTMLRecognizerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OPENTAG = 1
    CLOSETAG = 2
    ENDTAG = 3
    ATTRIBUTION = 4
    ASPAS = 5
    SIMPLEASPAS = 6
    TEXT = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'/>'", "'='", "'\"'", "'''" ]

    symbolicNames = [ "<INVALID>",
            "OPENTAG", "CLOSETAG", "ENDTAG", "ATTRIBUTION", "ASPAS", "SIMPLEASPAS", 
            "TEXT", "WS" ]

    ruleNames = [ "OPENTAG", "CLOSETAG", "ENDTAG", "ATTRIBUTION", "ASPAS", 
                  "SIMPLEASPAS", "TEXT", "WS" ]

    grammarFileName = "HTMLRecognizer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


