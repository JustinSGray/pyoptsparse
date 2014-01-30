#!/usr/bin/env python
'''
pyOptSparse_error

Holds a simple error handling class for pyOptSparse

Copyright (c) 2008-2013 by Dr. Gaetan Kenway
All rights reserved.

Developers:
-----------
- Dr. Gaetan K.W. Kenway (GKK)

History
-------
    v. 1.0  - Initial Class Creation (GKK, 2013)
'''

class Error(Exception):
    """
    Format the error message in a box to make it clear this
    was a expliclty raised exception.
    """
    def __init__(self, message):
      msg = '\n+'+'-'*78+'+'+'\n' + '| pyOptSparse Error: '
      i = 22
      for word in message.split():
         if len(word) + i +1 > 78: # Finish line and start new one
            msg += ' '*(78-i)+'|\n| ' + word + ' '
            i = 2 + len(word)+1
         else:
            msg += word + ' '
            i += len(word)+1
         msg += ' '*(79-i) + '|\n' + '+'+'-'*78+'+'+'\n'
         print msg

