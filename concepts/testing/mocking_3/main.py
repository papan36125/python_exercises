class HelloTest():
    def foo(self, msg):
        self.msg = msg.upper()
        self.bar(self.msg)

    def bar(self, MSG):
        print( MSG)
