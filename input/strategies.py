#Example strategies file
import numpy as np

def s02_ALLD(actions,periods):
    '''Always defect strategy'''
    T = len(actions)
    out = np.zeros(T)
    out[np.isnan(actions)]=np.nan
    return out

def s01_ALLC(actions,periods):
    '''Always cooperate strategy'''
    T = len(actions)
    out = np.ones(T)
    out[np.isnan(actions)]=np.nan
    return out

def s03_TFT(actions,periods):
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

def s10_GRIM(actions,periods):
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

def s04_DTFT(actions,periods):
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

def s15_CTOD(actions,periods):
    '''C to D strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=1
        else:
            out[t]=0
    out[np.isnan(actions)]=np.nan
    return out

def s20_DCALT(actions,periods):
    '''DC Alternator strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=0
        else:
            out[t]=1-out[t-1]
    out[np.isnan(actions)]=np.nan
    return out

def s05_TF2T(actions,periods):
    '''Tit-for-two-tats strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]<=2:
            out[t]=1
        else:
            if actions[t-1]==0 and actions[t-2]==0:
                out[t]=0
            else:
                out[t]=1
    out[np.isnan(actions)]=np.nan
    return out

def s06_TF3T(actions,periods):
    '''Tit-for-three-tats strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]<=3:
            out[t]=1
        else:
            if actions[t-1]==0 and actions[t-2]==0 and actions[t-3]==0:
                out[t]=0
            else:
                out[t]=1
    out[np.isnan(actions)]=np.nan
    return out

def s11_GRIM2(actions,periods):
    '''Lenient Grim 2 trigger strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]<=2:
            out[t]=1
        else:
            if actions[t-1]==0 and actions[t-2]==0:
                out[t]=0
            else:
                out[t]=out[t-1]
    out[np.isnan(actions)]=np.nan
    return out
    
def s12_GRIM3(actions,periods):
    '''Lenient Grim 3 trigger strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]<=3:
            out[t]=1
        else:
            if actions[t-1]==0 and actions[t-2]==0 and actions[t-3]==0:
                out[t]=0
            else:
                out[t]=out[t-1]
    out[np.isnan(actions)]=np.nan
    return out

def s13_WSLS(actions,periods):
    '''Win-stay-lose-shift strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=1
        else:
            if actions[t-1]==1 and out[t-1]==1:
                out[t]=1
            elif actions[t-1]==0 and out[t-1]==0:
                out[t]=1
            else:
                out[t]=0
    out[np.isnan(actions)]=np.nan
    return out

def s16_DTF2T(actions,periods):
    '''Suspicious-Tit-for-two-tats strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=0
        elif periods[t]==2:
            out[t]=1
        else:            
            if actions[t-1]==0 and actions[t-2]==0:
                out[t]=0
            else:
                out[t]=1
                    
    out[np.isnan(actions)]=np.nan
    return out

def s17_DTF3T(actions,periods):
    '''Suspicious-Tit-for-three-tats strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=0
        elif periods[t]==2 or periods[t]==3:
            out[t]=1
        else:            
            if actions[t-1]==0 and actions[t-2]==0 and actions[t-3]==0:
                out[t]=0
            else:
                out[t]=1
                    
    out[np.isnan(actions)]=np.nan
    return out



def s18_DGRIM2(actions,periods):
    '''Suspicious-Lenient-Grim-2'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=0
        elif periods[t]==2:
            out[t]=1
        else:            
            if min(out[t-1],actions[t-1])==0 and min(out[t-2],actions[t-2])==0:
                out[t]=0
            else:
                out[t]=1
                    
    out[np.isnan(actions)]=np.nan
    return out




def s07_TWOTFT(actions,periods):
    '''Two-Tits-for-one-tat strategy'''
    T = len(actions)
    out = np.ones(T)
    
    for t in range(T):
        if periods[t]==1:
            out[t]=1
            punish=0
        else:            
            if punish==0:
                if actions[t-1]==0:
                    out[t]=0
                    punish=1
                else:
                    out[t]=1
                    punish=0
            else:
                if actions[t-1]==0:
                    out[t]=0
                    punish=1
                else:
                    out[t]=0
                    punish=0
                    
    out[np.isnan(actions)]=np.nan
    return out

def s08_TWOTF2T(actions,periods):
    '''Two-Tits-for-two-tats strategy'''
    T = len(actions)
    out = np.ones(T)
    
    for t in range(T):
        if periods[t]<=2:
            out[t]=1
            punish = 0
        else:            
            if actions[t-1]==0 and actions[t-2]==0 and punish==0:
                out[t]=0
                punish=1
            else:
                if punish==1:
                    out[t]=0
                    punish=punish-actions[t-1]
                else:
                    out[t]=1
                    punish=0

                    
    out[np.isnan(actions)]=np.nan
    return out


def s09_T2(actions,periods):
    '''T2 Strategy'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=1
            punish=0
        else:            
            if punish==0:
                if actions[t-1]==0:
                    out[t]=0
                    punish=2
                else:
                    out[t]=1
                    punish=0
            elif punish==2:
                out[t]=0
                punish=1
            else:
                out[t]=1
                punish=0
                    
    out[np.isnan(actions)]=np.nan
    return out


def s14_TWOWSLS(actions,periods):
    '''Win-stay-lose-shift strategy'''
    T = len(actions)
    out = np.ones(T)
    state=1
    for t in range(T):
        if periods[t]==1:
            state=1
            out[t]=1
            
        else:
            if state==1:
                if actions[t-1]==1:
                    out[t]=1
                    state=1
                else:
                    out[t]=0
                    state=2
            elif state==2:
                if actions[t-1]==1:
                    out[t]=0
                    state=2
                else:
                    out[t]=0
                    state=3
            else:
                if actions[t-1]==1:
                    out[t]=0
                    state=2
                else:
                    out[t]=1
                    state=1         
    out[np.isnan(actions)]=np.nan
    return out


# Need to check

def s19_DGRIM3(actions,periods):
    '''Suspicious-Lenient-Grim-3'''
    T = len(actions)
    out = np.ones(T)
    for t in range(T):
        if periods[t]==1:
            out[t]=0
        elif periods[t]==2 or periods[t]==3:
            out[t]=1
        else:            
            if min(out[t-1],actions[t-1])==0 and min(out[t-2],actions[t-2])==0 and min(out[t-3],actions[t-3])==0:
                out[t]=0
            else:
                out[t]=1
                    
    out[np.isnan(actions)]=np.nan
    return out