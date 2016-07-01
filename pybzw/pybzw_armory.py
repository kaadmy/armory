#! /usr/bin/python2

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

import pybzw

USE_OCTACOLUMNS = False # use octagonal mesh columns instead of boxes

CL = 1.0 # column large
CS = 0.4 # column small

SS = 5 # shrub size

VW = 10 # vine width
VH = 16 # vine height

AW = 6 # arrow sign width
AH = 6 # arrow sign height

AR = 3 # armorypoint radius

bzw = pybzw.World("../armory.bzw", "KaadmY")

# world options
bzw.add_object("world", [["name", "\"Armory\""], ["size", 150]])
bzw.add_object("options", [
        ["-j"],
        ["+r"],
        ["-sb"],
        ["-fb"], ["+f", "KY{1}"], ["-set", "_maxFlagGrabs 5"],
        ["-ms", 4],
        ["-set", "_skyColor \"0.8 0.3 0.1\""]
        ])

# flowing water texture matrix
bzw.add_object("textureMatrix", [
        ["name", "flowingwater"],
        ["shift", "0.0 -2.0"]
        ])

# smaller textures for box sides
bzw.add_object("textureMatrix", [
        ["name", "small"],
        ["fixedscale", "0.5 0.5"]
        ])

# and a medium for glass sides
bzw.add_object("textureMatrix", [
        ["name", "medium"],
        ["fixedscale", "0.7 0.7"]
        ])

# large textures for glass tops
bzw.add_object("textureMatrix", [
        ["name", "large"],
        ["fixedscale", "2.0 2.0"]
        ])

# extra large textures for rock walls
bzw.add_object("textureMatrix", [
        ["name", "xlarge"],
        ["fixedscale", "3.0 3.0"]
        ])

# rock wall material
bzw.add_object("material", [
        ["name", "wall"],
        ["texture", "wall"],
        ["texmat", "xlarge"]
        ])

# octacolumn material
bzw.add_object("material", [
        ["name", "octacolumn"],
        ["texture", "pyrwall"],
        ])

# caution material
bzw.add_object("material", [
        ["name", "caution"],
        ["texture", "caution"],
        ])

# smallcaution material
bzw.add_object("material", [
        ["name", "smallcaution"],
        ["texture", "caution"],
        ["texmat", "small"],
        ])

# glass material
bzw.add_object("material", [
        ["name", "glass"],
        ["texture", "telelink"],
        ["diffuse", "0.8 0.8 1.0 0.6"],
        ["texmat", "large"],
        ["spheremap"],
        ])

# smallglass material
bzw.add_object("material", [
        ["name", "smallglass"],
        ["texture", "telelink"],
        ["diffuse", "0.8 0.8 1.0 0.6"],
        ["texmat", "medium"],
        ["spheremap"],
        ])

# shrub material
bzw.add_object("material", [
        ["name", "shrub"],
        ["nosorting"],
        ["noculling"],
        ["noradar"],
        ["noshadow"],
        ["nolighting"],
        ["alphathresh", 0.6],
        ["diffuse", "0.0 1.0 0.0 1.0"],
        ["texture", "http://images.bzflag.org/bz_legacy/louman/churchyard/shrub.png"],
        ])

# purple shrub material
bzw.add_object("material", [
        ["name", "purpleshrub"],
        ["nosorting"],
        ["noculling"],
        ["noradar"],
        ["noshadow"],
        ["nolighting"],
        ["alphathresh", 0.6],
        ["diffuse", "1.0 0.0 1.0 1.0"],
        ["texture", "http://images.bzflag.org/bz_legacy/louman/churchyard/shrub.png"],
        ])

# vines material
bzw.add_object("material", [
        ["name", "vines"],
        ["nosorting"],
        ["noradar"],
        ["noshadow"],
        ["alphathresh", 0.6],
        ["texture", "http://images.bzflag.org/bz_legacy/louman/churchyard/treeleaves.png"],
        ])

# arrow sign material
bzw.add_object("material", [
        ["name", "arrowsign"],
        ["nosorting"],
        ["noradar"],
        ["noshadow"],
        ["alphathresh", 0.6],
        ["texture", "http://images.bzflag.org/kdmy/arrow.png"],
        ])

# armorypoint material
bzw.add_object("material", [
        ["name", "armorypoint"],
        ["noshadow"],
        ["alphathresh", 0.6],
        ["texture", "http://images.bzflag.org/kdmy/armorypoint.png"],
        ])

