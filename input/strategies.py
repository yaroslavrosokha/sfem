# Example strategies file
import numpy as np
import sys

"""     This file contains strategy definitions. Each strategy function takes two lists/arrays as arguments. 
        The first argument is the list of actions. Action are either 1 (=Cooperate) or 0 (=Defect). 
        The second argument is the list of periods. Period 1 signifies start of a new supergame.
        Each function returns a numpy array play of that strategy against a sequence of actions provided.
        """

def s01_allc(actions, periods):
    """Always cooperate strategy"""
    n = len(actions)
    out = np.ones(n)
    out[np.isnan(actions)] = np.nan
    return out


def s02_alld(actions, periods):
    """Always defect strategy"""
    n = len(actions)
    out = np.zeros(n)
    out[np.isnan(actions)] = np.nan
    return out


def s03_tft(actions, periods):
    """Tit-for-tat strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 1
        else:
            out[t] = actions[t - 1]
    out[np.isnan(actions)] = np.nan
    return out


def s04_dtft(actions, periods):
    """Suspicious Tit-for-Tat strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 0
        else:
            out[t] = actions[t - 1]
    out[np.isnan(actions)] = np.nan
    return out


def s05_tf2t(actions, periods):
    """Tit-for-two-tats strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] <= 2:
            out[t] = 1
        else:
            if actions[t - 1] == 0 and actions[t - 2] == 0:
                out[t] = 0
            else:
                out[t] = 1
    out[np.isnan(actions)] = np.nan
    return out


def s06_tf3t(actions, periods):
    """Tit-for-three-tats strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] <= 3:
            out[t] = 1
        else:
            if actions[t - 1] == 0 and actions[t - 2] == 0 and actions[t - 3] == 0:
                out[t] = 0
            else:
                out[t] = 1
    out[np.isnan(actions)] = np.nan
    return out


def s07_2tft(actions, periods):
    """Two-Tits-for-one-tat strategy"""
    n = len(actions)
    out = np.ones(n)
    punish = 0
    for t in range(n):
        if periods[t] == 1:
            out[t] = 1
            punish = 0
        else:
            if punish == 0:
                if actions[t - 1] == 0:
                    out[t] = 0
                    punish = 1
                else:
                    out[t] = 1
                    punish = 0
            else:
                if actions[t - 1] == 0:
                    out[t] = 0
                    punish = 1
                else:
                    out[t] = 0
                    punish = 0

    out[np.isnan(actions)] = np.nan
    return out


def s08_2tf2t(actions, periods):
    """Two-Tits-for-two-tats strategy"""
    n = len(actions)
    out = np.ones(n)
    punish = 0
    for t in range(n):
        if periods[t] <= 2:
            out[t] = 1
            punish = 0
        else:
            if actions[t - 1] == 0 and actions[t - 2] == 0 and punish == 0:
                out[t] = 0
                punish = 1
            else:
                if punish == 1:
                    out[t] = 0
                    punish = punish - actions[t - 1]
                else:
                    out[t] = 1
                    punish = 0

    out[np.isnan(actions)] = np.nan
    return out


def s09_t2(actions, periods):
    """T2 Strategy"""
    n = len(actions)
    out = np.ones(n)
    punish = 0
    for t in range(n):
        if periods[t] == 1:
            out[t] = 1
            punish = 0
        else:
            if punish == 0:
                if actions[t - 1] == 0:
                    out[t] = 0
                    punish = 2
                else:
                    out[t] = 1
                    punish = 0
            elif punish == 2:
                out[t] = 0
                punish = 1
            else:
                out[t] = 1
                punish = 0

    out[np.isnan(actions)] = np.nan
    return out


def s10_grim(actions, periods):
    """Grim trigger strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 1
        else:
            out[t] = min(out[t - 1], actions[t - 1])
    out[np.isnan(actions)] = np.nan
    return out


def s11_grim2(actions, periods):
    """Lenient Grim 2 trigger strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] <= 2:
            out[t] = 1
        else:
            if actions[t - 1] == 0 and actions[t - 2] == 0:
                out[t] = 0
            else:
                out[t] = out[t - 1]
    out[np.isnan(actions)] = np.nan
    return out


