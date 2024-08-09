def filter_odd(sia):
    evens = []
    for sia in sia:
        if sia % 2 == 0:
            evens.append(sia)
    return evens

sia = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
filtered = filter_odd(sia)
print(filtered)
#როგორ გამოვიძახოთ ფუნქცია def filter_odd სახელი ფუნქციის ჩვენ ფუნქციის დასასრულში უნდა ჩავწერით print(ფუნქციის სახელი ანუ filtered_odd)z