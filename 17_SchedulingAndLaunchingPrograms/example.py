from time import time
def calcProd():
    product = 1
    for i in range(1,101):
        product = product * i
    print(product)
    return product


start = time()
prod = calcProd()
end = time()

print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (end - start))

