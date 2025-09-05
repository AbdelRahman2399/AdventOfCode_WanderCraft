from aocd import get_data
import numpy as np


def getdata():
    session_id = '53616c7465645f5f79bff3e09207f2fd73dda95c225238bbca4f653337b69eb957e275e76ddab8e7e0316fe2ea281fd7e15dc2c40f4524995666ca5b7563c7ab'
    data = get_data(session=session_id,day=2, year=2024)
    return data

def main():
    
    data = getdata()
    #print(data)
    data_split1 = data.split("\n")
    #print(data_split1)
    arri = []
    arri = np.array(arri)
    listj = []
    for i in range(0,len(data_split1)):
        data_split2 = data_split1[i].split(' ')
        #print(data_split2)
        for j in range(0,len(data_split2)):
            listj.append(int(data_split2[j]))
        
        arrj = np.array(listj)
        asc_arrj = np.sort(arrj)
        des_arrj = asc_arrj[::-1]
        sarrj = str(arrj)
        sasc_arrj = str(asc_arrj)
        sdes_arrj = str(des_arrj)
        if sarrj == sasc_arrj or sarrj == sdes_arrj:
            us = 0
            for k in range(0,len(arrj)-1):
                d = abs(arrj[k+1] - arrj[k])
                if d > 3 or d < 1:
                    arri = np.append(arri,'unsafe')
                    us = 1
                    break
                d = 0
            if us != 1:
                arri = np.append(arri,'safe')
        else:
            arri = np.append(arri,'unsafe')
        listj = []
    #print(arri)
    unique, counts = np.unique(arri, return_counts=True)
    res = dict(zip(unique,counts))
    print(res['safe'])
    
        
            
    
if __name__ == '__main__':
    main()