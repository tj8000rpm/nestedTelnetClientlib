#!/usr/bin/python3
import nestedTelnetClientlib
'''This is an example of using NestedTelnetClient

global config of nested telnet nodes
below example config/code is the accessing to three depth nested telnet nodes.
and run few commands in (1)node and (3)ndoe
> client(this program) -telnet-> (1)192.168.122.44 -telnet-> (2)localhost -telnet-> (3)192.168.122.44

exec order:
client > 
telnet(1)
    (1)node >
    uname -n
    pwd
    ip link | grep eth0
    telnet(2)
        (2)node >
        telnet(3)
            (3)node >
            uname -n
            exit
        exit
    exit
'''

# config as objects
hosts=[
    {'host':'192.168.122.44', 'user':'root', 'password':'root123', 'prompt':'~ #', 'command':[
        'uname -n',
        'pwd',
        'ip link | grep eth0'
    ]},
    {'host':'localhost', 'user':'root', 'password':'root123', 'prompt':'~ #', 'command':[
    ]},
    {'host':'192.168.122.44', 'user':'root', 'password':'root123', 'prompt':'~ #', 'command':[
        'uname -n'
    ]}
]

# create a new Client instance
tn=nestedTelnetClientlib.NestedTelnetClient()

exit_prompt=[]

# connect and run commands each remote server according to above config
for target in hosts:
    host=target['host']
    user=target['user']
    passwd=target['password']
    prompt=target['prompt']
    exit_prompt.insert(0, prompt)
    commands=target['command']
    tn.connectWithTelnet((host, 23), user, passwd, prompt)
    for command in commands:
        outputs=tn.writeACommandAndGetResultSTDOUT(command, prompt)
        nestedTelnetClientlib.printOutputs(outputs)

# get command history
outputs=tn.getCommandHistory()
nestedTelnetClientlib.printOutputs(outputs)

# graceful exit
exit_prompt.append('')
exit_prompt=exit_prompt[1:]
for prompt in exit_prompt:
    tn.writeACommandAndGetResultSTDOUT('exit', prompt)