# flowing water material
bzw.add_object("material", [
        ["name", "flowingwater"],
        ["nosorting"],
        ["noculling"],
        ["noradar"],
        ["noshadow"],
        ["nolighting"],
        ["texture", "water"],
        ["diffuse", "0.9 0.9 1.0 0.8"],
        ["texmat", "flowingwater"]
        ])

# armorypoint
bzw.add_tag("define", "armorypoint")

bzw.add_object("mesh", [
        ["vertex", pybzw.Vector(val = [-AR,  AR, 0])], # 0
        ["vertex", pybzw.Vector(val = [ AR,  AR, 0])], # 1
        ["vertex", pybzw.Vector(val = [ AR, -AR, 0])], # 2
        ["vertex", pybzw.Vector(val = [-AR, -AR, 0])], # 3

        ["texcoord", pybzw.Vector(2, [0, 1])], # 0
        ["texcoord", pybzw.Vector(2, [1, 1])], # 1
        ["texcoord", pybzw.Vector(2, [1, 0])], # 2
        ["texcoord", pybzw.Vector(2, [0, 0])], # 3

        ["matref", "armorypoint"],

        ["face", "# north"],
        [" vertices",  "3 2 1 0"],
        [" texcoords", "0 1 2 3"],
        [" passable"],
        ["endface"],
        ])

bzw.add_tag("enddef")

# shrub
bzw.add_tag("define", "shrub")

bzw.add_object("mesh", [
        ["vertex", pybzw.Vector(val = [-SS / 2, 0, SS])], # 0
        ["vertex", pybzw.Vector(val = [ SS / 2, 0, SS])], # 1
        ["vertex", pybzw.Vector(val = [ SS / 2, 0, 0])], # 2
        ["vertex", pybzw.Vector(val = [-SS / 2, 0, 0])], # 3

        ["vertex", pybzw.Vector(val = [0, -SS / 2, SS])], # 4
        ["vertex", pybzw.Vector(val = [0,  SS / 2, SS])], # 5
        ["vertex", pybzw.Vector(val = [0,  SS / 2, 0])], # 6
        ["vertex", pybzw.Vector(val = [0, -SS / 2, 0])], # 7

        ["texcoord", pybzw.Vector(2, [0, 1])], # 0
        ["texcoord", pybzw.Vector(2, [1, 1])], # 1
        ["texcoord", pybzw.Vector(2, [1, 0])], # 2
        ["texcoord", pybzw.Vector(2, [0, 0])], # 3

        ["matref", "shrub"],

        ["face", "# north-south"],
        [" vertices",  "0 1 2 3"],
        [" texcoords", "0 1 2 3"],
        [" passable"],
        ["endface"],

        ["face", "# east-west"],
        [" vertices",  "4 5 6 7"],
        [" texcoords", "0 1 2 3"],
        [" passable"],
        ["endface"],
        ])

bzw.add_tag("enddef")

# purple shrub
bzw.add_tag("define", "purpleshrub")

bzw.add_object("mesh", [
        ["vertex", pybzw.Vector(val = [-SS, 0, SS])], # 0
        ["vertex", pybzw.Vector(val = [ SS, 0, SS])], # 1
        ["vertex", pybzw.Vector(val = [ SS, 0, 0])], # 2
        ["vertex", pybzw.Vector(val = [-SS, 0, 0])], # 3

        ["vertex", pybzw.Vector(val = [0, -SS, SS])], # 4
        ["vertex", pybzw.Vector(val = [0,  SS, SS])], # 5
        ["vertex", pybzw.Vector(val = [0,  SS, 0])], # 6
        ["vertex", pybzw.Vector(val = [0, -SS, 0])], # 7

        ["texcoord", pybzw.Vector(2, [0, 1])], # 0
        ["texcoord", pybzw.Vector(2, [1, 1])], # 1
        ["texcoord", pybzw.Vector(2, [1, 0])], # 2
        ["texcoord", pybzw.Vector(2, [0, 0])], # 3

        ["matref", "purpleshrub"],

        ["face", "# north-south"],
        [" vertices",  "0 1 2 3"],
        [" texcoords", "0 1 2 3"],
        [" passable"],
        ["endface"],

        ["face", "# east-west"],
        [" vertices",  "4 5 6 7"],
        [" texcoords", "0 1 2 3"],
        [" passable"],
        ["endface"],
        ])

bzw.add_tag("enddef")

# vines
bzw.add_tag("define", "vines")

