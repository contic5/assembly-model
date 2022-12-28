file1 = open('thesis-results-parsev3.txt', 'r') 
  
# Using for loop 
for line in file1: 
    line=line.strip()
    if('is ' in line):
        print(line.split("is ",1)[1])
    else:
        print(line)
