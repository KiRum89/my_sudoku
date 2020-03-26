import numpy as np

#pretty printing functions
def stringify(row):
    s = ''
    i=0
    for el in row:
        if el!=0:
            s+=str(int(el))+' '
            i+=1
            if i%3==0:
                s+='|'
        else:
            s+='x'+' '
            i+=1
            if i%3==0:
                s+='|'

    return s
def myPrint(data):
    s = ''
    i = 0
    for row in data:
    
        s += stringify(row)+'\n'
        i+=1
        vl=''
        if i%3==0:
            for j in range(0,10):
                vl += ' _'
            vl+='\n'
        s += vl

    return s
#example: print myPrint(data)
###
#some examples
def initData2():
    data = np.array([[0,0,0,2,4,0,5,0,0],\
    [6,0,7,0,0,0,0,0,0],\
    [0,5,0,8,0,0,0,0,0],\
    [4,0,0,0,1,0,0,0,0],\
    [0,0,0,0,0,4,0,1,0],\
    [0,6,0,0,5,0,0,3,0],\
    [3,0,0,0,0,1,0,0,6],\
    [8,0,0,0,0,6,4,7,0],\
    [7,0,6,0,0,0,8,0,1]])
    return data
def initData3():
    data = np.array([[1,0,6,0,0,2,3,0,0],\
    [0,5,0,0,0,6,0,9,1],\
    [0,0,9,5,0,1,4,6,2],\
    [0,3,7,9,0,5,0,0,0],\
    [5,8,1,0,2,7,9,0,0],\
    [0,0,0,4,0,8,1,5,7],\
    [0,0,0,2,6,0,5,4,0],\
    [0,0,4,1,5,0,6,0,9],\
    [9,0,0,8,7,4,2,1,0]])
    return data


#block limits
def getBlockOf(data,arg):
    n,m=arg
    if 0<=n<3:
        slice1 = data[0:3]
    elif 3<=n<6:
        slice1 = data[3:6]
    elif 6<=n<9:
        slice1 = data[6:9]
    if 0<=m<3:
        slice2 = slice1[:,0:3]
        ##print slice1,slice2
    elif 3<=m<6:
        slice2 = slice1[:,3:6]
    elif 6<=m<9:
        slice2 = slice1[:,6:9]

    return slice2

def goal1(arr):

    arr = arr.flatten()
     
    indxs = np.where(arr!=0)[0]
    arr = arr[indxs]
    arrUnique = np.unique(arr) 
    if len(arr)!=len(arrUnique):
        return False
    else:
        return True
def goal2(n,m,data):
    if goal1(data[:,m]) and  goal1(data[n,:]):
        return True
    else:
        return False

def ind2nm(ind,colCount):
    #transform index of flat array to [n,m] coordinate of 2d Array.
    #The 2d Array represents the sudoku
    if ind%colCount!=0:
        m = ind%colCount
        n = (ind-m)/9  
        return [n,m]
    else:
        return [ind/9,ind%9]


def solve(data,ind,depth):
    #ind is index of element in a flatted array
    #ind2nm transform ind to [n,m] coordinates    
    #depth is not used
    if ind<=80:
        [n,m]=ind2nm(ind,9)
        if data[n,m]==0:
            for i in range(1,10):
                #try a number i at [n,m]
                data[n,m] = i
                block = getBlockOf(data,[n,m])
                if goal1(block) and goal2(n,m,data):
                    data=solve(data,ind+1,depth+1)
                    if np.size(np.where(data==0))==0:
                        #no more empty elements-> the game is complete
                        return data
                else:
                    #i didn't work, set [n,m] back to 0
                    data[n,m]=0
        else:
            #skip a pre-defined (!=0) value
            data=solve(data,ind+1,depth+1)
    return data

data = initData3()    
dataInit = data.copy()
data = solve(data,0,0)


print 'initial'
print myPrint(dataInit)
print 'result' 
print myPrint(data)

    
                        
    