def s12_grim3(actions, periods):
    """Lenient Grim 3 trigger strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] <= 3:
            out[t] = 1
        else:
            if actions[t - 1] == 0 and actions[t - 2] == 0 and actions[t - 3] == 0:
                out[t] = 0
            else:
                out[t] = out[t - 1]
    out[np.isnan(actions)] = np.nan
    return out


def s13_wsls(actions, periods):
    """Win-stay-lose-shift strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 1
        else:
            if actions[t - 1] == 1 and out[t - 1] == 1:
                out[t] = 1
            elif actions[t - 1] == 0 and out[t - 1] == 0:
                out[t] = 1
            else:
                out[t] = 0
    out[np.isnan(actions)] = np.nan
    return out


def s14_2wsls(actions, periods):
    """Win-stay-lose-shift strategy"""
    n = len(actions)
    out = np.ones(n)
    state = 1
    for t in range(n):
        if periods[t] == 1:
            state = 1
            out[t] = 1

        else:
            if state == 1:
                if actions[t - 1] == 1:
                    out[t] = 1
                    state = 1
                else:
                    out[t] = 0
                    state = 2
            elif state == 2:
                if actions[t - 1] == 1:
                    out[t] = 0
                    state = 2
                else:
                    out[t] = 0
                    state = 3
            else:
                if actions[t - 1] == 1:
                    out[t] = 0
                    state = 2
                else:
                    out[t] = 1
                    state = 1
    out[np.isnan(actions)] = np.nan
    return out


def s15_ctod(actions, periods):
    """C to D strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 1
        else:
            out[t] = 0
    out[np.isnan(actions)] = np.nan
    return out


def s16_dtf2t(actions, periods):
    """Suspicious-Tit-for-two-tats strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 0
        elif periods[t] == 2:
            out[t] = 1
        else:
            if actions[t - 1] == 0 and actions[t - 2] == 0:
                out[t] = 0
            else:
                out[t] = 1

    out[np.isnan(actions)] = np.nan
    return out


def s17_dtf3t(actions, periods):
    """Suspicious-Tit-for-three-tats strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 0
        elif periods[t] == 2 or periods[t] == 3:
            out[t] = 1
        else:
            if actions[t - 1] == 0 and actions[t - 2] == 0 and actions[t - 3] == 0:
                out[t] = 0
            else:
                out[t] = 1

    out[np.isnan(actions)] = np.nan
    return out


def s18_dgrim2(actions, periods):
    """Suspicious-Lenient-Grim-2"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 0
        elif periods[t] == 2:
            out[t] = 1
        else:
            if min(out[t - 1], actions[t - 1]) == 0 and min(out[t - 2], actions[t - 2]) == 0:
                out[t] = 0
            else:
                out[t] = 1

    out[np.isnan(actions)] = np.nan
    return out


def s19_dgrim3(actions, periods):
    """Suspicious-Lenient-Grim-3"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 0
        elif periods[t] == 2 or periods[t] == 3:
            out[t] = 1
        else:
            if min(out[t - 1], actions[t - 1]) == 0 and min(out[t - 2], actions[t - 2]) == 0 and min(out[t - 3],
                                                                                                     actions[
                                                                                                         t - 3]) == 0:
                out[t] = 0
            else:
                out[t] = 1

    out[np.isnan(actions)] = np.nan
    return out


def s20_dcalt(actions, periods):
    """DC Alternator strategy"""
    n = len(actions)
    out = np.ones(n)
    for t in range(n):
        if periods[t] == 1:
            out[t] = 0
        else:
            out[t] = 1 - out[t - 1]
    out[np.isnan(actions)] = np.nan
    return out


if __name__ == "__main__":
    strategy_list = []
    strategy_names = []
    for i in dir(sys.modules[__name__]):
        s = getattr(sys.modules[__name__], i)
        if callable(s):
            strategy_list.append(s)
            strategy_names.append(s.__name__)
    print("\n")
    print("=" * 100)
    print("This file contains", len(strategy_list), "strategy definitions.")
    print("Each strategy takes two lists/arrays as arguments. The first argument is the list of actions. Action are " +
      "either 1 (=Cooperate) or 0 (=Defect). The second argument is the list of periods. Period 1 signifies" +
      "start of a new supergame.")
    print("The strategies are:", strategy_names)
    print("-" * 50)
    print("Example call: ", strategy_names[0] + "(actions=[1,1,0,0,1],periods=[1,2,3,1,2]) --> ",
          strategy_list[0](actions=[1, 1, 0, 0, 1], periods=[1, 2, 3, 1, 2]))
    print("=" * 100)
