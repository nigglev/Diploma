from Libs import *
from IntegralSolver import *

C = 1 / math.sqrt(2)
#C = 1

def IsInsideParabolaG2(x, y):
    p = pow(y, 2) - (2 * C) * x
    return p

def IsInsideParabolaG1(x, y):
    p = pow(y, 2) + (2 * C) * x
    return p

def GetPositionRelativeToCurve(x, y):
    pos = ["Above", "Below", "On Curve"]
    if x == 0 and y == 0:
        return pos[2]
    if x >= 0 and y >= 0:
        return pos[0]
    if x <= 0 and y <= 0:
        return pos[1]
    p1 = IsInsideParabolaG1(x,y)
    p2 = IsInsideParabolaG2(x,y)
    
    if p2 < 0:
        return pos[0]
    if p1 < 0:
        return pos[1]
    if p1 == 0 or p2 == 0:
        return pos[2]
    if p1 > 0 or p2 > 0:
        if y < 0:
            return pos[1]
        if y > 0:
            return pos[0]
    
    return "None"


def XYAbove(x_0, y_0, tau, T):
    i = 1
    x = list()
    y = list()
    step = 0.0001
    t1 = np.arange(0, tau + step, step)
    t2 = np.arange(tau + step, T + step, step)
    t = np.concatenate([t1,t2])
    x.append(x_0)
    y.append(y_0)
    while t[i] <= tau:
        t_i = t[i]
        value_x = -C * t_i**2 / 2 + y_0 * t_i + x_0
        value_y = -C*t_i + y_0
        x.append(value_x)
        y.append(value_y)
        i = i + 1
    for j in range(i, t.size):
        t_j = t[j]
        value_x = (C / 2) * (t_j**2 - tau**2) + C*T*(tau - t_j) + (y_0 - C*tau)**2 / (2*C)
        value_y = C * t_j - y_0 - 2 * math.sqrt(C*x_0 + ((y_0**2) / 2))
        x.append(value_x)
        y.append(value_y)
    return x, y, t

def XYBelow(x_0, y_0, tau, T):
    i = 1
    x = list()
    y = list()
    step = 0.0001
    t1 = np.arange(0, tau + step, step)
    t2 = np.arange(tau + step, T + step, step)
    t = np.concatenate([t1,t2])
    x.append(x_0)
    y.append(y_0)
    while t[i] <= tau:
        t_i = t[i]
        value_x = C * t_i**2 / 2 + y_0 * t_i + x_0
        value_y = C*t_i + y_0
        x.append(value_x)
        y.append(value_y)
        i = i + 1
    for j in range(i, t.size):
        t_j = t[j]
        e = 2*math.sqrt(y_0**2 / 2 - C*x_0) - y_0
        value_x = -C*t_j**2 / 2 + e*t_j + y_0*tau + x_0 + C*tau**2 - e*tau
        value_y = -C * t_j + e
        x.append(value_x)
        y.append(value_y)
    return x, y, t

def CalculateTime(x_0, y_0, pos):
    T = 0
    tau = 0
    if pos == "Above":
        tau = y_0 / C + math.sqrt(y_0**2 / 2 + C * x_0) / C
        T = (1 / C) * (y_0 + 2 * math.sqrt(y_0**2 / 2 + C * x_0))
    if pos == "Below":
        tau = -y_0 / C + math.sqrt(y_0**2 / 2 - C * x_0) / C
        T = (1 / C) * (-y_0 + 2 * math.sqrt(y_0**2 / 2 - C * x_0))
    return tau, T


def CalculateTrajectory(x_0, y_0, tau, T, pos):
    if pos == "Above":
        x, y, t = XYAbove(x_0, y_0, tau, T)
    if pos == "Below":
        x, y, t = XYBelow(x_0, y_0, tau, T)
    return x, y, t
    
def EqualizeListSizes(list1, list2):
    l1_length = len(list1)
    l2_length = len(list2)
    gap = abs(l1_length - l2_length)

    if l1_length == l2_length:
        return list1, list2
    if l1_length > l2_length:
        for i in range(gap):
            list2.append(0)
    if l2_length > l1_length:
        for i in range(gap):
            list1.append(0)
    return list1, list2

