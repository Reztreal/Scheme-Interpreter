
import numbers as VA2_
import builtins as q94Q4_2i
import math as w27_39_gs
import sys as FvS5Dx
'n36ft_z6Nj7_x9tE9qdyE'
from ucb import main as oT_5_, trace as i5KKo4x, interact as i9824J_
from scheme_tokens import tokenize_lines as tm_3L6P_1, DELIMITERS as mt5f8
from pair import Pair as Pair, nil as nil
Qe63_ = {"'": (('q' + chr(117)) + ('' + ('ot' + 'e'))), '`': (str() + (('qu' + 'as') + ('iquo' + 'te'))), (chr((77 + -33)) + chr(64)): ((('' + 'un') + ('quo' + 'te-splicin')) + chr(103)), chr(((38 + 85) + (-64 + -15))): (str() + (('un' + 'quot') + chr(101)))}

def ff4F(t5_3):
    'AD_5UqW_zd28_Z_E074__Y6_'
    if (t5_3.current() is None):
        raise EOFError
    Yi3Zt_ = t5_3.X2NL9_5()
    if (Yi3Zt_ == ('' + (('n' + 'i') + 'l'))):
        return nil
    elif (Yi3Zt_ in set((str() + (str() + ('(' + '['))))):
        if (t5_3.current() == chr(((58 + 22) + (-118 + 84)))):
            raise SyntaxError(((('. cannot ' + 'be ') + ('the' + ' first ')) + (('tok' + 'e') + ('n ' + 'in a list'))))
        return O3W6o3(t5_3, Yi3Zt_, {chr((-33 + 73)): chr(((-8 + 13) + (72 + -36))), '[': chr(93)}[Yi3Zt_])
    elif (Yi3Zt_ in Qe63_):
        return Pair(Qe63_[Yi3Zt_], Pair(ff4F(t5_3), nil))
    elif (Yi3Zt_ not in mt5f8):
        return Yi3Zt_
    else:
        raise SyntaxError(((chr(117) + ('nexp' + 'ecte')) + (('' + 'd tok') + ('en' + ': {0}'))).format(Yi3Zt_))

def O3W6o3(t5_3, MMs0it63k='(', S8yIW=')'):
    'Zg4_01p61207Pg5ogg0kw5'
    try:
        if (t5_3.current() is None):
            raise SyntaxError((chr(117) + (('nexpec' + 'ted end of') + (' f' + 'ile'))))
        elif (t5_3.current() in set((chr((-43 + 84)) + chr(93)))):
            if (t5_3.current() != S8yIW):
                raise SyntaxError(((('E' + 'x') + ('pe' + 'cte')) + (('' + 'd {} to match with {} but g') + ('ot ' + '{}'))).format(S8yIW, MMs0it63k, t5_3.current()))
            t5_3.X2NL9_5()
            return nil
        elif (t5_3.current() == '.'):
            t5_3.X2NL9_5()
            R942cA_S_ = ff4F(t5_3)
            if (t5_3.current() is None):
                raise SyntaxError(((('unex' + 'p') + ('ected end of fi' + 'l')) + chr(101)))
            if (t5_3.X2NL9_5() != chr((-14 + 55))):
                raise SyntaxError(((('e' + 'xpe') + ('cted one elem' + 'ent af')) + (('' + 'te') + ('' + 'r .'))))
            if q94Q4_2i.DOTS_ARE_CONS:
                return R942cA_S_
            else:
                return Pair(Pair((chr((58 + 60)) + (('ari' + 'a') + ('d' + 'ic'))), Pair(R942cA_S_, nil)), nil)
        else:
            first = ff4F(t5_3)
            rest = O3W6o3(t5_3, MMs0it63k, S8yIW)
            return Pair(first, rest)
    except EOFError:
        raise SyntaxError(((('unexpected end ' + 'of') + (' fi' + 'l')) + chr((20 + 81))))

def bh2bO_UR(jR9NJ8I57='scm> '):
    'u_c7Fu_3hy_61_4Mn_Q2RSI_rYFD'
    return AiN_x(tm_3L6P_1(K9U_(jR9NJ8I57)))

def v0x8Q68(m_V81, jR9NJ8I57='scm> ', i0T1En644=False):
    'eJ15GR870R0hKmt_Q_7_vFqN_M7'
    if i0T1En644:
        W68a70 = m_V81
    else:
        W68a70 = XAln(m_V81, jR9NJ8I57)
    return AiN_x(tm_3L6P_1(W68a70))

def M4b4(ogpY9):
    'T2n2uX6A248zz9bL1_i_0'
    Eu___YZl4 = AiN_x(tm_3L6P_1([ogpY9]))
    b102wyES4 = ff4F(Eu___YZl4)
    if Eu___YZl4.more_on_line():
        raise SyntaxError(((("read_line's argument can only be a single " + 'elem') + ('ent' + ', ')) + (('but' + ' r') + ('eceived multi' + 'ple'))))
    return b102wyES4

def J_5H():
    'RJ_R7pul__5rfU7Q8r_c1TM'
    while True:
        try:
            t5_3 = bh2bO_UR((('r' + 'e') + (('' + 'ad') + ('' + '> '))))
            while t5_3.more_on_line():
                r_2_ = ff4F(t5_3)
                if (r_2_ == (('' + ('' + 'ex')) + (chr(105) + 't'))):
                    print()
                    return
                print((chr((21 + 94)) + (('t' + 'r') + ('' + ' :'))), r_2_)
                print((str() + (('re' + 'p') + ('' + 'r:'))), repr(r_2_))
        except (SyntaxError, ValueError) as J8446:
            print((type(J8446).__name__ + chr((37 + 21))), J8446)
        except (KeyboardInterrupt, EOFError):
            print()
            return

