def sumfrac(x, y):
    res = {}
    res['numer']= x['numer']*y['denumer']+y['numer']*x['denumer']
    res['denumer']= x['denumer']*y['denumer']
    #if res['numer']%res['denumer'] == 0:
        #return res['numer']/res['denumer']
    #else:    
    return res


def mul(x,y):
    res = {}
    res['numer']= x['numer']*y['numer']
    res['denumer']= x['denumer']*y['denumer']
    return str(res['numer'])+'/'+str(res['denumer'])
def getsm(dic):
    s = int(input(''))
    denumer = int(input('')) 
    dic['numer']= s
    dic['denumer']= denumer
a={}
getsm(a)
b={}
getsm(b)

print(mul(a,b))



