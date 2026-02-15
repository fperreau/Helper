class helper():
    def __init__(self,path):
        self.path=path

    def main(self,args,**kwargs):
        print(f"helper: path='{self.path}', main(args={args}, kwargs={kwargs})")

