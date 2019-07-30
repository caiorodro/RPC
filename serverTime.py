import rpyc
from rpyc.utils.server import ThreadedServer
import time
from lib.port import port as p
from datetime import datetime

class timeService(rpyc.Service):

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_doTime(self, seconds=int, timeoutSecs=int):
        """
        This function sends seconds and timeout to server waits and return

        Parameters:
            seconds: You have to fill with Seconds (not miliseconds)
            timeoutSecs: Fill this parameters with max seconds the server will waits

        Returns: 
            A message with the seconds processed or a timeout message 
        """

        print('-'*45)
        print("{} - Receiving a new demand to process {} seconds...".format(datetime.now().strftime('%d-%m-%Y %H:%M:%S'), str(seconds)))

        retorno = None

        i = 0
        while i < seconds:
            time.sleep(1)

            if (i+1) > timeoutSecs:
                retorno = 'Timeout request. Max time for this request is {} seconds'.format(str(timeoutSecs))
                break

            i += 1

        if retorno is None:
            retorno = 'Your request was succesfully processed in {} seconds'.format(str(seconds))

        print("{} - Demand of {} seconds was successfuly processed...".format(datetime.now().strftime('%d-%m-%Y %H:%M:%S'), str(seconds)))
        print('-'*45)

        return retorno

if __name__ == "__main__":
    try:
        host = '127.0.0.1'
        port = p().getPort('Please, type a port number of Server Time: ')

        server = ThreadedServer(timeService, hostname=host, port=port)
        print("Hey body! I'm time server hosted in {} port. What can I do for you?. Press Ctrl+C to exit...".format(str(port)))
        
        server.start()
    except Exception as err:
        if err.args[0] == 48:
            print('This server ({}: {}) is already used by another service'.format(host, str(port)))
        else:
            [print(item) for item in err.args if type(item) is str]