bzw.add_object("mesh", [
        ["vertex", pybzw.Vector(val = [-VW / 2, 0.1, 0])], # 0
        ["vertex", pybzw.Vector(val = [ VW / 2, 0.1, 0])], # 1
        ["vertex", pybzw.Vector(val = [ VW / 2, 0.1, -VH])], # 2
        ["vertex", pybzw.Vector(val = [-VW / 2, 0.1, -VH])], # 3

        ["texcoord", pybzw.Vector(2, [0, 1])], # 0
        ["texcoord", pybzw.Vector(2, [1, 1])], # 1
        ["texcoord", pybzw.Vector(2, [1, 0])], # 2
        ["texcoord", pybzw.Vector(2, [0, 0])], # 3

        ["matref", "vines"],

        ["face", "# north"],
        [" vertices",  "0 1 2 3"],
        [" texcoords", "0 1 2 3"],
        [" passable"],
        ["endface"],
        ])

bzw.add_tag("enddef")

# wide vines
bzw.add_tag("define", "widevines")

bzw.add_object("mesh", [
        ["vertex", pybzw.Vector(val = [-VW, 0.1, 0])], # 0
        ["vertex", pybzw.Vector(val = [ VW, 0.1, 0])], # 1
        ["vertex", pybzw.Vector(val = [ VW, 0.1, -VH])], # 2
        ["vertex", pybzw.Vector(val = [-VW, 0.1, -VH])], # 3

        ["texcoord", pybzw.Vector(2, [0, 1])], # 0
        ["texcoord", pybzw.Vector(2, [1, 1])], # 1
        ["texcoord", pybzw.Vector(2, [1, 0])], # 2
        ["texcoord", pybzw.Vector(2, [0, 0])], # 3

        ["matref", "vines"],

        ["face", "# north"],
        [" vertices",  "0 1 2 3"],
        [" texcoords", "0 1 2 3"],
        [" passable"],
        ["endface"],
        ])

bzw.add_tag("enddef")

# arrow sign
bzw.add_tag("define", "arrowsign")

bzw.add_object("mesh", [
        ["vertex", pybzw.Vector(val = [-AW / 2, 0.1, AH])], # 0
        ["vertex", pybzw.Vector(val = [ AW / 2, 0.1, AH])], # 1
        ["vertex", pybzw.Vector(val = [ AW / 2, 0.1, 0])], # 2
        ["vertex", pybzw.Vector(val = [-AW / 2, 0.1, 0])], # 3

        ["texcoord", pybzw.Vector(2, [0, 1])], # 0
        ["texcoord", pybzw.Vector(2, [1, 1])], # 1
        ["texcoord", pybzw.Vector(2, [1, 0])], # 2
        ["texcoord", pybzw.Vector(2, [0, 0])], # 3

        ["matref", "arrowsign"],

        ["face", "# north"],
        [" vertices",  "0 1 2 3"],
        [" texcoords", "0 1 2 3"],
        [" passable"],
        ["endface"],
        ])

bzw.add_tag("enddef")

# 43-unit octagonal column walls
bzw.add_tag("define", "octacolumn_long")

# Vertex order(clockwise from lower-right)
# 3 > 4
# ^   v
# 2 < 1 <

#      8   9
#       0 1
#        N
# 15 NE     NW 11
#   6   +y    3
#    W   L+x E
#   7         2
# 14 SE     SW 10
#        S
#       4 5
#     12   13

if USE_OCTACOLUMNS:
    bzw.add_object("mesh", [
            ["vertex", pybzw.Vector(val = [-CS,  CL,  0])], # 0
            ["vertex", pybzw.Vector(val = [ CS,  CL,  0])], # 1

            ["vertex", pybzw.Vector(val = [ CL, -CS,  0])], # 2
            ["vertex", pybzw.Vector(val = [ CL,  CS,  0])], # 3

            ["vertex", pybzw.Vector(val = [-CS, -CL,  0])], # 4
            ["vertex", pybzw.Vector(val = [ CS, -CL,  0])], # 5

            ["vertex", pybzw.Vector(val = [-CL,  CS,  0])], # 6
            ["vertex", pybzw.Vector(val = [-CL, -CS,  0])], # 7

            ["vertex", pybzw.Vector(val = [-CS,  CL, 43])], # 8
            ["vertex", pybzw.Vector(val = [ CS,  CL, 43])], # 9

            ["vertex", pybzw.Vector(val = [ CL, -CS, 43])], # 10
            ["vertex", pybzw.Vector(val = [ CL,  CS, 43])], # 11

            ["vertex", pybzw.Vector(val = [-CS, -CL, 43])], # 12
            ["vertex", pybzw.Vector(val = [ CS, -CL, 43])], # 13

            ["vertex", pybzw.Vector(val = [-CL, -CS, 43])], # 14
            ["vertex", pybzw.Vector(val = [-CL,  CS, 43])], # 15

            ["matref", "octacolumn"],

            ["face", "# north"],
            [" vertices", "1 0 8 9"],
            ["endface"],

            ["face", "# north-east"],
            [" vertices", "3 1 9 11"],
            ["endface"],

            ["face", "# east"],
            [" vertices", "2 3 11 10"],
            ["endface"],

            ["face", "# south-east"],
            [" vertices", "5 2 10 13"],
            ["endface"],

            ["face", "# south"],
            [" vertices", "4 5 13 12"],
            ["endface"],

            ["face", "# south-west"],
            [" vertices", "7 4 12 14"],
            ["endface"],

            ["face", "# west"],
            [" vertices", "6 7 14 15"],
            ["endface"],

            ["face", "# north-west"],
            [" vertices", "0 6 15 8"],
            ["endface"],

            ["face", "# top north"],
            [" vertices", "14 11 9 8"],
            ["endface"],

            ["face", "# top middle"],
            [" vertices", "15 10 11 14"],
            ["endface"],

            ["face", "# top south"],
            [" vertices", "12 13 10 15"],
            ["endface"],

            ["inside", pybzw.Vector(val = [0, 0, 10])],

            ["smoothbounce"],
            ])
