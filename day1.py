from aocd import get_data
import numpy as np



def getdata():
    session_id = '53616c7465645f5f79bff3e09207f2fd73dda95c225238bbca4f653337b69eb957e275e76ddab8e7e0316fe2ea281fd7e15dc2c40f4524995666ca5b7563c7ab'
    data = get_data(session=session_id,day=1, year=2024)
    return data

def calculatedist(arr1,arr2):
    dist = 0
    for i in range(0, len(arr1)):
        dist = dist + abs(arr1[i] - arr2[i])
    return dist


def main():
    datastring = getdata()
    
    newdata = datastring.split("\n")
    
    arr1 = []
    arr2 = []
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    for i in range(0, len(newdata)):
        comb = newdata[i].split('   ')
        arr1 = np.append(arr1,int(comb[0]))
        arr2 = np.append(arr2,int(comb[1]))

    arr1 = np.sort(arr1)
    arr2 = np.sort(arr2)
    
    dist = calculatedist(arr1,arr2)
        
    print(dist)
    
    



if __name__ == '__main__':
    main()