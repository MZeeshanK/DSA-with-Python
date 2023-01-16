list = [4,2,3,6,1,5,2]

# Selection Sort
def selection_sort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i,len(list)):
            if list[j] < list[min]:
                min = j
            
        temp = list[i]
        list[i] = list[min]
        list[min] = temp

    print(list)

#insertion Sort
def insertion_sort(list):
    for i in range(1,len(list)):
        j = i
        while list[j-1] > list[i] and j> 0:
            list[j-1], list[j] = list[j],list[j-1]
            j -= 1
            
    print(list)

# bubble sort
def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    print(list)




# quick sort
def quick_sort(list,left,right):
    if left < right:
        pos = partition(list,left,right)
        quick_sort(list, left, pos-1)
        quick_sort(list, pos + 1, right)
    return list    

def partition(list,left,right):
    i = left
    j = right -1 
    pivot = list[right]

    while i < j:
        while i < right and list[i] < pivot:
            i += 1
        while j > left and list[j]>= pivot:
            j -=1

        if i< j:
            list[i],list[j] = list[j],list[i]
    
    if list[i] >pivot:
        list[i],list[right] = list[right],list[i]

    return i 
    

#merge sort 
def merge_sort(list):
    if len(list)>1:
        left_list = list[0:len(list)//2]
        right_list = list[len(list)//2:len(list)]

        #recursion
        merge_sort(left_list)
        merge_sort(right_list)

        #merge
        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i+=1
            else:
                list[k] = right_list[j]
                j+=1

            k+=1

        while i < len(left_list):
            list[k] = left_list[i]
            i+=1
            k+=1
        
        while j < len(right_list):
            list[k] = right_list[j]
            j+=1
            k+=1

list= [3,4,1,3,5,6,2,3,5,2]
merge_sort(list)

print(list)
                


        





