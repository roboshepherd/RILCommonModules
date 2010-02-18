from math import pi
# Tuneable param:
#RIL and AFM params
MAX_SHOPTASK = 4   
INIT_TASK_URGENCY = 0.5
MIN_TASK_URGENCY = 0
MAX_TASK_URGENCY  = 1 
DELTA_TASK_URGENCY_INC = 0.005
DELTA_TASK_URGENCY_DEC = 0.0025
RW_MAX_URGENCY = 0.3
#INIT_MATERIAL_COUNT = 10
XY = 2  # for task coordinates
DELTA_DISTANCE = 0.000001
 
#robot device's instrinsics
INIT_SENSITIZATION = 0.1
INIT_LEARN_RATE = 0.03 
INIT_FORGET_RATE = 0.01 # should be INIT_LEARN_RATE/ (MAX_SHOPTASK -1)
 
# for pose nomalization
MAX_X = 2400
MAX_Y = 2144
MAX_THETA = (2* pi)
 
# for navigation
TASK_RADIUS = 300 #pixel
TASK_CONE_ANGLE = 0.26 #15deg
MAX_NAV_STEP = 1 #how long navigation continues



# Enabling/Disabling Some Expt Settings/Params of TaskSelector
USE_NORMALIZED_POSE = True
POSE_FACTOR = 5
PROB_SCALE = 100
TASK_SELECTION_STEPS = 1000 # inf
RANDOM_WALK_TASK_ID = 0
TASK_PERIOD = 10 # task timeout period
TASK_INFO_UPDATE_FREQ = 5 # updater delay
TASK_INFO_EMIT_FREQ = 2.5 # emitter delay

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
ROBOTS_PATH_CFG_FILE =\
"/home/newport-ril/centralized-expt/DistributedTaskServer/robots_dbus_path.conf"
DBUS_PATH_EPUCK_LOCALITY = "/EpuckLocal"
#TASK_INFO_TYPE = "TaskInfoType"
#LOCAL_INFO_PRIMARY = 1  # robot got this taskinfo from task server
#LOCAL_INFO_SECONDARY = 2 # learned about this task via other peers



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

# Angle alias
ANGLE30  = pi/6
ANGLE90  = pi/2
ANGLE180 = pi
ANGLE270  = 3.0 * pi/2
ANGLE360  =  2.0 * pi
ANGLE0 = 0.0

#--------- Robot Device States: obsolete now  ---#
#/* Connectivity states */
NOTSET = -100
#/* state as (- id) e.g. UNAVAILABLE = - id
#UNAVAILABLE state of Robot 5 = - 5*/
UNAVAILABLE = -50
#/* state as (+ id) e.g. AVAILABLE = state + id
#AVAILABLE state of Robot 5 = 5*/
AVAILABLE = 0

