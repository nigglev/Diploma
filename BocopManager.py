from Libs import *
from IntegralSolver import *

def IsNumber(val):
    try:
        float(val)
        return True
    except ValueError:
        return False



def ReadFile(path):
    file_handler = open(path)
    print(file_handler.read())


def GetValues1DProblem(problem_name):
    if problem_name == "Fuller1D":
        path = "C://Bocop-2.2.1/examples/fuller/problem.sol"
    if problem_name == "OCP1D":
        path = "C://Bocop-2.2.1/Projects/OCP/problem.sol"

    values = list()

    with open(path) as infile:
        copy = False
        for line in infile:
            if line.strip() == "# State 0":
                copy = True
                continue
            elif line.strip() == "# State 1":
                copy = False
                continue
            elif copy:                
                if(IsNumber(line)):
                    values.append(float(line))
    res = SolveIntegralTrapzMethod1D(values, 3)
    print(res)

def GetXValues2DProblem(problem_name):
    if problem_name == "Fuller2D":
        path = "C://Bocop-2.2.1/Projects/Fuller2D/problem.sol"
    if problem_name == "OCP2D":
        path = "C://Bocop-2.2.1/Projects/OCP2D/problem.sol"

    values_state_0 = list()
    values_state_1 = list()
    T = 0

    with open(path) as infile:
        copy_state_1 = False
        copy_state_2 = False
        copy_state_time = False
        for line in infile:
            if line.strip() == "# Objective value :":
                copy_state_time = True
                continue
            if line.strip() == "# L2-norm of the constraints :":
                copy_state_time = False
                continue
            if line.strip() == "# State 0":
                copy_state_1 = True
                continue
            elif line.strip() == "# State 1":
                copy_state_1 = False
                continue
            if line.strip() == "# State 2":
                copy_state_2 = True
                continue
            elif line.strip() == "# State 3":
                copy_state_2 = False
                continue
            elif copy_state_1:                
                if(IsNumber(line)):
                    values_state_0.append(float(line))
            elif copy_state_2:                
                if(IsNumber(line)):
                    values_state_1.append(float(line))
            elif copy_state_time:                
                if(IsNumber(line)):
                    T = float(line)
    return T, values_state_0, values_state_1


def GetYValues2DProblem(problem_name):
    if problem_name == "Fuller2D":
        path = "C://Bocop-2.2.1/Projects/Fuller2D/problem.sol"
    if problem_name == "OCP2D":
        path = "C://Bocop-2.2.1/Projects/OCP2D/problem.sol"

    values_state_0 = list()
    values_state_1 = list()

    with open(path) as infile:
        copy_state_1 = False
        copy_state_2 = False
        copy_state_time = False
        for line in infile:
            if line.strip() == "# Objective value :":
                copy_state_time = True
                continue
            if line.strip() == "# L2-norm of the constraints :":
                copy_state_time = False
                continue
            if line.strip() == "# State 1":
                copy_state_1 = True
                continue
            elif line.strip() == "# State 2":
                copy_state_1 = False
                continue
            if line.strip() == "# State 3":
                copy_state_2 = True
                continue
            elif line.strip() == "# State 4":
                copy_state_2 = False
                continue
            elif copy_state_1:                
                if(IsNumber(line)):
                    values_state_0.append(float(line))
            elif copy_state_2:                
                if(IsNumber(line)):
                    values_state_1.append(float(line))
            elif copy_state_time:                
                if(IsNumber(line)):
                    T = float(line)
    return values_state_0, values_state_1


def GetControl2DProblem(problem_name):
    if problem_name == "Fuller2D":
        path = "C://Bocop-2.2.1/Projects/Fuller2D/problem.sol"
    if problem_name == "OCP2D":
        path = "C://Bocop-2.2.1/Projects/OCP2D/problem.sol"

    values_control_0 = list()
    values_control_1 = list()
    T = 0

    with open(path) as infile:
        copy_control_1 = False
        copy_control_2 = False
        copy_state_time = False
        for line in infile:
            if line.strip() == "# Objective value :":
                copy_state_time = True
                continue
            if line.strip() == "# L2-norm of the constraints :":
                copy_state_time = False
                continue
            if line.strip() == "# Control 0":
                copy_control_1 = True
                continue
            elif line.strip() == "":
                copy_control_1 = False
                continue
            if line.strip() == "# Control 1":
                copy_control_2 = True
                continue
            elif line.strip() == "":
                copy_control_2 = False
                continue
            elif copy_control_1:                
                if(IsNumber(line)):
                    values_control_0.append(float(line))
            elif copy_control_2:                
                if(IsNumber(line)):
                    values_control_1.append(float(line))
            elif copy_state_time:                
                if(IsNumber(line)):
                    T = float(line)
    return values_control_0, values_control_1
    
def PlotDataTwoStacked(x1, y1, x2, y2):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_xlabel(r'$x_{1}$')
    ax2.set_xlabel(r'$x_{2}$')
    ax1.set_ylabel(r'$y_{1}$')
    ax2.set_ylabel(r'$y_{2}$')
    ax1.plot(x1, y1)
    ax2.plot(x2, y2)
    ax1.grid(True)
    ax2.grid(True)
    plt.show()
    

def SolveSystem(x, y, u):
    h = 0.001
    x_new = list()
    y_new = list()
    length = range(len(x))

    for i in length:
        if i == 0:
           x_new.append(x[0]) 
           y_new.append(y[0]) 
           continue 
        val_x = x_new[i - 1] + h * y_new[i - 1]
        val_y = y_new[i - 1] + h * (u[i - 1] + x_new[i-1])
        x_new.append(val_x)
        y_new.append(val_y)
    
    return x_new, y_new

def main():
    problems = ["Fuller1D", "Fuller2D", "OCP1D", "OCP2D"]
    
    T, x1, x2 = GetXValues2DProblem(problems[3])
    y1, y2 = GetYValues2DProblem(problems[3])
    u1, u2 = GetControl2DProblem(problems[3])

    x1_new, y1_new = SolveSystem(x1, y1, u1)
    x2_new, y2_new = SolveSystem(x2, y2, u2)

    dist1 = math.sqrt(x1_new[-1]**2 + y1_new[-1]**2)
    dist2 = math.sqrt(x2_new[-1]**2 + y2_new[-1]**2)

    print("Last point: x1(T) = {}, y1(T) = {}, x2(T) = {}, y2(T) = {}".format(x1_new[-1], y1_new[-1], x2_new[-1], y2_new[-1]))
    print("Distance for first set = {}; Distance for second set = {}".format(dist1, dist2))
    
    PlotDataTwoStacked(x1_new, y1_new, x2_new, y2_new)
    
        
   
if __name__ == "__main__":
    main()
    