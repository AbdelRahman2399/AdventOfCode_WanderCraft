from aocd import get_data
import numpy as np


def getdata():
    session_id = '53616c7465645f5f79bff3e09207f2fd73dda95c225238bbca4f653337b69eb957e275e76ddab8e7e0316fe2ea281fd7e15dc2c40f4524995666ca5b7563c7ab'
    data = get_data(session=session_id,day=4, year=2024)
    return data

def count_horizontal(hor_data):
    count = 0
    for i in range(0,len(hor_data)):
        index = 0
        while True:
            index = hor_data[i].find('X')
            #print(in)
            if index == -1:
                break
            if index >= 3:
                if (hor_data[i][index] + hor_data[i][index-1] + hor_data[i][index-2] + hor_data[i][index-3]) == 'XMAS':
                    count = count + 1
            if index <= len(hor_data) - 4:
                if (hor_data[i][index] + hor_data[i][index+1] + hor_data[i][index+2] + hor_data[i][index+3]) == 'XMAS':
                    count = count + 1
            #print(ver_data[i])
            hor_data[i] = hor_data[i][:index] + 'N' + hor_data[i][index + 1: ]
            
    return count

def count_vertical(ver_data):
    #print(data)
    count = 0
    for i in range(0,len(ver_data)):
        index = 0
        while True:
            index = ver_data[i].find('X')
            #print(in)
            if index == -1:
                break
            if i >= 3:
                if (ver_data[i][index] + ver_data[i-1][index] + ver_data[i-2][index] + ver_data[i-3][index]) == 'XMAS':
                    count = count + 1
            if i <= len(ver_data) - 4:
                if (ver_data[i][index] + ver_data[i+1][index] + ver_data[i+2][index] + ver_data[i+3][index]) == 'XMAS':
                    count = count + 1
            #print(ver_data[i])
            ver_data[i] = ver_data[i][:index] + 'N' + ver_data[i][index + 1: ]
            
    return count

def count_diag1(diag_data):
    #print(data)
    count = 0
    for i in range(0,len(diag_data)):
        index = 0
        while True:
            index = diag_data[i].find('X')
            #print(in)
            if index == -1:
                break
            if index >= 3 and i >=3:
                if (diag_data[i][index] + diag_data[i-1][index-1] + diag_data[i-2][index-2] + diag_data[i-3][index-3]) == 'XMAS':
                    count = count + 1
            if i <= len(diag_data) - 4 and index <= len(diag_data) - 4:
                if (diag_data[i][index] + diag_data[i+1][index+1] + diag_data[i+2][index+2] + diag_data[i+3][index+3]) == 'XMAS':
                    count = count + 1
            #print(ver_data[i])
            diag_data[i] = diag_data[i][:index] + 'N' + diag_data[i][index + 1: ]
            
    return count


def count_diag2(diag_data2):
    #print(data)
    count = 0
    for i in range(0,len(diag_data2)):
        index = 0
        while True:
            index = diag_data2[i].find('X')
            #print(in)
            if index == -1:
                break
            if index <= len(diag_data2) - 4 and i >= 3:
                if (diag_data2[i][index] + diag_data2[i-1][index+1] + diag_data2[i-2][index+2] + diag_data2[i-3][index+3]) == 'XMAS':
                    count = count + 1
            if i <= len(diag_data2) - 4 and index >= 3:
                if (diag_data2[i][index] + diag_data2[i+1][index-1] + diag_data2[i+2][index-2] + diag_data2[i+3][index-3]) == 'XMAS':
                    count = count + 1
            #print(ver_data[i])
            diag_data2[i] = diag_data2[i][:index] + 'N' + diag_data2[i][index + 1: ]
            
    return count

                    

def main():
    data = getdata()
    data_split1 = data.split("\n")
    counth =  count_horizontal(data_split1[:])
    print(counth)
    countv =  count_vertical(data_split1[:])
    print(countv)
    countd1 = count_diag1(data_split1[:])
    print(countd1)
    countd2 = count_diag2(data_split1[:])
    print(countd2)
    count_total = counth + countv + countd1 + countd2
    print(count_total)
    
    
    
    
if __name__ == '__main__':
    main()