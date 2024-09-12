FN bubbleSort(array)
    
  # loop to access each array element
  FOR i RANGE LEN(array) THEN

    # loop to compare array elements
    FOR j RANGE len(array)-1 BY 1 THEN

      # compare two adjacent elements
      # change > to < to sort in descending order
      IF array/j > array/j + 1 THEN


        # swapping elements if elements
        # are not in the intended order
        LET temp = array/j
        array/j = array/j+1
        array/j+1 = temp


LET data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
