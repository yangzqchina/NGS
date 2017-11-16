 -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 15:50:18 2017

@author: zqyang
"""

import argparse
import os
Args=argparse.ArgumentParser(description='count reference genome length')
Args.add_argument('-i','--input',dest='input')
args=Args.parse_args()
def convert(infile):
    out=open('chrom.sizes','w')
    i=0
    for line in open(infile):
        line2=line.strip()
        if line2[0]=='>':
            if i == 0:
                chr_i=line2[1:]
                len_i=0
                i+=1
            else:
                out.write("%s\t%i\n"%(chr_i,len_i))
                chr_i=line2[1:]
                len_i=0
                i+=1
        else:
            len_i += len(line2)
    out.write("%s\t%i"%(chr_i,len_i))
    out.close()
convert(args.input)
