#! /usr/bin/env python3
import os
import sys
import argparse
import datetime as DT
import helper

## Define main function
def main(args, **kwargs):
    st=DT.datetime.now()
    print(f"Start: {st.strftime('%Y-%m-%d %H:%M:%S')}")
    
    print(f"INCUS: path='.', main(args={args}, kwargs={kwargs})")
    helper.helper("./nas").main(args[1:], opt2="deux")

    et=DT.datetime.now()
    print(f"End  : {et.strftime('%Y-%m-%d %H:%M:%S')}, Elapsed: {et-st}")

if __name__== "__main__":
    main(sys.argv, opt1="un")