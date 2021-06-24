from Libs import *
from OptimalControlProblem import SolveOCP
from FullerModel import *
from IntegralSolver import *
from BocopManager import *

def WriteToCSV(T, x1_0, y1_0, x2_0, y2_0, I_F, T1_OCP, T2_OCP, I_F_OCP):
    f = open('text.txt', 'a')
    f.write("{},{},{},{},{},{},{},{},{}\n".format(T, x1_0, y1_0, x2_0, y2_0, I_F, T1_OCP, T2_OCP, I_F_OCP))
    f.close


def GetTimeArray(T, N):
    step = T / N

    return np.arange(0, T + step, step)

def main():

    # T = [1,2,3]
    # N = 100000
    # fig, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.set_xlabel(r'$x_{1}(0)$', fontsize=20)
    # ax1.set_ylabel(r'$y_{1}(0)$', fontsize=20)
    # ax2.set_xlabel(r'$x_{2}(0)$', fontsize=20)
    # ax2.set_ylabel(r'$y_{2}(0)$', fontsize=20)
    # ax1.grid(True)
    # ax2.grid(True)

    # for T_i in T:
    #     t = GetTimeArray(T_i,N)
    #     x1, y1, x2, y2 = CalculateTrajectoryFuller(t)

    #     angle_list = list()
    #     angle_list.append(0)
    #     number_of_angles = 1000
    #     for i in range(number_of_angles):
    #         angle_list.append((i+1) * math.pi / (number_of_angles / 2))

    #     x_1_0_rotated_list, y_1_0_rotated_list, x_2_0_rotated_list, y_2_0_rotated_list = RotateInitialPoints(x1[0], y1[0], x2[0], y2[0], angle_list)
    #     ax1.plot(x_1_0_rotated_list[0], y_1_0_rotated_list[0], 'bo', color = "red", markersize=6)
    #     ax2.plot(x_2_0_rotated_list[0], y_2_0_rotated_list[0], 'bo', color = "red", markersize=6)
    #     ax1.plot(x_1_0_rotated_list, y_1_0_rotated_list, label='T = {}'.format(T_i))
    #     ax2.plot(x_2_0_rotated_list, y_2_0_rotated_list, label='T = {}'.format(T_i))
    # ax1.legend()
    # ax2.legend()    
    # plt.show()

    while True:
        data = input("Enter T = ")
        if data == "":
            break
        T = float(data)
        N = 10000
        t = GetTimeArray(T,N)
        x1, y1, x2, y2 = CalculateTrajectoryFuller(t)
        
        angle_list = list()
        angle_list.append(0)
        number_of_angles = 1000
        for i in range(number_of_angles):
            angle_list.append((i+1) * math.pi / (number_of_angles / 2))

        x_1_0_rotated_list, y_1_0_rotated_list, x_2_0_rotated_list, y_2_0_rotated_list = RotateInitialPoints(x1[0], y1[0], x2[0], y2[0], angle_list)
        x_1_0_rotated = x_1_0_rotated_list[1]
        y_1_0_rotated = y_1_0_rotated_list[1]
        x_2_0_rotated = x_2_0_rotated_list[1]
        y_2_0_rotated = y_2_0_rotated_list[1]

        dot_value = x_1_0_rotated * y_1_0_rotated + x_2_0_rotated * y_2_0_rotated
        length_value = math.sqrt(x_1_0_rotated * x_1_0_rotated + x_2_0_rotated * x_2_0_rotated) * math.sqrt(y_1_0_rotated * y_1_0_rotated + y_2_0_rotated * y_2_0_rotated)
        angle_value = math.acos(dot_value / length_value)
        I_Fuller = SolveIntergralFullerScipyQuadMethod(T)
        I_F_2 = SolveIntegralTrapzMethod2D(x1, x2, T)

        print("Angle value = {}. Correct Value = {}". format(angle_value, 2 * math.atan(math.sqrt(5))))
        print("Left Value = {}. Right = {}". format(y1[0] * y1[0] + y2[0] * y2[0], math.sqrt(6) / 2 * math.sqrt(x1[0] * x1[0] + x2[0] * x2[0])))
    
   
if __name__ == "__main__":
    main()