else:
    bzw.add_object("box", [
            ["pos", pybzw.Vector(val = [0, 0, 0])],
            ["size", pybzw.Vector(val = [CL, CL, 43])],
            ["matref", "octacolumn"]
            ])

bzw.add_tag("enddef")

# 23-unit octagonal column walls
bzw.add_tag("define", "octacolumn")

# Vertex order(clockwise from lower-right)
# 3 > 4
# ^   v
# 2 < 1 <

#      8   9
#       0 1
#        N
# 15 NE     NW 11
#   6   +y    3
#    W   L+x E
#   7         2
# 14 SE     SW 10
#        S
#       4 5
#     12   13

if USE_OCTACOLUMNS:
    bzw.add_object("mesh", [
            ["vertex", pybzw.Vector(val = [-CS,  CL,  0])], # 0
            ["vertex", pybzw.Vector(val = [ CS,  CL,  0])], # 1

            ["vertex", pybzw.Vector(val = [ CL, -CS,  0])], # 2
            ["vertex", pybzw.Vector(val = [ CL,  CS,  0])], # 3

            ["vertex", pybzw.Vector(val = [-CS, -CL,  0])], # 4
            ["vertex", pybzw.Vector(val = [ CS, -CL,  0])], # 5

            ["vertex", pybzw.Vector(val = [-CL,  CS,  0])], # 6
            ["vertex", pybzw.Vector(val = [-CL, -CS,  0])], # 7

            ["vertex", pybzw.Vector(val = [-CS,  CL, 23])], # 8
            ["vertex", pybzw.Vector(val = [ CS,  CL, 23])], # 9

            ["vertex", pybzw.Vector(val = [ CL, -CS, 23])], # 10
            ["vertex", pybzw.Vector(val = [ CL,  CS, 23])], # 11

            ["vertex", pybzw.Vector(val = [-CS, -CL, 23])], # 12
            ["vertex", pybzw.Vector(val = [ CS, -CL, 23])], # 13

            ["vertex", pybzw.Vector(val = [-CL, -CS, 23])], # 14
            ["vertex", pybzw.Vector(val = [-CL,  CS, 23])], # 15

            ["matref", "octacolumn"],

            ["face", "# north"],
            [" vertices", "1 0 8 9"],
            ["endface"],

            ["face", "# north-east"],
            [" vertices", "3 1 9 11"],
            ["endface"],

            ["face", "# east"],
            [" vertices", "2 3 11 10"],
            ["endface"],

            ["face", "# south-east"],
            [" vertices", "5 2 10 13"],
            ["endface"],

            ["face", "# south"],
            [" vertices", "4 5 13 12"],
            ["endface"],

            ["face", "# south-west"],
            [" vertices", "7 4 12 14"],
            ["endface"],

            ["face", "# west"],
            [" vertices", "6 7 14 15"],
            ["endface"],

            ["face", "# north-west"],
            [" vertices", "0 6 15 8"],
            ["endface"],

            ["face", "# top north"],
            [" vertices", "14 11 9 8"],
            ["endface"],

            ["face", "# top middle"],
            [" vertices", "15 10 11 14"],
            ["endface"],

            ["face", "# top south"],
            [" vertices", "12 13 10 15"],
            ["endface"],

            ["inside", pybzw.Vector(val = [0, 0, 10])],

            ["smoothbounce"],
            ])
else:
    bzw.add_object("box", [
            ["pos", pybzw.Vector(val = [0, 0, 0])],
            ["size", pybzw.Vector(val = [CL, CL, 23])],
            ["matref", "octacolumn"]
            ])

