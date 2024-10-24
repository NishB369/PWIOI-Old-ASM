class MyArray:
    def __init__(self, cap: int) -> None:
        self.__cap = cap
        self.__size = 0
        self.__data = [None] * cap

    def __getitem__(self, ind: int) -> int:
        if 0 <= ind < self.__size:
            return self.__data[ind]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, ind: int, val: int) -> None:
        if 0 <= ind < self.__size:
            self.__data[ind] = val
        else:
            raise IndexError("Index out of range")
        
    def __resize(self) -> None:
        arr2 = [None] * (2 * self.__cap)
        for i in range(self.__size):
            arr2[i] = self.__data[i]
        self.__data = arr2
        self.__cap *= 2
        
    def append(self, val: int) -> None:
        if self.__size >= self.__cap:
            self.__resize()
        self.__data[self.__size] = val
        self.__size += 1
        
    def __str__(self) -> str:
        return str(self.__data[:self.__size])
    
    def insert(self, ind: int, val: int) -> None:
        if ind>(self.__size+1):
            raise IndexError('Index Out of Range')

        else:
            if self.__size >= self.__cap:
                self.__resize()
            
            for i in range(self.__size,ind-1,-1):
                self.__data[i+1]=self.__data[i]
                
            self.__data[ind]=val
            self.__size+=1
            
    def delete(self, ind: int) -> None:
        if ind>(self.__size-1):
            raise IndexError('Index Out of Range')

        else:
            if self.__size >= self.__cap:
                self.__resize()
            
            for i in range(self.__size,ind,-1):
                self.__data[i-1]=self.__data[i]
                
            self.__size-=1
            
    def __len__(self) -> int:
        return self.__size
    
    def IsEmpty(self) -> int:
        if self.__size==0:
            return True
        return False
    
    def right_rotate(self,k:int)->None:
        k=k%self.__size
        self.__data = (self.__data[-k:] + self.__data[:-k])
        
    def reverse(self) -> None:
        if self.__size % 2 == 0:
            ind = self.__size // 2
        else:
            ind = (self.__size // 2) - 1
            
        for i in range(ind + 1):
            self.__data[i], self.__data[self.__size - i - 1] = self.__data[self.__size - i - 1], self.__data[i]
            
    def prepend(self, val) -> None:
        if self.__size == self.__cap:
            self.__resize()
        for i in range(self.__size,-1,-1):
            self.__data[i+1]=self.__data[i]
        self.__data[0]=val
        self.__size+=1
        
    def extend(self, arr: list) -> None: #merge
        self.__cap= self.__size + len(arr)
        if self.__size >= self.__cap:
            self.__resize()
            
        for k in range(len(arr)):
            self.__data.append(arr[k])
            self.__size+=1     
            
    def interleave(self, arr: list) -> list:
        new_arr=[]
        i=j=0
        while i<self.__size and j<len(arr):
            new_arr.append(self.__data[i])
            i+=1
            new_arr.append(arr[j])
            j+=1
        
        if len(arr)<self.__size:
            for k in range(i,self.__size):
                new_arr.append(self.__data[k])
        else:
            for m in range(j,len(arr)):
                new_arr.append(arr[m])
            
        return new_arr
    
    def mid(self) -> None:
        if self.__size % 2 == 0:
            ind = self.__size // 2 - 1
        else:
            ind = (self.__size // 2)
        
        return self.__data[ind]
    
    def locate(self, val:int) -> int:
        flag=False
        for i in range(self.__size):
            if self.__data[i]==val:
                flag=True
                break
        if flag:
            return i
        return -1
    
    def split_array(self, ind:int):
        return (self.__data[:ind],self.__data[ind:self.__size])
    
    def cust_resize(self, factor:int) -> None:
        arr2 = [None] * (factor * self.__cap)
        for i in range(self.__size):
            arr2[i] = self.__data[i]
        self.__data = arr2
        self.__cap *= factor
