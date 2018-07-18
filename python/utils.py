import time


def get_run_time(func):
    def run_time(*args, **kw):
        start = time.clock()
        ret = func(*args, **kw)
        end = time.clock()
        print("Executed: {0} secs".format(end - start))
        return ret
    return run_time