bzw.add_tag("enddef")

# full platform prefab
bzw.add_tag("define", "platform_full")

bzw.add_object(["group", "octacolumn"], [
        ["shift", pybzw.Vector(val = [-10, 10, 0])]
        ])
bzw.add_object(["group", "octacolumn_top"], [
        ["shift", pybzw.Vector(val = [-10, 10, 23])]
        ])

bzw.add_object(["group", "octacolumn"], [
        ["shift", pybzw.Vector(val = [-10, -10, 0])]
        ])
bzw.add_object(["group", "octacolumn_top"], [
        ["shift", pybzw.Vector(val = [-10, -10, 23])]
        ])

bzw.add_object(["group", "octacolumn"], [
        ["shift", pybzw.Vector(val = [10, -10, 0])]
        ])
bzw.add_object(["group", "octacolumn_top"], [
        ["shift", pybzw.Vector(val = [10, -10, 23])]
        ])

bzw.add_object(["group", "octacolumn"], [
        ["shift", pybzw.Vector(val = [10, 10, 0])]
        ])
bzw.add_object(["group", "octacolumn_top"], [
        ["shift", pybzw.Vector(val = [10, 10, 23])]
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, 0, 0])],
        ["size", pybzw.Vector(val = [10, 10, 8])],
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, 0, 18])],
        ["size", pybzw.Vector(val = [10, 10, 2])],
        ])

bzw.add_tag("enddef")

# half platform prefab(columns are on north side)
bzw.add_tag("define", "platform_half")

bzw.add_object(["group", "octacolumn"], [
        ["shift", pybzw.Vector(val = [-10, 10, 0])]
        ])
bzw.add_object(["group", "octacolumn"], [
        ["shift", pybzw.Vector(val = [10, 10, 0])]
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, 0, 0])],
        ["size", pybzw.Vector(val = [10, 10, 8])],
        ])
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, 0, 18])],
        ["size", pybzw.Vector(val = [10, 10, 2])],
        ])

bzw.add_tag("enddef")

# tower prefab
bzw.add_tag("define", "tower")

bzw.add_object(["group", "octacolumn_long"], [
        ["shift", pybzw.Vector(val = [-5, 5, 0])]
        ])
bzw.add_object(["group", "octacolumn_long"], [
        ["shift", pybzw.Vector(val = [-5, -5, 0])]
        ])
bzw.add_object(["group", "octacolumn_long"], [
        ["shift", pybzw.Vector(val = [5, -5, 0])]
        ])
bzw.add_object(["group", "octacolumn_long"], [
        ["shift", pybzw.Vector(val = [5, 5, 0])]
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, 0, 8])],
        ["size", pybzw.Vector(val = [5, 5, 2])],
        ])
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, 0, 18])],
        ["size", pybzw.Vector(val = [5, 5, 2])],
        ])
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, 0, 28])],
        ["size", pybzw.Vector(val = [5, 5, 2])],
        ])
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, 0, 38])],
        ["size", pybzw.Vector(val = [5, 5, 2])],
        ])

bzw.add_tag("enddef")

# key spawn zone
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [-130, -80, 0])],
        ["size", pybzw.Vector(val = [5, 5, 0.2])]
        ])

bzw.add_object("zone", [
        ["pos", pybzw.Vector(val = [-130, -80, 1])],
        ["size", pybzw.Vector(val = [5, 5, 5])],
        ["flag", "KY"]
        ])

# some shrubs around key to partially hide it
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [-122, -77, 0])]
        ])
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [-120, -82, 0])]
        ])
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [-123, -88, 0])]
        ])
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [-124, -90, 0])]
        ])

# attackers' spawns
for x in range(-140, -20, 30):
    bzw.add_object("box", [
            ["pos", pybzw.Vector(val = [x, -120, 0])],
            ["size", pybzw.Vector(val = [5, 5, 1.75])],
            ["top matref", "caution"],
            ["bottom matref", "caution"],
            ["sides matref", "smallcaution"],
            ])
    bzw.add_object("zone", [
            ["pos", pybzw.Vector(val = [x, -120, 1.75])],
            ["size", pybzw.Vector(val = [3, 3, 5])],
            ["team", 1],
            ])

# defenders' spawns
for x in range(40, 120, 30):
    bzw.add_object("box", [
            ["pos", pybzw.Vector(val = [x, -120, 0])],
            ["size", pybzw.Vector(val = [5, 5, 1.75])],
            ["top matref", "caution"],
            ["bottom matref", "caution"],
            ["sides matref", "smallcaution"],
            ])
    bzw.add_object("zone", [
            ["pos", pybzw.Vector(val = [x, -120, 1.75])],
            ["size", pybzw.Vector(val = [3, 3, 5])],
            ["team", 2],
            ])

