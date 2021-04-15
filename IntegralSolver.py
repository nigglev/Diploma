from Libs import *

def SolveIntegralTrapzMethod1D(x, T):
    x_squared = [i ** 2 for i in x]
    N = len(x) - 1
    h = T / N

    val1 = x_squared[0] + x_squared[-1]
    val2 = 0

    for t_i in range(1, N):
        val2 = val2 + x_squared[t_i]

    val2 = val2 * 2

    result = (h / 2) * (val1 + val2)

    return result

def SolveIntergralFullerScipyQuadMethod(T):
    A0 = 1/126
    def func(t):
        return ((T - t)**4) * 49 * 6 * A0 ** 2
    result, err = scipy.integrate.quad(lambda t: func(t), 0, T)
    print("Integral Result for Fuller Problem(Quad) = {}".format(result))
    return result

def SolveIntegralTrapzMethod2D(x1, x2, T):

    N = len(x1) - 1
    h = T / N


    x1_squared = [i ** 2 for i in x1]
    x2_squared = [i ** 2 for i in x2]
    zipped = zip(x1_squared, x2_squared)
    x_sum = [val1 + val2 for (val1, val2) in zipped]

    val1 = x_sum[0] + x_sum[-1]
    val2 = 0

    for t_i in range(1, N):
        val2 = val2 + x_sum[t_i]

    val2 = val2 * 2

    result = (h / 2) * (val1 + val2)

    print(result)

    return result