def SolveIntegralTrapzMethod(x, t):
    x_squared = [i ** 2 for i in x]
    N = len(t) - 1
    h = t[1] - t[0]

    val1 = x_squared[0] + x_squared[-1]
    val2 = 0

    for t_i in range(1, N):
        val2 = val2 + x_squared[t_i]

    val2 = val2 * 2

    result = (h / 2) * (val1 + val2)

    return result

def IntergralFromZeroToTau(tau, T, pos, x_0, y_0):

    def x_above_func(t):
        return (-C * t**2 / 2 + y_0 * t + x_0)**2
    def x_below_func(t):
        return (C * t**2 / 2 + y_0 * t + x_0)**2

    if pos == "Above":
        result, err = scipy.integrate.quad(lambda t: x_above_func(t), 0, tau)
    if pos == "Below":
        result, err = scipy.integrate.quad(lambda t: x_below_func(t), 0, tau)

    return result

def IntergralFromTauToT(tau, T, pos, x_0, y_0):

    def x_above_func(t):
        val = (C / 2) * (t**2 - tau**2) + C*T*(tau - t) + (y_0 - C*tau)**2 / (2*C)
        return val**2
    def x_below_func(t):
        e = 2*math.sqrt(y_0**2 / 2 - C*x_0) - y_0
        val = -C*t**2 / 2 + e*t + y_0*tau + x_0 + C*tau**2 - e*tau
        return val**2

    if pos == "Above":
        result, err = scipy.integrate.quad(lambda t: x_above_func(t), tau, T)
    if pos == "Below":
        result, err = scipy.integrate.quad(lambda t: x_below_func(t), tau, T)

    return result


def SolveIntergralOCPScipyQuadMethod(tau, T, pos, x_0, y_0):

    I1 = IntergralFromZeroToTau(tau, T, pos, x_0, y_0)
    I2 = IntergralFromTauToT(tau, T, pos, x_0, y_0)

    return (I1 + I2)

def PlotData(t1, t2, x1, y1, x2, y2):

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(t1, x1)
    axs[0, 0].set_title('X1')
    axs[0, 1].plot(t1, y1, 'tab:orange')
    axs[0, 1].set_title('Y1')
    axs[1, 0].plot(t2, x2, 'tab:green')
    axs[1, 0].set_title('X2')
    axs[1, 1].plot(t2, y2, 'tab:red')
    axs[1, 1].set_title('Y2')

    for ax in axs.flat:
        ax.set(xlabel='Time', ylabel='Value')

    for ax in axs.flat:
        ax.label_outer()

    plt.grid(True)
    plt.show()

def SolveOCP(x_0_1, y_0_1, x_0_2, y_0_2):

    pos1 = GetPositionRelativeToCurve(x_0_1, y_0_1)
    pos2 = GetPositionRelativeToCurve(x_0_2, y_0_2)

    tau1, T1 = CalculateTime(x_0_1, y_0_1, pos1)
    tau2, T2 = CalculateTime(x_0_2, y_0_2, pos2)

    x1, y1, t1 = CalculateTrajectory(x_0_1, y_0_1, tau1, T1, pos1)
    x2, y2, t2 = CalculateTrajectory(x_0_2, y_0_2, tau2, T2, pos2)

    #PlotData(t1, t2, x1, y1, x2, y2)

    x3 = [1, 2, 3, 4, 5]

    I1 = SolveIntegralTrapzMethod1D(x1, T1)
    I2 = SolveIntegralTrapzMethod1D(x2, T2)
    I3 = SolveIntegralTrapzMethod1D(x3, 1)

    I = I1 + I2

    print("Times for Optimal Control Problem:")
    print("T1 = {} \nT2 = {}".format(T1, T2))
    print("Integral Result for Optimal Control Problem(Quad) = {}".format(I))

    return T1, T2, I
    