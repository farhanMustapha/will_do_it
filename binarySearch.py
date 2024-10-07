list=[1,4,6,8,9,12,14,34,40]
def binary_search(list,item):
    low_index=0
    high_index=len(list)-1
    while low_index<=high_index:
        mid_index=(low_index+high_index)//2
        guss=list[mid_index]
        if guss==item:
            return mid_index
        if guss>item:
            high_index=mid_index-1
        else:
            low_index=mid_index+1
    return None

print(binary_search(list,6))
        