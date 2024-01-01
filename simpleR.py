def Cal(P,T,R):
    SI = (P*T*R)/100
    return SI
    
P = float(input("Enter the rate of Principle:" ))
T = float(input("Time Taken:" ))
R = float(input("Enter the rate of Interest:" ))
  
    
simple_interest = Cal(P,T,R)
print("simple Interest:", simple_interest)