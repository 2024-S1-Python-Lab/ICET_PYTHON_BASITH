class student:
    def get(self):
        self.rlno = int(input("Enter RollNumber:"))
        self.name = input("Enter Name:")
        self.totalmark = float(input("Enter TotalMarks:"))

    def disp(self):
        print("\nStudent Details")
        print(f"RollNumber:{self.rlno}")
        print(f"Name:{self.name}")
        print(f"Total Mark:{self.totalmark}")

stud1 = student()
stud1.get()
stud1.disp()
        