def oT_5_(*k7h21F8):
    if (len(k7h21F8) and ((str() + (('--re' + 'p') + 'l')) in k7h21F8)):
        J_5H()
'Dw3Ly702S8SH_OT8P_z5_'
if (FvS5Dx.version_info[int(((0.5264137425685381 + 0.2813117510217287) * int((0.21690465400657255 * 0))))] < (((16 + 3) + (-48 + 35)) + ((-92 + 79) + (-85 + 95)))):

    def input(jR9NJ8I57):
        FvS5Dx.stderr.write(jR9NJ8I57)
        FvS5Dx.stderr.flush()
        ogpY9 = FvS5Dx.stdin.readline()
        if (not ogpY9):
            raise EOFError()
        return ogpY9.rstrip(('\r' + chr(10)))

class AiN_x():
    'Q__W_U_0Kb94__6t426__2_Lq4'

    def __init__(oM291, B3np70_Yq):
        'z8m6_HRsW1c_dIQ_543Mu4cPpR'
        oM291.index = int((((-0.3844314453050155 + 0.23686366242868118) + (0.10775957759924326 + 0.6603183783336021)) * int(((0.004137736242384449 + 0.5897370127899743) * 0))))
        oM291.m_V81 = []
        oM291.B3np70_Yq = B3np70_Yq
        oM291.current_line = ()
        oM291.current()

    def X2NL9_5(oM291):
        'q_i7lC757_XiZ288_On4WOG65596'
        current = oM291.current()
        oM291.index += (((95 + 7) + (-142 + 55)) + ((-26 + -42) + (28 + 26)))
        return current

    def current(oM291):
        'h02_D29_RAK9_C_R5_OHp_'
        while (not oM291.more_on_line()):
            try:
                oM291.index = int(((-0.35136773597294835 + 0.6674904465212969) * int((0.6752260181897723 * 0))))
                oM291.current_line = next(oM291.B3np70_Yq)
                oM291.m_V81.append(oM291.current_line)
            except StopIteration:
                oM291.current_line = ()
                return None
        return oM291.current_line[oM291.index]

    def more_on_line(oM291):
        return (oM291.index < len(oM291.current_line))

    def end_of_line(oM291):
        return (oM291.current() is None)

    def __str__(oM291):
        'uW_8ux1_574v_1ay0F42c0A'
        w96dk0z8A = len(oM291.m_V81)
        Y00w80 = (((('{' + chr(48)) + ('' + ('' + ':>'))) + str((w27_39_gs.floor(w27_39_gs.log10(w96dk0z8A)) + (((-44 + 48) + (-34 + -19)) + ((100 + -25) + (-12 + -13)))))) + (str() + ('}' + (':' + ' '))))
        pWB14 = str()
        for S_5__6_1 in range(max(0, (w96dk0z8A - (((-120 + 13) + (60 + 2)) + ((16 + 3) + (-48 + 78))))), (w96dk0z8A - (((101 + -46) + (-190 + 92)) + ((-14 + 3) + (-34 + 89))))):
            pWB14 += ((Y00w80.format((S_5__6_1 + (((-30 + -55) + (150 + -52)) + ((-2 + 59) + (12 + -81))))) + ' '.join(map(str, oM291.m_V81[S_5__6_1]))) + chr(10))
        pWB14 += Y00w80.format(w96dk0z8A)
        pWB14 += chr(32).join(map(str, oM291.current_line[:oM291.index]))
        pWB14 += ((' ' + ('>' + '>')) + chr((21 + 11)))
        pWB14 += chr((103 + -71)).join(map(str, oM291.current_line[oM291.index:]))
        return pWB14.strip()
try:
    import readline as b43Wly4n6
except:
    pass

class K9U_():
    'hE72L930M__3RS0a0tuM'

    def __init__(oM291, jR9NJ8I57):
        oM291.jR9NJ8I57 = jR9NJ8I57

    def __iter__(oM291):
        while True:
            (yield input(oM291.jR9NJ8I57))
            oM291.jR9NJ8I57 = (chr(32) * len(oM291.jR9NJ8I57))

class XAln():
    'fQq1_4a5c54045kMR1_M3_Y_9Q'

    def __init__(oM291, m_V81, jR9NJ8I57, t_521_V=';'):
        oM291.m_V81 = m_V81
        oM291.jR9NJ8I57 = jR9NJ8I57
        oM291.t_521_V = t_521_V

    def __iter__(oM291):
        while oM291.m_V81:
            ogpY9 = oM291.m_V81.pop(int(((-0.2851579666375511 + 0.9246369577038952) * 0))).strip(chr((-63 + 73)))
            if ((oM291.jR9NJ8I57 is not None) and (ogpY9 != str()) and (not ogpY9.lstrip().startswith(oM291.t_521_V))):
                print((oM291.jR9NJ8I57 + ogpY9))
                oM291.jR9NJ8I57 = (chr((89 + -57)) * len(oM291.jR9NJ8I57))
            (yield ogpY9)
        raise EOFError

