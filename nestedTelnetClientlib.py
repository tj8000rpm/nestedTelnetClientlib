#!/usr/bin/python3
import telnetlib

class NestedTelnetClient(object):
    def __init__(self):
        self.telnetInstance=None

    def connectWithTelnet(self, tuple_host_port, user, passwd, wait, encoding='euc-jp'):
        '''Connecting to the remote server/switch with telnet.

        This function switch the connecting behavior with member variable as context(self.telnetInstance).
        If you have not a existing telnet connection, this function will generate a new connection using telnetlib.
        On other hand, if you have a existing telnet connection, a like the jump server, 
        you can reuse a existing telnet connection, and telnet to remote server from currently connected server.
        
        Arguments:
        - tuple_host_port : A Tuple of remote host string, port number. The port can be omit.
        - user : A username of remote.
        - passwd : A password  stirng of remote.
        - wait : A string of waiting of the prompt.
        - encoding : A character encoding strings(such as 'euc-jp', 'utf-8')

        Returned:
        - telnetInstance : A object of telnetlib's instance. It was generated by this function or given from argument.
        '''

        telnetInstance=self.telnetInstance
        port=23
        if len(tuple_host_port)==2:
            host, port=tuple_host_port
            try:
                port=int(port)
            except ValueError:
                raise ValueError("invalid argument: tuple_host_port, port is not number")
        elif len(tuple_host_port)==1:
            host,=tuple_host_port
        else:
            raise ValueError("invalid argument: tuple_host_port, incorrect format")

        # in case argument telnetInstance is not exist, create new telnet session
        if not telnetInstance:
            telnetInstance=telnetlib.Telnet(host, )
        # in case argument telnetInstance is existed, send telnet command
        else:
            telnetInstance.write('telnet {} {}\n'.format(host,port).encode(encoding))

        telnetInstance.read_until(b'login')
        telnetInstance.write((user+'\n').encode(encoding))
        telnetInstance.read_until(b'Password')
        telnetInstance.write((passwd+'\n').encode(encoding))
        telnetInstance.read_until(wait.encode(encoding))
        self.telnetInstance=telnetInstance
        return telnetInstance

    def writeACommandAndGetResultSTDOUT(self, command, wait, encoding='euc-jp'):
        '''Write a given command on the telnet console and get command result from stdout.

        This function run a command and store a command result, through the exsiting telnet connection.
        The raw command result has contained 'ran command string' and 'waiting prompt after end of command result'.
        Those unnecessary strings will remove too with this function.

        Arguments:
        - command : A string you want to write in telnet console.
        - wait : A string of waiting of the prompt.
        - encoding : A character encoding strings(such as 'euc-jp', 'utf-8')

        Returned:
        - outputs : A list of string of command result on telnet console stdout, it was separated with ``\r\n``.
        '''
        telnetInstance=self.telnetInstance
        telnetInstance.write((command+'\n').encode(encoding))
        output=telnetInstance.read_until(wait.encode(encoding))
        output=output.decode(encoding)
        outputs=output.split('\r\n')[1:-1]  # strip written command and end line of waiitng prompt
        return outputs

def printOutputs(outputs):
    '''Debug function: The return value of ``writeACommandAndGetResultSTDOUT`` is printed on the screen.

    Arguments:
    - outputs : A list of string of command result on telnet console stdout, it was separated with ``\r\n``.

    Returned:
    - voided
    '''
    [print(line) for line in outputs]