# west ramparts
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [-106, 12, 0])]
        ])
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [-107, 10, 0])]
        ])

bzw.add_object(["group", "vines"], [
        ["shift", pybzw.Vector(val = [-140, -10, 20])],
        ["rot", 180]
        ])

bzw.add_object(["group", "arrowsign"], [
        ["scale", "1 -1 1"],
        ["shift", pybzw.Vector(val = [-110, 0, 1])],
        ["rot", -90]
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [-140, 0, 0])],
        ["size", pybzw.Vector(val = [10, 10, 20])],
        ])

bzw.add_object(["group", "platform_full"], [
        ["shift", pybzw.Vector(val = [-120, 0, 0])],
        ])

bzw.add_object(["group", "platform_half"], [
        ["shift", pybzw.Vector(val = [-120, 20, 0])],
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [-120, 40, 1.55])],
        ["size", pybzw.Vector(val = [5, 10, 6.35])],
        ["top matref", "glass"],
        ["bottom matref", "glass"],
        ["sides matref", "smallglass"],
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [-120, 70, 0])],
        ["size", pybzw.Vector(val = [10, 20, 20])],
        ])

# northwest tower
bzw.add_object(["group", "tower"], [
        ["shift", pybzw.Vector(val = [-90, 70, 0])],
        ])

# north outer ramparts
bzw.add_object(["group", "platform_full"], [
        ["shift", pybzw.Vector(val = [-120, 100, 0])],
        ])

bzw.add_object(["group", "platform_half"], [
        ["shift", pybzw.Vector(val = [-100, 100, 0])],
        ["rot", -90],
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [-80, 100, 1.55])],
        ["size", pybzw.Vector(val = [10, 5, 6.35])],
        ["top matref", "glass"],
        ["bottom matref", "glass"],
        ["sides matref", "smallglass"],
        ])

# center barred wall
bzw.add_object(["group", "arrowsign"], [
        ["spin", "45 0 1 0"],
        ["shift", pybzw.Vector(val = [-67, 90.05, 12])],
        ["rot", 180],
        ])

bzw.add_object(["group", "vines"], [
        ["shift", pybzw.Vector(val = [-60, 90, 20])],
        ["rot", 180]
        ])
bzw.add_object(["group", "vines"], [
        ["scale", "-1 1 1"],
        ["shift", pybzw.Vector(val = [-50, 90, 16])],
        ["rot", 180],
        ])
bzw.add_object("box", [ # west
        ["pos", pybzw.Vector(val = [-50, 100, 0])],
        ["size", pybzw.Vector(val = [20, 10, 20])],
        ])
bzw.add_object(["group", "arrowsign"], [
        ["scale", "-1 1 1"],
        ["shift", pybzw.Vector(val = [40, 90, 2])],
        ["rot", 180],
        ])
bzw.add_object(["group", "vines"], [
        ["shift", pybzw.Vector(val = [40, 110, 16])],
        ])
bzw.add_object("box", [ # east
        ["pos", pybzw.Vector(val = [50, 100, 0])],
        ["size", pybzw.Vector(val = [20, 10, 20])],
        ])

bzw.add_object("box", [ # lower beam
        ["pos", pybzw.Vector(val = [0, 100, 0])],
        ["size", pybzw.Vector(val = [30, 3, 1])],
        ["top matref", "glass"],
        ["bottom matref", "glass"],
        ["sides matref", "smallglass"],
        ])
bzw.add_object("box", [ # upper beam
        ["pos", pybzw.Vector(val = [0, 100, 19])],
        ["size", pybzw.Vector(val = [30, 3, 0.9])],
        ["top matref", "glass"],
        ["bottom matref", "glass"],
        ["sides matref", "smallglass"],
        ])
for x in range(-28, 30, 5): # bars
    bzw.add_object("box", [
            ["pos", pybzw.Vector(val = [x + 0.25, 100, 1])],
            ["size", pybzw.Vector(val = [1, 1, 18])],
            ["top matref", "glass"],
            ["bottom matref", "glass"],
            ["sides matref", "smallglass"],
            ]
)
# teleporters
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [-45, 117, 0])]
        ])
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [-43, 118, 0])]
        ])
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [-46, 120, 0])]
        ])

bzw.add_object(["teleporter", "bars_lower"], [
        ["pos", pybzw.Vector(val = [-40, 120, 0])],
        ["size", pybzw.Vector(val = [-0.125, 3, 8])],
        ["rot", 90],
        ["border", 1.0]
        ])
