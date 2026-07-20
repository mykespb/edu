#!/usr/bin/env python

# генератор uuid'ов (uuid4) in hex form
# Mikhail (myke) Kolodin, 2020
# 2020-12-09 0.1

import uuid

for i in range(10):
    print(uuid.uuid4().hex)

# ~ 0431758743904f699581adff67660db2
# ~ 04820f7631034a478aa22f5e2fce2690
# ~ ffbf80267e53465a90ecd0823f11b3cc
# ~ 0a3fa546c3a24cd8957661822f7c3f20
# ~ 65dfedffcaef47adabeb64125933e3b8
# ~ 9e25814dc0d140c69b05f683933e3698
# ~ 09e0a02d282446248d1e3a6fdd798519
# ~ 6844766b420141efb497778c16044ccb
# ~ 971841d4196f43e9b3e4dfb0a1daad69
# ~ 74b06beeb6c9421d9485df198f37972b
