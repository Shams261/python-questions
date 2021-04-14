## by using advance min_max function try to findout the problems

# findout the length of maximum names 
def name(item):
    return len(item)
names = ['asfdasf','dgdfzhb','asf','zsbfxsatfeuihsdk']
print(max(names , key = name))

# or we can do the samae problem by like list comprehension

names = ['asfdasf','dgdfzhb','asf','zsdk']
print(max(names , key = lambda item : len(item)))

## SUPOSE HERE IS LIST IN WHICH WE WANAT TO FINIDOUT THE NAME BY SCORE OR ANY OTHER VARIABLE

students = [
    {'name': 'shams','score':90 , 'age':20},
    {'name': 'tabrez','score':46 , 'age':26},
    {'name': 'azaan','score':265, 'age':27},
    {'name': 'zain','score':120 , 'age':24}
]
print(max(students, key = lambda item :item.get('age'))['name']) ## here you can get the value by any var

## SUPOSE HERE IS DICT IN WHICH WE WANAT TO FINIDOUT THE NAME BY SCORE OR ANY OTHER VARIABLE

students2 = {
    'akhtar': {'score':90 , 'age':20},
    'aryan': {'score':46 , 'age':26},
    'aman': {'score':265, 'age':27},
    'ali': {'score':120 , 'age':24}
}

print(min(students2, key = lambda item :students2[item]['age']))

