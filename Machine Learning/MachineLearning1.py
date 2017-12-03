from random import randint
_actions =  [lambda x:x+1, lambda x:0, lambda x: x/2, lambda x: x*100, lambda x: x%2]

class Machine:
    def __init__(self):
        self.commands = {}
        self.lastMod = 0
        self.lastCom = 0
    def command(self, cmd, num):
        if cmd not in self.commands:
            self.commands[cmd] = [1, 1, 1, 1, 1]
        apply = randint(1, sum([val for val in self.commands[cmd] if val > 0]))
        runningtotal = 0
        for counter, tester in enumerate(self.commands[cmd]):
            if tester > 0:
                runningtotal += tester
            if runningtotal >= apply:
                self.lastMod = counter
                self.lastCom = cmd
                return _actions[counter](num)
    def response(self,res):
        if res:
            self.commands[self.lastCom][self.lastMod] += 1
        else:
            self.commands[self.lastCom][self.lastMod] -= 2

