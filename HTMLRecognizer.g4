grammar HTMLRecognizer;

htmlTags: | (OPENTAG | TEXT | CLOSETAG | ENDTAG | ATTRIBUTION | ASPAS | SIMPLEASPAS)*;

OPENTAG: '<';
CLOSETAG: '>';
ENDTAG: '/>';
ATTRIBUTION: '=';
ASPAS: '"';
SIMPLEASPAS: '\'';
TEXT: [a-zA-Z#_:/.%0-9,?@!&;-]+;
WS: [ \t\n\r] -> skip;