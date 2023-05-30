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
        4,0,9,62,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,
        4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,52,8,6,1,7,4,7,55,8,7,11,7,12,7,56,1,8,
        1,8,1,8,1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,6,
        2,0,72,72,104,104,2,0,84,84,116,116,2,0,80,80,112,112,2,0,83,83,
        115,115,7,0,33,33,35,35,37,38,44,59,63,90,95,95,97,122,3,0,9,10,
        13,13,32,32,63,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,
        9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,
        19,1,0,0,0,3,21,1,0,0,0,5,23,1,0,0,0,7,26,1,0,0,0,9,28,1,0,0,0,11,
        30,1,0,0,0,13,51,1,0,0,0,15,54,1,0,0,0,17,58,1,0,0,0,19,20,5,60,
        0,0,20,2,1,0,0,0,21,22,5,62,0,0,22,4,1,0,0,0,23,24,5,60,0,0,24,25,
        5,47,0,0,25,6,1,0,0,0,26,27,5,61,0,0,27,8,1,0,0,0,28,29,5,34,0,0,
        29,10,1,0,0,0,30,31,5,39,0,0,31,12,1,0,0,0,32,33,7,0,0,0,33,34,7,
        1,0,0,34,35,7,1,0,0,35,36,7,2,0,0,36,37,7,3,0,0,37,38,5,58,0,0,38,
        39,5,47,0,0,39,40,5,47,0,0,40,41,1,0,0,0,41,52,3,15,7,0,42,43,7,
        0,0,0,43,44,7,1,0,0,44,45,7,1,0,0,45,46,7,2,0,0,46,47,5,58,0,0,47,
        48,5,47,0,0,48,49,5,47,0,0,49,50,1,0,0,0,50,52,3,15,7,0,51,32,1,
        0,0,0,51,42,1,0,0,0,52,14,1,0,0,0,53,55,7,4,0,0,54,53,1,0,0,0,55,
        56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,16,1,0,0,0,58,59,7,5,0,
        0,59,60,1,0,0,0,60,61,6,8,0,0,61,18,1,0,0,0,3,0,51,56,1,6,0,0
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
    LINK = 7
    TEXT = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'</'", "'='", "'\"'", "'''" ]

    symbolicNames = [ "<INVALID>",
            "OPENTAG", "CLOSETAG", "ENDTAG", "ATTRIBUTION", "ASPAS", "SIMPLEASPAS", 
            "LINK", "TEXT", "WS" ]

    ruleNames = [ "OPENTAG", "CLOSETAG", "ENDTAG", "ATTRIBUTION", "ASPAS", 
                  "SIMPLEASPAS", "LINK", "TEXT", "WS" ]

    grammarFileName = "HTMLRecognizer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


