if __name__ == '__main__': 
    Ps = 23
    Gs = 9 
    print('Value of Ps is : %d'%(Ps))
    print('Value of Gs is : %d'%(Gs))
    
    g = 4
    print('Private Key g is: %d'%(g))
    
    p = int(pow(Gs,g,Ps)) 
    h = 3
    print('Private Key h is : %d'%(h))
    
    q = int(pow(Gs,h,Ps)) 
    
    K_A = int(pow(q,g,Ps))
    
    K_B = int(pow(p,h,Ps))
     
    print('Joy\'s Secret key is : %d'%(K_A))
    print('Happy\'s Secret key is : %d'%(K_B))
