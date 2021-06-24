from Libs import *
from OptimalControlProblem import SolveOCP

A0 = 1/126
alpha = math.sqrt(5)

def PlotDataTwoStacked(t, val_1, val_2, title, color):
    plt.ion()
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(title)
    ax1.set_xlabel(r'$T$')
    ax2.set_xlabel(r'$T$')
    if title == r'$x_{1}(t), x_{2}(t)$':
        ax1.set_ylabel(r'$x_{1}(t)$')
        ax2.set_ylabel(r'$x_{2}(t)$')
    if title == r'$y_{1}(t), y_{2}(t)$':
        ax1.set_ylabel(r'$y_{1}(t)$')
        ax2.set_ylabel(r'$y_{2}(t)$')
    if title == r'$u_{1}(t), u_{2}(t)$':
        ax1.set_ylabel(r'$u_{1}(t)$')
        ax2.set_ylabel(r'$u_{2}(t)$')
    ax1.plot(t, val_1, color)
    ax2.plot(t, val_2, color)
    ax1.grid(True)
    ax2.grid(True)
    plt.show()

def PlotData(val_1, val_2, max_num_frames):
    x = val_1
    y = val_2
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'ro')
    k = 0

    def init():
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        return ln,

    def update(real_frame):
        Q = ax.quiver(0, 0, x[real_frame], y[real_frame], pivot='mid', color='r', units='inches')
        xdata.append(x[real_frame])
        ydata.append(y[real_frame])
        ln.set_data(xdata, ydata)
        return ln,

    ani = FuncAnimation(fig, update, frames=max_num_frames,
                        init_func=init, blit=True)
    plt.show()

    

def RotateInitialPoints(x_1_0, y_1_0, x_2_0, y_2_0, angle_list):

    x_1_0_rotated_list = list()
    x_2_0_rotated_list = list()

    y_1_0_rotated_list = list()
    y_2_0_rotated_list = list()


    for angle in angle_list:

        x_1_0_rotated = x_1_0 * math.cos(angle) - x_2_0 * math.sin(angle)
        x_2_0_rotated = x_1_0 * math.sin(angle) + x_2_0 * math.cos(angle)
        x_1_0_rotated_list.append(x_1_0_rotated)
        x_2_0_rotated_list.append(x_2_0_rotated)

        y_1_0_rotated = y_1_0 * math.cos(angle) - y_2_0 * math.sin(angle)
        y_2_0_rotated = y_1_0 * math.sin(angle) + y_2_0 * math.cos(angle)
        y_1_0_rotated_list.append(y_1_0_rotated)
        y_2_0_rotated_list.append(y_2_0_rotated)   
    

    return x_1_0_rotated_list, y_1_0_rotated_list, x_2_0_rotated_list, y_2_0_rotated_list



def CalculateTrajectoryFuller(t):

    T = t[-1]
    
    phi_x = math.atan(alpha)
    phi_y = math.atan(-alpha)

    x1 = list()
    y1 = list()

    x2 = list()
    y2 = list()

    u1 = list()
    u2 = list()
    
    for i in t:

        if(i == T):
            x1.append(x1_i)
            y1.append(y1_i)
            x2.append(x2_i)
            y2.append(y2_i)
            u1.append(u1_i)
            u2.append(u2_i)
            break

        ln = math.log(T - i)
        
        x1_i = A0 * 7 * math.sqrt(6) * (T - i)**2 * math.cos(alpha * ln + phi_x)
        y1_i = A0 * 21 * math.sqrt(6) * (T - i) * math.cos(alpha * ln + phi_y)

        x2_i = A0 * 7 * math.sqrt(6) * (T - i)**2 * math.sin(alpha * ln + phi_x)
        y2_i = A0 * 21 * math.sqrt(6) * (T - i) * math.sin(alpha * ln + phi_y)

        u1_i = math.cos(alpha * ln)
        u2_i = math.sin(alpha * ln)
        

        x1.append(x1_i)
        y1.append(y1_i)
        x2.append(x2_i)
        y2.append(y2_i)
        u1.append(u1_i)
        u2.append(u2_i)


    print("x1(0) = {}; y1(0) = {}".format(x1[0], y1[0]))
    print("x2(0) = {}; y2(0) = {}".format(x2[0], y2[0]))
    #print("x1(T) = {}; y1(T) = {}".format(x1[-1], y1[-1]))
    #print("x2(T) = {}; y2(T) = {}".format(x2[-1], y2[-1]))
    #print("u1(0) = {}; u2(0) = {}".format(u1[0], u2[0]))
    
    #PlotDataTwoStacked(t, x1, x2, r'$x_{1}(t), x_{2}(t)$', 'tab:orange')
    #PlotDataTwoStacked(t, y1, y2, r'$y_{1}(t), y_{2}(t)$', 'tab:green')
    #PlotDataTwoStacked(t, u1, u2, r'$u_{1}(t), u_{2}(t)$', 'tab:red')
    #PlotData(u1, u2, len(u1))

    return x1, y1, x2, y2