# BSD license
#
# Copyright (c) 2016 Kaadmy
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer. 
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies, 
# either expressed or implied, of the FreeBSD Project.

MODULE_AUTHOR  = "Kaadmy"
MODULE_VERSION = ["0", "1"]

####################
#      VECTOR      #
####################

X = R = 0
Y = G = 1
Z = B = 2
W = A = 3

class Vector:

    def __init__(self, size = 3, val = 0):

        self.axes = [0] * size

        if type(val) == list:
            for axis in range(len(val)):
                try: self.axes[axis] = val[axis]
                except: break
        else:
            self.axes = [val] * size


    def __str__(self):
        
        return " ".join([str(float(i)) for i in self.axes])
        
    def get(self, axis):
        
        return self.axes[axis]

    def set(self, axis, val = 0):
        
        self.axes[axis] = val

    def add(self, that):

        for axis in range(len(that.axes)):
            try: self.axes[axis] += that.axes[axis]
            except: break

    def sub(self, that):

        for axis in range(len(that.axes)):
            try: self.axes[axis] -= that.axes[axis]
            except: break

    def mul(self, that):

        for axis in range(len(that.axes)):
            try: self.axes[axis] *= that.axes[axis]
            except: break

    def div(self, that):

        for axis in range(len(that.axes)):
            try: self.axes[axis] /= that.axes[axis]
            except: break

####################
#     BZ WORLD     #
####################

INDENT = "  " # 2 spaces

def dump_tag(key, tag = None, indent = 0):
    
    if tag == None:
        return ((INDENT * indent) + key)
    else:
        return ((INDENT * indent) + key + " " + tag)

class World:

    def __init__(self, path = "pybzw_output.bzw", author = "UNKNOWN"):

        self.path = path
        self.author = author

        self.objects = []

    def save(self):

        print "Writing to " + self.path + "..."

        f = open(self.path, "w")

        header = "\n"
        header += "# PYBZW map export module v" + ".".join(MODULE_VERSION) + " by " + MODULE_AUTHOR + "\n"
        header += "# Map made by " + self.author + "\n"

        f.write(header)
        
        for obj in self.objects:

            objdata = "\n"

            if type(obj[1]) == list:
                if type(obj[0]) == list:
                    objdata += dump_tag(obj[0][0], obj[0][1]) + "\n"
                else:
                    objdata += dump_tag(obj[0]) + "\n"

                for tag in obj[1]:
                    try: objdata += dump_tag(tag[0], str(tag[1]), 1) + "\n"
                    except: objdata += dump_tag(tag[0], indent = 1) + "\n"

                objdata += dump_tag("end") + "\n"
            else:
                if obj[1] == None:
                    objdata += dump_tag(obj[0]) + "\n"
                else:
                    objdata += dump_tag(obj[0], str(obj[1])) + "\n"

            f.write(objdata)

        f.close()

        print "Successfully wrote " + str(len(self.objects)) + " objects to " + self.path

    def add_object(self, name, tags = []):

        self.objects.append([name, tags])
    
    def add_tag(self, name, tag = None):

        self.objects.append([name, tag])

    def add_box(self, pos = None, size = None, **kwargs):
        
        if pos == None:  pos  = Vector(3, 0)
        if size == None: size = Vector(3, 5)

        obj = [["pos", str(pos)], ["size", str(size)]]

        for key in kwargs:
            obj.append([key, kwargs[key]])

        self.add_object("box", obj)
