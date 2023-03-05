import os
import time

from metaflow import FlowSpec, step


class BranchFlow(FlowSpec):
    @step
    def start(self):
        self.next(self.a, self.b)

    @step
    def a(self):
        self.x = 1
        # Get process id
        print("Process ID: %s" % os.getpid())
        start_sleep = time.time()
        print(f"{start_sleep}: Sleeping for 5")

        time.sleep(5)
        print("Finished sleeping")
        self.next(self.join)

    @step
    def b(self):
        self.x = 2
        print("Process ID: %s" % os.getpid())

        start_sleep = time.time()
        print(f"{start_sleep}: Sleeping for 5")
        time.sleep(5)
        print("Finished sleeping")
        self.next(self.join)

    @step
    def join(self, inputs):
        print("a is %s" % inputs.a.x)
        print("b is %s" % inputs.b.x)
        print("total is %d" % sum(input.x for input in inputs))
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    BranchFlow()
