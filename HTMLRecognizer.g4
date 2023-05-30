grammar HTMLRecognizer;
options { caseInsensitive = true; }

htmlTags: | (OPENTAG | ENDTAG | CLOSETAG | ATTRIBUTION | ASPAS | SIMPLEASPAS | LINK | TEXT)*;

OPENTAG: '<';
CLOSETAG: '>';
ENDTAG: '</';
ATTRIBUTION: '=';
ASPAS: '"';
SIMPLEASPAS: '\'';
LINK: 'https://' TEXT | 'http://' TEXT;
TEXT: [a-z#_:/.%0-9,?@!&;-]+;
WS: [ \t\n\r] -> skip;