bzw.add_object(["teleporter", "bars_upper"], [
        ["pos", pybzw.Vector(val = [-40, 100, 20])],
        ["size", pybzw.Vector(val = [-0.125, 3, 8])],
        ["border", 1.0]
        ])

bzw.add_object("link", [ # link lower to upper' back
        ["name", "teleporters_bars"],
        ["from", "bars_lower:f"],
        ["to", "bars_upper:b"],
        ])
bzw.add_object("link", [ # link lower to upper's front
        ["name", "teleporters_bars"],
        ["from", "bars_lower:b"],
        ["to", "bars_upper:f"],
        ])

bzw.add_object("link", [ # link upper to lower's back
        ["name", "teleporters_bars"],
        ["from", "bars_upper:f"],
        ["to", "bars_lower:b"],
        ])
bzw.add_object("link", [ # link upper to lower's front
        ["name", "teleporters_bars"],
        ["from", "bars_upper:b"],
        ["to", "bars_lower:f"],
        ])

# center walls/platforms
bzw.add_object(["group", "platform_full"], [
        ["shift", pybzw.Vector(val = [-40, 20, 0])],
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [-40, 0, 1.55])],
        ["size", pybzw.Vector(val = [5, 10, 6.35])],
        ["top matref", "glass"],
        ["bottom matref", "glass"],
        ["sides matref", "smallglass"],
        ])

bzw.add_object(["group", "platform_full"], [
        ["shift", pybzw.Vector(val = [-40, -20, 0])],
        ])
bzw.add_object(["group", "platform_half"], [
        ["shift", pybzw.Vector(val = [-20, -20, 0])],
        ["rot", -90],
        ])

bzw.add_object(["group", "widevines"], [
        ["shift", pybzw.Vector(val = [30, 30, 25])],
        ["rot", -90]
        ])
bzw.add_object(["group", "vines"], [
        ["shift", pybzw.Vector(val = [30, 50, 30])],
        ["rot", -90]
        ])
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [20, 20, 0])],
        ["size", pybzw.Vector(val = [10, 50, 40])],
        ["matref", "wall"]
        ])

bzw.add_object(["group", "arrowsign"], [
        ["scale", "-1 1 1"],
        ["spin", "-45 0 1 0"],
        ["shift", pybzw.Vector(val = [60, 10, 10])],
        ])
bzw.add_object(["group", "vines"], [
        ["shift", pybzw.Vector(val = [90, 3, 34])],
        ["rot", -90]
        ])
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [60, 0, 0])],
        ["size", pybzw.Vector(val = [30, 10, 40])],
        ["matref", "wall"]
        ])
# waterfall
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [30, 45, 0])],
        ["size", pybzw.Vector(val = [3, 5, 35])],
        ["matref", "flowingwater"],
        ["passable"],
        ])

# river
bzw.add_object(["group", "shrub"], [
        ["shift", pybzw.Vector(val = [120, 60, 0])]
        ])
bzw.add_object(["group", "shrub"], [
        ["scale", "2.3 2.3 0.8"],
        ["shift", pybzw.Vector(val = [118, 54, 0])],
        ])

bzw.add_object("box", [ # north bank
        ["pos", pybzw.Vector(val = [90, 51.5, 0])],
        ["size", pybzw.Vector(val = [60, 0.5, 1.5])],
        ["matref", "wall"],
        ])
bzw.add_object("box", [ # south bank
        ["pos", pybzw.Vector(val = [90, 38.5, 0])],
        ["size", pybzw.Vector(val = [60, 0.5, 1.5])],
        ["matref", "wall"],
        ])
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [90, 45, 0])],
        ["size", pybzw.Vector(val = [6.2, 60.1, 1])],
        ["rot", 90],
        ["matref", "flowingwater"],
        ["passable"]
        ])

# main mid wall
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, -40, 0])],
        ["size", pybzw.Vector(val = [10, 30, 40])],
        ])
bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [0, -140, 0])],
        ["size", pybzw.Vector(val = [10, 10, 40])],
        ])

bzw.add_object("box", [ # lower  beam
        ["pos", pybzw.Vector(val = [0, -100, 0])],
        ["size", pybzw.Vector(val = [3, 30, 1])],
        ])
bzw.add_object("box", [ # glass
        ["pos", pybzw.Vector(val = [0, -100, 2])],
        ["size", pybzw.Vector(val = [1, 30, 18])],
        ["top matref", "glass"],
        ["bottom matref", "glass"],
        ["sides matref", "smallglass"],
        ])
