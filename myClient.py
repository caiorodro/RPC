import rpyc
from rpyc import ThreadedServer
from serverBalance import balance
from lib.port import port as p
import sys

def makeTime(_client, _host, _port):
    """
    Makes a requests to Balance server with fixed port 7000 and it makes a rout by a port server time
    choosen by user

    Parameters:
    _client = client point connected in Balance server
    _host = IP address or name server of Balance server
    _port = the port number of Server time

    Returns:
    returns a string message of seconds processed or a timeout message
    """
    
    print('Type -1 to abort...')

    response = 'Operation aborted...'

    secs = iport.getSecAndTimeOut('seconds')

    if secs > -1:
        timeout = iport.getSecAndTimeOut('timeOut')

    if secs > -1 and timeout > -1:
        response = _client.root.askToServerTime(_host, _port, secs, timeout)

    return response

host = '127.0.0.1'
iport = p()

ports = [8000, 9000, -1]

line = '| Server Time: 127.0.0.1 | Port: {}'
width = len(line)+2

print('-' * width)
[(print(line.format(item))) for item in ports]
print('-' * width)

port = iport.getPort('Please, type a Server Time port number: ')

if port == -1:
    print('Ok, See you in next time')
    sys.exit()

try:
    client = rpyc.connect(host, 7000)

    print("You're now connected in balance server...")
    print('-'*35)

    if client is not None:
        response = makeTime(client, '127.0.0.1', port)

        print('-'*35)
        print(response)
        print('-'*35)

except Exception as err:
    [print(item) for item in err.args if type(item) is str]

print('See ya!')
