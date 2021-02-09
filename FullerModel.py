from Libs import *
from OptimalControlProblem import SolveOCP

A0 = 1/126
alpha = math.sqrt(5)

def SolveIntergralFullerScipyQuadMethod(T):
    def func(t):
        return ((T - t)**4) * 49 * 6 * A0 ** 2
    result, err = scipy.integrate.quad(lambda t: func(t), 0, T)
    print("Integral Result for Fuller Problem(Quad) = {}".format(result))


def SolveIntegralTrapzMethod(x1, x2, t):

    T = t[-1]

    x1_squared = [i ** 2 for i in x1]
    x2_squared = [i ** 2 for i in x2]
    zipped = zip(x1_squared, x2_squared)
    x_sum = [val1 + val2 for (val1, val2) in zipped]

    N = len(t) - 1
    h = t[1] - t[0]

    val1 = x_sum[0] + x_sum[-1]
    val2 = 0

    for t_i in range(1, N):
        val2 = val2 + x_sum[t_i]

    val2 = val2 * 2

    result = (h / 2) * (val1 + val2)

    print("Integral Result for Fuller Problem(Trapz) = {}".format(result))

def GetTimeArray(T, N):
    step = T / N

    return np.arange(0, T + step, step)

def CalculateTrajectoryFuller(t):

    T = t[-1]
    ln = math.log(T)

    phi_x = math.atan(alpha)
    phi_y = math.atan(-alpha)

    x1 = list()
    y1 = list()

    x2 = list()
    y2 = list()
    
    for i in t:
        x1_i = A0 * 7 * math.sqrt(6) * (T - i)**2 * math.cos(alpha * ln + phi_x)
        y1_i = A0 * 21 * math.sqrt(6) * (T - i) * math.cos(alpha * ln + phi_y)

        x2_i = A0 * 7 * math.sqrt(6) * (T - i)**2 * math.sin(alpha * ln + phi_x)
        y2_i = A0 * 21 * math.sqrt(6) * (T - i) * math.sin(alpha * ln + phi_y)
        
        x1.append(x1_i)
        y1.append(y1_i)
        x2.append(x2_i)
        y2.append(y2_i)

    print("x1(0) = {}; y1(0) = {}".format(x1[0], y1[0]))
    print("x2(0) = {}; y2(0) = {}".format(x2[0], y2[0]))
    print("x1(T) = {}; y1(T) = {}".format(x1[-1], y1[-1]))
    print("x2(T) = {}; y2(T) = {}".format(x2[-1], y2[-1]))

    return x1,y1,x2,y2

def main():

    while True:
        data = input("Enter T = ")
        if data == "":
            break

        N = int(input("Enter N = "))

        T = float(data)
        t = GetTimeArray(T, N)

        x1, y1, x2, y2 = CalculateTrajectoryFuller(t)
        SolveIntergralFullerScipyQuadMethod(T)
        SolveIntegralTrapzMethod(x1, x2, t)
        
        
        SolveOCP(x1[0], y1[0], x2[0], y2[0])
        


   
if __name__ == "__main__":
    main()