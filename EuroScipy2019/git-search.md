fd '\.f$'
fd '\.f$' -x git log --since="2017-09-03"  | rg '^commit '  | wc -l
