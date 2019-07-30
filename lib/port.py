
class port:

    def getPort(self, _label):
        while True:
            port = input(_label)

            try:
                port = int(port)

                if port == -1:
                    return port

                if port not in [7000, 8000, 9000]:
                    raise 'Invalid port number. Try again...'

                if port < 0 or port > 65535:
                    raise 'The port number must be between 0 and 65535...'

                return port
            except:
                print('-' * 35)
                print('Invalid port number. Try again...')
                print('-' * 35)
    
    def getSecAndTimeOut(self, _label):
        while True:
            secs = input('Enter with {} number: '.format(_label))

            try:
                seconds = int(secs)

                return seconds
            except:
                print('-' * 35)
                print('Invalid number. Try again...')
                print('-' * 35)
