def even_sum(sia):
    jami = 0  
    for number in sia: 
        if number % 2 == 0:
            jami += number  
    return jami  

sia = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = even_sum(sia)
print(result)  
