#!/usr/bin/env python

"""
aprspass.py: Get an APRS-IS password hash for a given callsign.

Ported from aprsd: http://sourceforge.net/projects/aprsd/
"""

import sys

def getPass(callsign):

        basecall = callsign.upper().split('-')[0] + '\0'
        result = 0x73e2
        
        c = 0
        while (c+1 < len(basecall)):
                result ^= ord(basecall[c]) << 8
                result ^= ord(basecall[c+1])
                c += 2
        
        result &= 0x7fff
        return result

def main():
        print getPass(sys.argv[1])

if __name__ == "__main__":
        main()
