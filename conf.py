import sys
import getopt
import logger

class Conf:
    def __init__(self, optspec, usage):
        self.usage = usage
        self.path = None
        self.path_model = None
        self.__parseArgs("hm:" + optspec)

    def __parseArgs(self, optspec):
        try:
            opts, args = getopt.getopt(sys.argv[1:], optspec)
        except getopt.GetoptError:
            logger.error("invalid option")
            self.usage()
            exit(1)

        for o, a in opts:
            if o == '-h':
                self.usage()
                exit(0)
            elif o == '-m':
                self.path_model = a
            else:
                self.handleOpt(o, a)
        if len(args) < 1:
            return False

        self.path = args[0]
        return True

    def handleOpt(self, o, a):
        pass
