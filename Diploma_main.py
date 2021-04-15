from Libs import *
from OptimalControlProblem import SolveOCP
from FullerModel import CalculateTrajectoryFuller
from IntegralSolver import *
from FileManager import *

def WriteToCSV(T, x1_0, y1_0, x2_0, y2_0, I_F, T1_OCP, T2_OCP, I_F_OCP):
    f = open('text.txt', 'a')
    f.write("{},{},{},{},{},{},{},{},{}\n".format(T, x1_0, y1_0, x2_0, y2_0, I_F, T1_OCP, T2_OCP, I_F_OCP))
    f.close


def GetTimeArray(T, N):
    step = T / N

    return np.arange(0, T + step, step)

def main():

    # T_1 = np.arange(0.1, 1 + 0.1, 0.1)
    # T_2 = np.arange(2, 16, 1)
    # T = np.concatenate([T_1,T_2])
    # N = 100000

    # for T_i in T:
    #     t = GetTimeArray(T_i,N)
    #     x1, y1, x2, y2 = CalculateTrajectoryFuller(t)
    #     I_Fuller = SolveIntergralFullerScipyQuadMethod(T_i)
    #     T1_OCP, T2_OCP, I_OCP = SolveOCP(x1[0], y1[0], x2[0], y2[0])
    #     WriteToCSV(T_i, x1[0], y1[0], x2[0], y2[0], I_Fuller, T1_OCP, T2_OCP, I_OCP)


    while True:
        data = input("Enter T = ")
        if data == "":
            break
        T = float(data)
        N = 100000
        t = GetTimeArray(T,N)
        x1, y1, x2, y2 = CalculateTrajectoryFuller(t)
   
if __name__ == "__main__":
    main()
