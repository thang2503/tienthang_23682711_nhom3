# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:50:32 2024

@author: ACER
"""

a="Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM" 
a=a.replace("P. ","").replace("Q. ","").replace("Tp. " ,"")
sub_string = a.split(", ")
for sub in sub_string:
    print(sub)


    



