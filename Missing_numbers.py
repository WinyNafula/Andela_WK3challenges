
#forming a function that holds a list 
def missing_number_list(listednumbers):

    missing_values_list = list()
    
    sorted_list = sorted(listednumbers)
    upper = sorted_list[-1]
    lower = sorted_list[0]
    if len(sorted_list) == 0:
        return "invalid input"

#Using inbuilt function isinstance to check if listed numbers is a subclass of list
    if not isinstance(listednumbers, list):
        return 'only lists are allowed'
    
    for i in range(lower,upper):
        if i not in listednumbers:
            missing_values_list.append(i)

    return missing_values_list


if __name__ == '__main__':
    listednumber = [1, 2, 3, 5, 6, 7, 9]
    print(missing_number_list(listednumber))
