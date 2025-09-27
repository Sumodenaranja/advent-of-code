filepath = 'dayOne.txt'
prev = 0
increased = 0
decreased = 0
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       data = ("{}".format(line.strip()))
       try:
           if data > prev:
               print(data, "(Increased)")
               increased += 1
           elif data < prev:
                print(data, "(Decreased)")
                decreased += 1
            
       except:
           print(data,"(N/A - no previous mesurement)")

       prev = data
       line = fp.readline()
       cnt += 1 

       
print("The sumbmarines depth increased:" ,increased, "times")
print("The sumbmarines depth decreased:", decreased, "times")