def merge_sort(list1):

    if len(list1) > 1:

        mid =  len(list1) // 2
        left_sublist =  list1[:mid]
        right_sublist = list1[mid:]

        merge_sort(left_sublist)
        merge_sort(right_sublist)

        i = 0 
        j = 0 
        k = 0

        while i< len(left_sublist) and j< len(right_sublist):

            if(left_sublist[i]<right_sublist[j]):
                list1[k] = left_sublist[i]
                i+=1
                k+=1
            
            else:
                list1[k] = right_sublist[j]
                j+=1
                k+=1
        while  len(left_sublist)> i:
            list1[k] = left_sublist[i]
            i+=1
            k+=1
        while len(right_sublist) > j:
            list1[k] = right_sublist[i]
            j+=1
            k+=1

    return list1
        