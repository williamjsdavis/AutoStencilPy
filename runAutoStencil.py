#!/usr/bin/python
import sys
import AutoStencil as austen

if __name__ == '__main__':
    latexString, codeString = austen.parseStringInputs(
        str(sys.argv[1]), str(sys.argv[2]))
    print(latexString)
    print(codeString)