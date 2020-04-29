def sparse_search(data, search_val):
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))
    first = 0
    last = len(data)
    while first <= last :
        mid = (first + last) // 2 #median point
        if data[mid] == "" : #check surrounding values if median point is empty
            left = mid - 1
            right = mid + 1
            canContinue = True
            while canContinue :
                if left < first and right > last: #check to see if iterated through entire dataset
                    print("{} is not in the dataset".format(search_val))
                    return None
                elif right <= last and data[right] != "" : #checks to if right data point exists and is not empty
                    mid = right
                    break
                elif left >= first and data[left] != "" : #check to if left data point exists and is not empty
                    mid = left
                    break
                else : #change pointers to check two next outer variables
                    left -= 1
                    right += 1
                    continue
        if data[mid] == search_val : #check if mid value is sought value
            print("{} found at position {}".format(search_val, mid))
            return mid
        elif search_val < data[mid] : #check if mid value is lower half of dataset
            last = mid - 1
        elif search_val > data[mid] : #check if mid value is upper half of dataset
            first = mid + 1
    print("{} is not in the dataset".format(search_val))
    return None
        
                    
