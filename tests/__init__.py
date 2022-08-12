# -*- coding: utf-8 -*-
#
# Copyright 2012 keyes.ie
#
# License: http://jkeyes.mit-license.org/
#

try:
    import os
    from dotenv import load_dotenv

    if os.path.exists('.env'):
        load_dotenv()
except Exception:
    pass