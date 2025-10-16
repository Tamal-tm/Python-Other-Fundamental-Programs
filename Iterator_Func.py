nums=[1,2,3,4,5] 

iterate=iter(nums)
print(iterate.__next__())
print(iterate.__next__())
print(next(iterate))

# Creating an iterator.

class Fantastic_Five:
    def __init__(self):
        self.num=1

    def __iter__(self): # Object.
        return self
    
    def __next__(self): # Will call next number. 
        if self.num<=5:
            value=self.num
            self.num +=1
            return value
        else:
            raise StopIteration
        
FF=Fantastic_Five()

for i in FF:
    
    print(i)










