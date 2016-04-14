#! /usr/bin/python
import os,os.path
from subprocess import Popen

CAN_SEND = "/tmp/fifo_can_send"
CAN_RECEIVE = "/tmp/fifo_can_receive"
USER_TASKS = "/tmp/fifo_user_receive"
TASK_HARDWARE = "/tmp/fifo_task_hardware"

HOMEDIR="/home/crysteo"

if os.path.exists(CAN_SEND):
    os.remove(CAN_SEND)
if os.path.exists(CAN_RECEIVE):
    os.remove(CAN_RECEIVE)
if os.path.exists(TASK_HARDWARE):
    os.remove(TASK_HARDWARE)
if os.path.exists(USER_TASKS):
    os.remove(USER_TASKS)

os.mkfifo(CAN_SEND,0666)
os.mkfifo(CAN_RECEIVE,0666)
os.mkfifo(TASK_HARDWARE,0666)
os.mkfifo(USER_TASKS,0666)

print "Executing CAN handler (C)"
Popen([HOMEDIR + "/C/CAN_HANDLER/CAN_HANDLER",CAN_RECEIVE,CAN_SEND])
print "Executing task_manager (python)"
Popen("python " + HOMEDIR + "/python/TaskManager/task_manager/task_manager.py " + CAN_RECEIVE + " " + CAN_SEND + " " + USER_TASKS, shell=True)
#placeholder = open(CAN_SEND, 'w')
