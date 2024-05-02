def binary_search(
    L : list[int],
    search_data : int,
    start_index : int ,
    end_index : int
):
    if(start_index >= end_index):
        return False
    
    mid_index = (start_index + end_index) // 2

    if(search_data == L[mid_index]):
        return True
    elif(search_data < L[mid_index]):
        return binary_search(L ,search_data ,start_index ,mid_index - 1)
    else:
        return binary_search(L ,search_data ,mid_index + 1 ,end_index)

Data = [11 ,21 ,51, 101 ,121 ,151]
ret = binary_search(Data ,51 ,0 ,len(Data)-1)
print(ret)
