from aocd import get_data
import numpy as np


def getdata():
    session_id = '53616c7465645f5f79bff3e09207f2fd73dda95c225238bbca4f653337b69eb957e275e76ddab8e7e0316fe2ea281fd7e15dc2c40f4524995666ca5b7563c7ab'
    data = get_data(session=session_id,day=3, year=2024)
    return data

def mul(num1,num2):
    return num1*num2

def main():
    data = getdata()
    #print(data)
    fun_list = []
    valid_list = ['1','2','3','4','5','6','7','8','9','0','(',',',')']
    
    while(True):
        index = data.find('mul')
        #print(index)
        if index == -1:
            break
        for i in range(index + 3, index + 12):
            #print(data[i])
            if data[i] not in valid_list:
                break
            if data[i] == ')':
                if '(' in data[index:i+1] and ',' in data[index:i+1]:
                    fun_list.append(data[index:i+1])
                    break
                else:
                    break
        data = data[index + 4:]
    #print(fun_list)
    sum = 0
    for f in fun_list:
        sum = sum + eval(f)
        #print(sum)
    print(sum)
    
    
    
if __name__ == '__main__':
    main()