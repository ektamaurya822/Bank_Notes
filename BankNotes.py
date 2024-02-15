# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:31:54 2024

@author: Ekta
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float