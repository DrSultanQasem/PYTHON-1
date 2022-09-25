
class convert ():
    global fr 
    def __init__(self,fr,frk,tok):
        
        self.fr=fr
        self.frk=frk
        self.tok=tok     
        
    def fr_bi_to_bi(self):
        return (self.fr)
    
    
    
    def fr_bi_to_de(self):
        return(int(str(self.fr),2))
        #self.fr must be string
    def fr_de_to_bi(self):
        return bin(self.fr).replace("0b","BINARY : ")



    def fr_bi_to_oc(self):
        return(oct(self.fr)).replace("0o","OCTAL : ")
        #note must enter number 0b???
    def fr_oc_to_bi(self):
        return(bin(self.fr)).replace("0b","BINARY : ")
        #note must enter number 0o???    
    

    def fr_bi_to_hx(self):
        return(hex(self.fr)).replace("0x","HEXA : ")
        #note must enter number 0b???
    def fr_hx_to_bi(self):
        return(bin(self.fr)).replace("0b","BINARY : ")
        #note must enter number 0x??? & CAPITAL ELEMNT
    
    
    
    
    
q1=convert(0xF,'x','x')
#print(q1.fr)
#print(q1.frk)
#print(q1.tok)
#print(q1.fr_bi_to_bi())
#print(q1.fr_bi_to_de())
#print(q1.fr_de_to_bi())
#print(q1.fr_bi_to_oc())
#print(q1.fr_oc_to_bi())
#print(q1.fr_bi_to_hx())
print(q1.fr_hx_to_bi())




