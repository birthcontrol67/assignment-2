def max_product_of_three(array):
    n = len(array)
    array.sort()
    product1 = array[n-1] * array[n-2] * array[n-3]
    product2 = array[0] * array[1] * array[n-1]
    return max(product1, product2)

numbers = [1, -5, 2, -2, 11]
print(max_product_of_three(numbers))
