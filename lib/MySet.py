class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self,value):
        return value in self.dictionary
    
    def __str__(self):
        set_list=[]
        for key,value in self.dictionary.items():
            set_list.append(str(key))

        return f'MySet: {{{",".join(set_list)}}}'

    def add(self,value):
        self.dictionary[value]=True
        return self
    
    def delete(self,value):
        self.dictionary.pop(value,None)
        return self

    def size(self):
        len(self.dictionary)

    def clear(self):
        self.dictionary.clear()
    
    

    # def first_repeated_value(list):
    #     for i in range(0,len(list)):
    #         for j in range(i+1, len(list)):
    #             if list[i]==list[j]:
    #                 return list[i]
    #     return None
    
    # print(first_repeated_value([1,2,2,3,2,4,5,6,7,7]))

   