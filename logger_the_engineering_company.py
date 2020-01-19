# log(entries with relevance) {"ERROR":8348376487}
# init(N)
# get_messages() - returns a collection of at most N messages, which are the top N messages by relevance sent to #log()
# M number of times log() called
import heapq


class Logger:
    def __init__(self, N):
        self.logs = []
        self.N = N

    def log(self, entry, relevance):  # "Error 1": 4,100,200; ...."Error 10":3,6,7 N = 4
        if len(self.logs) < self.N:
            heapq.heappush(self.logs, (relevance, entry))
        else:
            if relevance >= self.logs[0][0]:
                heapq.heapreplace(self.logs, (relevance, entry))

    def get_messages(self):
        result = []
        for (relevance, entry) in self.logs:
            result.append(entry)
        return result


logger = Logger(2)
logger.log("dkdkfnk1", 3)
logger.log("23fefc", 55643)
logger.log("eskufheufchnue", 34)
logger.log("rifjkreijvikfd", 35)
logger.log("jkfnke4jrne4knf", 55643)
logger.log("jkfnke4jrne4kdd", 55643)
logger.log("jkfnke4jrne4knfooooo", 55643)
print(logger.get_messages())
