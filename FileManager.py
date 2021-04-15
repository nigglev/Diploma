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

def GetValues2DProblem(problem_name):
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
    print(T)
    res = SolveIntegralTrapzMethod2D(values_state_0, values_state_1, T)
    
    

def main():
    problems = ["Fuller1D", "Fuller2D", "OCP1D", "OCP2D"]

    #GetValues1DProblem(problems[2])
    GetValues2DProblem(problems[3])
   
if __name__ == "__main__":
    main()
    