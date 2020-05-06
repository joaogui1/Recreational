#! /usr/bin/python3
import os
import sys
import random as rnd

def hello():
    print("I'm awake")

def todo():
    with open(os.path.expanduser("~/todo")) as todofile:
        for line in todofile.readlines():
            print(line, end='')
        print()

def task():
    with open(os.path.expanduser("~/todo")) as todofile:
        line = rnd.choice(todofile.readlines())
        print(line)

def new_task():
    with open(os.path.expanduser("~/todo"), "a") as todofile:
        new_task = input("Tell me your new task\n")
        todofile.write(new_task + '\n')


def inspire():
    with open(os.path.expanduser("~/list")) as listfile:
        line = rnd.choice(listfile.readlines())
        print(line, end='')
def nothing():
    return 1

def end():
    sys.exit()

hello()
while(1):
    phrase = input().lower()
    commands = {"sleep":end, "todo":todo, "inspire me":inspire, "tell me what to do":task, "new task":new_task}
    commands.get(phrase, nothing)()
    #if(phrase == "sleep"):
        #commands["sleep"]
