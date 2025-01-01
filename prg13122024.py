class student:
    def get(self, rlno,name,totalmark):
        self.rlno = rlno
        self.name = name
        self.totalmark = totalmark

    def disp(self):
        print(f"Roll Number:{self.rlno}")
        print(f"Nmae:{self.name}")
        print(f"Total Mark:{self.totalmark}")

stud1 = student()
stud1.get(101,"Alice",85)
stud1.disp()
        
