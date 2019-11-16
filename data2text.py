#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:56:27 2018

Simple python for creating mails using template mail.

Edit the index section

@author: mikeogawa
"""

import pandas as pd

candidate=pd.read_csv("source/name.csv")

## index
rep = dict(
XXM=0,
XXN=1,
XXO=2,
)

## Process
for i in range(len(candidate)):
    with open("source/script.txt") as f:
        file_str = f.read()
        for k,v in rep.items():
            file_str=file_str.replace(k,candidate.iloc[i,v])    
                    
    with open("mail_list/"+str("0"+str(i+1))[-2:]+".txt", "w") as f:
        f.write(file_str)

    