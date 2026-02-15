class incus_helper():
    def __init__(self,name,path):
        self.name=name
        self.path=path

    def __str__(self):
        return f"incus_helper(name='{self.name}', path='{self.path}')"
