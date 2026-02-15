#! /usr/bin/env python3
import os
import datetime as DT
import incus_helper as IH

## Define main function
def main():
    print("Start: ",DT.datetime.now())

    cur=IH.incus_helper("nas",".nas")
    print(cur)

    print("End  : ",DT.datetime.now())

if __name__== "__main__":
    main()