def sum(x,y):
    res = {}
    res['h']= x['h']+y['h']
    res ['m']=x['m']+y['m']
    res['s']=x['s']+y['s']
    if res['s'] >= 60:
        res['s']= res['s'] - 60
        res['m']= res['m'] + 1
    if res['m']>= 60:
        res['m']= res['m'] - 60
        res['h']= res['h'] + 1

    return res

def sub(x,y):
    res = {}
    res['h']= x['h']-y['h']
    res ['m']=x['m']-y['m']
    res['s']=x['s']-y['s']
    if res['s'] < 0:
        pass
    if res['m'] < 0:
        pass
    if res['h'] < 0:
        sub(y,x)
    