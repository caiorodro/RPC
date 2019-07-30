import rpyc
from rpyc.utils.server import ThreadedServer
from lib.port import port as p
import time
from datetime import datetime

class balance(rpyc.Service):

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_askToServerTime(self, host, port, secs, timeout):
        try:
            client = rpyc.connect(host, port)

            print("{} - Processing {} seconds request to {}:{}...".format(datetime.now().strftime('%d-%m-%Y %H:%M:%S'), str(secs), host, str(port)))
            print('-'*35)

            if client is not None:
                response = client.root.doTime(secs, timeout)

                print("{} - Time request processed!".format(datetime.now().strftime('%d-%m-%Y %H:%M:%S')))

                return response

        except Exception as err:
            print('Error in balance server')
            [print(item) for item in err.args if type(item) is str]
            raise err

if __name__ == "__main__":
    try:
        host = '127.0.0.1'
        port = 7000

        server = ThreadedServer(balance, hostname=host, port=port)
        print('Hey body! What can I do for you?. Press Ctrl+C to exit...')

        server.start()

    except Exception as err:
        if err.args[0] == 48:
            print('This server ({}: {}) is already used by another service'.format(host, str(port)))
        else:
            print(err)
