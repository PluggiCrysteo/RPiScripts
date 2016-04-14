#! /usr/bin/python
import os,os.path
from subprocess import Popen

CAN_SOCKET = "/tmp/can_unix_socket"
USER_TASKS = "/tmp/fifo_user_receive"
TASK_HARDWARE = "/tmp/fifo_task_hardware"

HOMEDIR="/home/crysteo"

if os.path.exists(CAN_SOCKET):
    os.remove(CAN_SOCKET)
if os.path.exists(TASK_HARDWARE):
    os.remove(TASK_HARDWARE)
if os.path.exists(USER_TASKS):
    os.remove(USER_TASKS)

os.mkfifo(TASK_HARDWARE,0666)
os.mkfifo(USER_TASKS,0666)

print "Executing CAN handler (C)"
Popen([HOMEDIR + "/C/CAN_HANDLER/CAN_HANDLER",CAN_SOCKET,USER_TASKS])
print "Executing task_manager (python)"
Popen("python " + HOMEDIR + "/python/TaskManager/task_manager/task_manager.py " + CAN_SOCKET + " " + USER_TASKS, shell=True)
#placeholder = open(CAN_SEND, 'w')
