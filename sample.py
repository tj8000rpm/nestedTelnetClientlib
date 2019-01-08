#!/usr/bin/python3
from nestedTelnetClientlib import NestedTelnetClient

hosts=[
    {'host':'10.0.0.1', 'user':'your_username', 'password':'your_password', 'prompt':':~$', 'command':[
        'uname -n',
        'pwd',
        'ip link | grep eth0'
    ]},
    {'host':'10.0.0.2', 'user':'your_username', 'password':'your_password', 'prompt':':~$', 'command':[
    ]},
    {'host':'10.0.0.3', 'user':'your_username', 'password':'your_password', 'prompt':':~$', 'command':[
        'uname -n'
    ]}
]

tn=None
exit_prompt=[]
for target in hosts:
    host=target['host']
    user=target['user']
    passwd=target['password']
    prompt=target['prompt']
    exit_prompt.insert(0, prompt)
    commands=target['command']
    tn=NestedTelnetClient.loginServerWithTelnet(host, user, passwd, prompt, tn)
    for command in commands:
        outputs=NestedTelnetClient.sendMessage(tn, command, prompt)
        NestedTelnetClient.printOutputs(outputs)

exit_prompt.append('')
exit_prompt=exit_prompt[1:]
for prompt in exit_prompt:
    NestedTelnetClient.sendMessage(tn, 'exit', prompt)

