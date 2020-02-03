#Example strategies file
import numpy as np

def ALLD(actions,periods):
    '''Always defect strategy'''
    T = len(actions)
    out = np.zeros(T)
    out[np.isnan(actions)]=np.nan
    return out

def ALLC(actions,periods):
    '''Always cooperate strategy'''
    T = len(actions)
    out = np.ones(T)
    out[np.isnan(actions)]=np.nan
    return out

def TFT(actions,periods):
    '''Tit-for-tat strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=1
        else:
            out[t]=actions[t-1]
    out[np.isnan(actions)]=np.nan
    return out

def GRIM(actions,periods):
    '''Grim trigger strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=1
        else:
            out[t]=min(out[t-1],actions[t-1])
    out[np.isnan(actions)]=np.nan
    return out

def DTFT(actions,periods):
    '''Suspicious Tit-for-Tat strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=0
        else:
            out[t]=actions[t-1]
    out[np.isnan(actions)]=np.nan
    return out