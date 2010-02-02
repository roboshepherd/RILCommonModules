from math import pi
# Enabling/Disabling Some Expt Settings/Params of TaskSelector
USE_NORMALIZED_POSE = True
POSE_FACTOR = 5
PROB_SCALE = 100
TASK_SELECTION_STEPS = 100
RANDOM_WALK_TASK_ID = 0
TASK_PERIOD = 30 # timeout period
TASK_INFO_UPDATE_FREQ = TASK_PERIOD / 3
TASK_INFO_EMIT_FREQ = TASK_PERIOD / 10

# DBus  Message Protocol
ROBOT_POSE_X = 'x'
ROBOT_POSE_Y = 'y'
ROBOT_POSE_THETA = 'theta'
ROBOT_POSE_TS = 'ts'
# TaskInfo list 
TASK_INFO_TIME  = 0
TASK_INFO_X  = 1
TASK_INFO_Y  = 2
TASK_INFO_THETA = 3
TASK_INFO_URGENCY = 4

#D-Bus Config
DBUS_IFACE_TRACKER = "uk.ac.newport.ril.SwisTrack"
DBUS_IFACE_EPUCK = "uk.ac.newport.ril.Epuck"
DBUS_PATH_BASE = "/robot"
DBUS_ROBOT_PATH_BASE = "/robot"
DBUS_IFACE_TASK_SERVER = "uk.ac.newport.ril.TaskServer"
DBUS_PATH_TASK_SERVER = "/taskserver"
SIG_TASK_STATUS = "TaskStatus"
SIG_ROBOT_POSE = "PoseSignal"
SIG_TASK_INFO = "TaskInfo"
SIG_LOCAL_TASK_INFO = "LocalTaskInfo"
SIG_TASK_NEIGHBOR = "TaskNeighbors"
SIG_ROBOT_PEERS = "RobotPeers"
DBUS_TASK_PATH_BASE = "/task"
ROBOTS_PATH_CFG_FILE = "/home/newport-ril/centralized-expt/\
DistributedTaskServer/robots_dbus_path.conf"

DBUS_PATH_EPUCK_LOCALITY = "/EpuckLocality"
TASK_INFO_TYPE = "TaskInfoType"
LOCAL_INFO_PRIMARY = 1  # robot got this taskinfo from task server
LOCAL_INFO_SECONDARY = 2 # learned about this task via other peers



# DataManager SelectedTask  Dict keys
SELECTED_TASK_ID = 'id' # val: TaskID
SELECTED_TASK_STATUS = 'status' # val: TaskStatus
SELECTED_TASK_INFO  = 'taskinfo' # val: [x, y, theta]
SELECTED_TASK_RW = 'rw' # Randomwalk
ROBOT_PEERS = 'peers'
TIME_STAMP = 'ts'


# Task Status
TASK_SELECTED = "TaskSelected"
TASK_PENDING = "TaskPending"
TASK_DONE = "TaskDone"
TASK_TIMED_OUT = "TaskTimedOut"


#RIL and AFM params
MAX_SHOPTASK = 3   
INIT_TASK_URGENCY = 0.4
DELTA_TASK_URGENCY = 0.01 
DELTA_TASK_URGENCY_INC = 0.005
DELTA_TASK_URGENCY_DEC = 0.0025
#INIT_MATERIAL_COUNT = 10
XY = 2  # for task coordinates
DELTA_DISTANCE = 0.000001
 
#robot device's instrinsics
INIT_SENSITIZATION = 0.1
INIT_LEARN_RATE = 0.02 
INIT_FORGET_RATE = 0.01 # should be INIT_LEARN_RATE/ (MAX_SHOPTASK -1)
 
# for pose nomalization
MAX_X = 3600
MAX_Y = 3248
MAX_THETA = (2* pi)
 
# for navigation
TASK_RADIUS = 300 #pixel
TASK_CONE_ANGLE = 0.26 #15deg
MAX_NAV_STEP = 1 #how long navigation continues
# angles
REVERSE_ANGLE1 = 2.90 
REVERSE_ANGLE2  = 1.52
DELTA_ANGLE1  = 0.26
DELTA_ANGLE0 =  0.26
 
ANGLE30  = pi/6
ANGLE90  = pi/2
ANGLE180 = pi
ANGLE270  = 3.0 * pi/2
ANGLE360  =  2.0 * pi
ANGLE0 = 0.0

# Robot Device States
#/* Connectivity states */
NOTSET = -100
#/* state as (- id) e.g. UNAVAILABLE = - id
#UNAVAILABLE state of Robot 5 = - 5*/
UNAVAILABLE = -50
#/* state as (+ id) e.g. AVAILABLE = state + id
#AVAILABLE state of Robot 5 = 5*/
AVAILABLE = 0
#/* task states, set state as (this value+id) e.g. RW = 50 + id*/
RW = 50
TASK = 99 #/* seldom used */
TASK1 = 100
TASK2 = 200
TASK3 = 300
TASK4 = 400
TASK5 = 500
TASK6 = 600
TASK7 = 700
TASK8 = 800
TASK9 = 900
TASK10 = 1000
