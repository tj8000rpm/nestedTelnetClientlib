#!/usr/bin/python3
import telnetlib

class NestedTelnetClient(object):
    def sendMessage(telnetInstance, command, wait, coding='euc-jp'):
        telnetInstance.write((command+'\n').encode(coding))
        output=telnetInstance.read_until(wait.encode(coding))
        output=output.decode(coding)
        outputs=output.split('\r\n')[1:-1]  # strip written command and end line
        return outputs

    def printOutputs(outputs):
        [print(line) for line in outputs]

    def loginServerWithTelnet(host, user, passwd, wait, telnetInstance=None, coding='euc-jp'):
        # in case argument telnetInstance is not exist, create new telnet session
        if not telnetInstance:
            telnetInstance=telnetlib.Telnet(host)
        # in case argument telnetInstance is existed, send telnet command
        else:
            telnetInstance.write('telnet {}\n'.format(host).encode(coding))
        telnetInstance.read_until(b'login')
        telnetInstance.write((user+'\n').encode(coding))
        telnetInstance.read_until(b'Password')
        telnetInstance.write((passwd+'\n').encode(coding))
        telnetInstance.read_until(wait.encode(coding))
        return telnetInstance

