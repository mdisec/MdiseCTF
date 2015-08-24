from twisted.internet import protocol, reactor, endpoints
from base64 import b64decode as decode
import cPickle
#
# cPickle module is vulnerable..! Look for RCE!
#

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        try:
            token = decode(data)
        except TypeError:
            self.transport.write("Token b64decode failure\n")
            return

        try:
            token = cPickle.loads(token)
        except cPickle.UnpicklingError:
            self.transport.write("Python cPickle UnpicklingError\n")
            return

        if type(token) is not dict:
            self.transport.write("Error. Input is not a python dict.!")
            return

        if 'pass' not in token:
            self.transport.write("Error. Dict does not have 'pass' key.")
            return

        if token['pass'] == "1234576":
            self.transport.write("TEBRIKLEEEER!\n")
            self.transport.write("Son bir adim kaldi. Flag /var/www/html/flag.txt!\n")
            self.transport.write("Merak ettiysen kaynak kod burada!\n")
            self.transport.write("""
                from twisted.internet import protocol, reactor, endpoints
                from base64 import b64decode as decode
                import cPickle
                #
                # cPickle module is vulnerable..! Look for RCE!
                #

                class Echo(protocol.Protocol):
                    def dataReceived(self, data):
                        try:
                            token = decode(data)
                        except TypeError:
                            self.transport.write("Token b64decode failure\n")
                            return

                        try:
                            token = cPickle.loads(token)
                        except cPickle.UnpicklingError:
                            self.transport.write("Python cPickle UnpicklingError\n")
                            return

                        if type(token) is not dict:
                            self.transport.write("Error. Input is not a python dict.!")
                            return

                        if 'pass' not in token:
                            self.transport.write("Error. Dict does not have 'pass' key.")
                            return

                        if token['pass'] == "1234576":
                            self.transport.write("TEBRIKLEEEER!\n")
                            self.transport.write("Merak ettiysen kaynak kod burada!")
                            self.transport.write("""

                                 """)
                        else:
                            self.transport.write("Wrong password..! Pass should be integer value.")


                class EchoFactory(protocol.Factory):
                    def buildProtocol(self, addr):
                        return Echo()


                endpoints.serverFromString(reactor, "tcp:1337").listen(EchoFactory())
                reactor.run()
                 """)
        else:
            self.transport.write("Wrong password..! Pass should be integer value.")


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:1337").listen(EchoFactory())
reactor.run()
