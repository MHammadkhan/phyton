# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:28:24 2017

@author: MuhammadHammad
"""
import base64
# BUILT IN STRING METHODS 
aa="Iqra"
bb="a"
intab="amys"
outtab="!@#$"
trantab = str.maketrans(intab, outtab)
b="-"
a="hammad is my name"
print("Capitilize mean first leeter capital \n")
print("without capital \n",a)

print("Capitilize function \n",a.capitalize())
print("center mean in the center \n")
print("nothing in left or right side\n",a.center(50))
print("* in left or right \n",a.center(50,"*"))

print("count mean count how many time given input occuer \n",a.count("m"))
en=a.encode('utf-8',errors='strict')
print("encode \n", en)
en=base64.b64encode(a.encode('utf-8',errors='strict'))   
print ("decode \n",en)
print("ends with \n", a.endswith("e"))
print("expand tabs \n",a.expandtabs(50))
print("Find mean if present return the index number \n",a.find("s"))
print("index is same as find\n",a.index("e"))
print("check string contain alphanumeric \n",a.isalnum())
print("The isalpha() method checks whether the string consists of alphabetic characters only. \n",a.isalpha())
print("The method isdigit() checks whether the string consists of digits only \n",a.isdigit())
print("The islower() method checks whether all the case-based characters (letters) of the string are lowercase\n",a.islower())
print("check only numeric present\n",a.isnumeric())
print("check only space present \n",a.isspace())
print("check all leeters are capital\n",a.istitle())
print("check all leeters are capital\n",a.isupper())
print("join strings \n",b.join(aa))
print("return lenght of string \n",len(a))
print("add some thing left side",a.ljust(50,'*'))
print("add some thing right side",a.rjust(50,'*'))

print("all data is in loeewr\n",a.lower())
print("all data is in upper\n",a.upper())
print("delete white space extra \n",a.strip('*'))
print("delete white space extra \n",a.lstrip('*'))
print("delete white space extra \n",a.rstrip('*'))
print("change characters \n",a.translate(trantab))
print("return max character \n",max(a))
print("return min character \n",min(aa))
print("replace character\n",a.replace('m','#'))
print("return last index if found \n",a.rfind(bb))
print("return last index if found \n",a.rindex(bb,4))
print("split strings into pices\n",a.split())
print("strtswith check strings start with given input\n",a.startswith('h'))
print("change character into upperor lower\n",a.swapcase())
print("return string with all first leeter capital\n",a.title())
print("add some thing \n",a.zfill(70))
print("check given string is decimal\n",a.isdecimal())

