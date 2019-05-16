# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
quandl token dRKBMBxVcFs2EX1yKmTT
"""
import pandas as pd
import os
import quandl
import time

auth_tok = "dRKBMBxVcFs2EX1yKmTT"

data = quandl.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2014-12-30", authtoken=auth_tok)

print(data)