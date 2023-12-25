class Employee():
    def __new__(self):
        print("Creator")
        return super().__new__(self)
    def __init__(self):
        print("Constructor")
Employee()

