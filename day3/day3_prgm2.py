try:
    arr=[1,6,7,8,9]
    print(arr[41])
except IndexError:
    print('cannot access index value')
else:
    print('no exception occured')
finally:
    print('finally wednesday s a last day of trip')