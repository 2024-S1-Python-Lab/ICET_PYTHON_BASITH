filename1 = input ("enter Source file name ") 
with open(filename1, 'r') as file1:  
      lines = file1.readlines()
filename2 = input ("enter destination file name ")
with open(filename2, 'w') as file2: 
     for i in range(len(lines)):   
         if i % 2 == 0:   
              file2.write(lines[i])
print("Odd lines copied to 'filename2'.")

with open(filename2,'r') as file2:
    lines=file2.readlines()
    print (lines)
