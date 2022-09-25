### MY FUNCTIONS ###

def fr_bi_to_bi(x):
    return (x)
def fr_bi_to_de(x):
    return(int(str(x),2))
def fr_de_to_bi(x):
    return bin(x).replace("0b","")
def fr_de_to_oc(x):
    return(oct(x)).replace("0o","")
def fr_oc_to_de(x):
    return(int(str(x),8))    
def fr_de_to_hx(x):
    return(hex(x)).replace("0x","")


"""
print("This from binary to binary",fr_bi_to_bi(101))
print("This from binary to decimal",fr_bi_to_de(101))
print("This from decimal to binary",fr_de_to_bi(101))
print("This from decimal to octal",fr_de_to_oc(101))
print("This from octal to decimal",fr_oc_to_de(101))
print("This from decimal to hexa",fr_de_to_hx(101)) 
"""
##################1
def fr_bi_to_oc(x):
    x_1=fr_bi_to_de(x)
    x_2=fr_de_to_oc(x_1)
    return(x_2)
print("This from binary to octal",fr_bi_to_oc(101))
##################2
def fr_oc_to_bi(x):
    x_1=fr_oc_to_de(x)
    x_2=fr_de_to_bi(x_1)
    return(x_2)
print("This from octal to binary",fr_oc_to_bi(101))
##################3
def fr_bi_to_hx(x):
    x_1=fr_bi_to_de(x)
    x_2=fr_de_to_hx(x_1)
    return(x_2)    
print("This from binary to hexa",fr_bi_to_hx(101))
#################4
def fr_oc_to_hx(x):
    x_1=fr_oc_to_de(x)
    x_2=fr_de_to_hx(x_1)
    return(x_2)
print(fr_oc_to_hx(101))









"""  
######################################################
    def fr_hx_to_oc(self):
        return(oct(self.fr)).replace("0o","OCTAL : ")
        #note must enter number 0x??? & CAPITAL ELEMNT
    def fr_hx_to_bi(self):
        return(bin(self.fr)).replace("0b","BINARY : ")
        #note must enter number 0x??? & CAPITAL ELEMNT
    def fr_hx_to_de(self):
        return(int(self.fr))
    #note must enter number 0x??? & CAPITAL ELEMNT    
######################################################  
 """

#print(fr_hx_to_bi())
#print(fr_hx_to_de())
#print(fr_hx_to_oc())