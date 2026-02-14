#! /usr/bin/env python3
import os
import datetime as DT

class Plugin():
    def __init__(self,name,path):
        self.name=name
        self.path=path

    def __repr__(self):
        return f"Plugin(name='{self.name}, path='{self.path}')"


## Define main function
def main():
    print("Start: ",DT.datetime.now())

    cur=Plugin("nas", ".nas")
    print(cur)

    print("End  : ",DT.datetime.now())

if __name__== "__main__":
    main()