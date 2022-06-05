#Method Resolution Order(MRO)

#case 1
class A:
    def father(self):
        print("My father is my Life ")
        
class B:
    pass

class C(A,B):
    pass
c1 = C()
c1.father()
print(C.mro())   

#Case 2
class A:
    def father(self):
        print("Fathar has home")
        
class B:
    def father(self):
        print("#daughter")
        
class C(A,B):
    pass

obj = C()
obj.father() 

#Case 3
class A:
    def father(self):
        print("father has 3 daughter")
        
class B:
    def father(self):
        print("Srabonti Sen Neeti")    
        
        
        
        
        
class State:
    def __init__(self):
        print("Main State")                            

class SecState():
    def __init__(self):
        print("Second State")

        
class FourthState():
    def __init__(self):
        print("Fourth State")

class ThirdState(State,SecState,FourthState):
    def __init__(self):
        print("Third State")
        State.__init__(self) #super.__init__()
        super(State,self).__init__()
        super(SecState,self).__init__()

        
                        
ses = ThirdState()                        
