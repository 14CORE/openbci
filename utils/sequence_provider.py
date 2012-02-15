#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:
#     Mateusz Kruszyński <mateusz.kruszynski@gmail.com>

import random
class ConstantMgr(object):
    def __init__(self, v):
        self.v = v
    def get_value(self):
        return self.v

class RandomMgr(object):
    def __init__(self, start, count):
        self.start = start
        self.end = start+count-1

    def get_value(self):
        return random.randint(self.start, self.end)

class RandomConsMgr(object):
    def __init__(self, start, count):
        self.start = start
        self.end = start+count-1
        self.last = -1

    def get_value(self):
        while True:
            v = random.randint(self.start, self.end)
            if v == self.last:
                print("RandomConsMgr - try shuffle again...")
            else:
                self.last = v
                return v

class SequentialMgr(object):
    def __init__(self, start, count):
        self.sequence = range(start, start+count)
        self.count = count
        self.index = -1

    def get_value(self):
        self.index = (self.index + 1) % self.count
        return self.sequence[self.index]


class RandomSequentialMgr(object):
    def __init__(self, start, count):
        self.sequence = range(start, start+count)
        self.count = count
        self.index = 0
        random.shuffle(self.sequence)

    def get_value(self):
        self.index = (self.index + 1) % self.count
        if self.index == 0:
            if self.count > 1:
                #make sure old self.sequence[count-1] != new self.sequence[0]
                old_last = self.sequence[self.count-1]
                random.shuffle(self.sequence)
                if old_last == self.sequence[0]:
                    self.sequence[0] = self.sequence[self.count-1]
                    self.sequence[self.count-1] = old_last
                
        return self.sequence[self.index]



PROVIDERS = {
    'random':RandomMgr,
    'random_sequential': RandomSequentialMgr,
    'sequential':SequentialMgr,
    'random_cons':RandomConsMgr,
    'constant':ConstantMgr
}