bzw.add_object("box", [ # upper beam
        ["pos", pybzw.Vector(val = [0, -100, 20])],
        ["size", pybzw.Vector(val = [3, 30, 20])],
        ])

bzw.add_object(["group", "purpleshrub"], [
        ["shift", pybzw.Vector(val = [18, -43, 0])],
        ])
bzw.add_object(["group", "purpleshrub"], [
        ["shift", pybzw.Vector(val = [14, -40, 0])],
        ])
bzw.add_object(["group", "purpleshrub"], [
        ["shift", pybzw.Vector(val = [17, -36, 0])],
        ])

bzw.add_object(["group", "arrowsign"], [
        ["spin", "-45 1 0 0"],
        ["shift", pybzw.Vector(val = [10, -55, 13])],
        ["rot", -90],
        ])
bzw.add_object("box", [ # lower step
        ["pos", pybzw.Vector(val = [15, -55, 8])],
        ["size", pybzw.Vector(val = [5, 5, 2])],
        ])
bzw.add_object("box", [ # upper step before armory
        ["pos", pybzw.Vector(val = [6.5, -90, 20])],
        ["size", pybzw.Vector(val = [3.5, 5, 2])],
        ])
bzw.add_object("box", [ # upper step with armory
        ["pos", pybzw.Vector(val = [6.5, -125, 20])],
        ["size", pybzw.Vector(val = [3.5, 5, 2])],
        ])

# east ramparts
bzw.add_object(["group", "arrowsign"], [
        ["scale", "-1 1 1"],
        ["shift", pybzw.Vector(val = [140, 10, 1])],
        ])
bzw.add_object(["group", "platform_full"], [
        ["shift", pybzw.Vector(val = [140, 0, 0])],
        ])

bzw.add_object("box", [
        ["pos", pybzw.Vector(val = [110, 0, 2.55])],
        ["size", pybzw.Vector(val = [20, 5, 5.35])],
        ["top matref", "glass"],
        ["bottom matref", "glass"],
        ["sides matref", "smallglass"],
        ])

# center tower
bzw.add_object(["group", "tower"], [
        ["shift", pybzw.Vector(val = [-10, 10, 0])],
        ])

# southeast tower
bzw.add_object(["group", "tower"], [
        ["shift", pybzw.Vector(val = [130, -90, 0])],
        ])

# armory gamemode stuff
bzw.add_object("armorypoint", [ # first armorypoint; Gate
        ["pos", pybzw.Vector(val = [-80, -10, -0.1])],
        ["size", pybzw.Vector(val = [AR, AR, 5])],
        ["title", "\"The Gate\""],
        ["name", "\"gate\""],
        ["unlock", "\"roof\""],
        ])
bzw.add_object(["group", "armorypoint"], [
        ["shift", pybzw.Vector(val = [-80, -10, 0])],
        ])

bzw.add_object("armorypoint", [ # second armorypoint; Roof
        ["pos", pybzw.Vector(val = [-120, 60, 19.9])],
        ["size", pybzw.Vector(val = [AR, AR, 5])],
        ["title", "\"The Roof\""],
        ["name", "\"roof\""],
        ["unlock", "\"bridge\""],
        ])
bzw.add_object(["group", "armorypoint"], [
        ["shift", pybzw.Vector(val = [-120, 60, 20.1])],
        ])

bzw.add_object("armorypoint", [ # third armorypoint; Bridge
        ["pos", pybzw.Vector(val = [60, 100, 19.9])],
        ["size", pybzw.Vector(val = [AR, AR, 5])],
        ["title", "\"The Bridge\""],
        ["name", "\"bridge\""],
        ["unlock", "\"waterfall\""],
        ])
bzw.add_object(["group", "armorypoint"], [
        ["shift", pybzw.Vector(val = [60, 100, 20.1])],
        ])

bzw.add_object("armorypoint", [ # fourth armorypoint; Waterfall
        ["pos", pybzw.Vector(val = [30, 45, 0])],
        ["size", pybzw.Vector(val = [3, 5, 35])],
        ["title", "\"The Waterfall\""],
        ["name", "\"waterfall\""],
        ["unlock", "\"armory\""],
        ])

bzw.add_object("armorypoint", [ # fifth armorypoint; Armory
        ["pos", pybzw.Vector(val = [6.5, -125, 21.9])],
        ["size", pybzw.Vector(val = [AR, AR, 5])],
        ["title", "\"The Armory\""],
        ["name", "\"armory\""],
        ])
bzw.add_object(["group", "armorypoint"], [
        ["shift", pybzw.Vector(val = [6.5, -125, 22.1])],
        ])

# save to the .bzw
bzw.save()
