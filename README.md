# MT*
MT machine simulator with three tapes.

Turing machine simulator called MT* with three tapes (X, Y and Z) which the tape X is actually the 
entry into the machine. The only rewritable tape is the tape X.

## Input mode:

prompt> simulatorMT archive.mt "Word"

In which 'simulatorMT' is the name of the machine, 'archive.mt' is the archive name (with the extension 
.mt) and '"Word"' is the entry that will be processed by the machine according to the archive .mt (it is 
important not to forget to put the word between the double quotes).

It is able to program on this machine using the Turing machine programming language (with the addition of 
the two other tapes Y and Z). The machine deals and erases all blank spaces, so do not forget to consider 
everything in the code (.mt) without them.
