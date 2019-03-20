
# forming a function that holds a list yet to be sorted.
def list_sort(list1):

    even = []
    odd = []
    characters = []
    
    mydict = dict()
    
#Using inbuilt function isinstance to check if list1 is a subclass of list.
    if not isinstance(list1, list):
        return 'Invalid Input'

    if not list1:
        mydict['evens'] = even
        mydict['odds'] = odd
        mydict['chars'] = characters
        return mydict

    for i in list1:

        if isinstance(i, int):
            if i % 2 == 0:
                even.append(i)
            
            else:
                odd.append(i)

        elif isinstance(i, str):
            characters.append(i)

    mydict['evens'] = sorted(even)
    mydict['odds'] = sorted(odd)
    mydict['chars'] = sorted(characters)
    return mydict


print(list_sort([2, 0, 6, 5, 1, 7, 'a', 'z']))
