# -*- coding: utf-8 -*-
# Copyright (c) 2019 - 2020 Geode-solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os 

import opengeode_py_basic
import opengeode_py_geometry as geom
import opengeode_py_mesh as mesh
import opengeode_py_model as model
import opengeode_io_py_model as model_io

def test_brep(brep):
    # Number of components
    if brep.nb_corners() != 8:
        raise ValueError("[Test] Number of corners is not correct" )
    if brep.nb_lines() != 12:
        raise ValueError("[Test] Number of lines is not correct" )
    if brep.nb_surfaces() != 6:
        raise ValueError("[Test] Number of surfaces is not correct" )
    if brep.nb_blocks() != 1:
        raise ValueError("[Test] Number of blocks is not correct" )

    # Number of vertices and elements in components
    for c in brep.corners():
        if c.mesh().nb_vertices() != 1:
            raise ValueError("[Test] Number of vertices in corners should be 1" )
    for l in brep.lines():
        if l.mesh().nb_vertices() != 5:
            raise ValueError("[Test] Number of vertices in lines should be 5" )
        if l.mesh().nb_edges() != 4:
            raise ValueError("[Test] Number of edges in lines should be 4" )
    for s in brep.surfaces():
        if s.mesh().nb_vertices() != 29:
            raise ValueError("[Test] Number of vertices in surfaces should be 29" )
        if s.mesh().nb_polygons() != 40:
            raise ValueError("[Test] Number of polygons in surfaces should be 40" )
    for b in brep.blocks():
        if b.mesh().nb_vertices() != 131:
            raise ValueError("[Test] Number of vertices in blocks should be 131" )
        if b.mesh().nb_polyhedra() != 364:
            raise ValueError("[Test] Number of polyhedra in blocks should be 364" )

    # Number of component boundaries and incidences
    for c in brep.corners():
        if brep.nb_boundaries( c.id() ) != 0:
            raise ValueError("[Test] Number of corner boundary should be 0" )
        if brep.nb_incidences( c.id() ) != 3:
            raise ValueError("[Test] Number of corner incidences should be 3" )
    for l in brep.lines():
        if brep.nb_boundaries( l.id() ) != 2:
            raise ValueError("[Test] Number of line boundary should be 2" )
        if brep.nb_incidences( l.id() ) != 2:
            raise ValueError("[Test] Number of line incidences should be 2" )
    for s in brep.surfaces():
        if brep.nb_boundaries( s.id() ) != 4:
            raise ValueError("[Test] Number of surface boundary should be 4" )
        if brep.nb_incidences( s.id() ) != 1:
            raise ValueError("[Test] Number of surface incidences should be 1" )
    for b in brep.blocks():
        if brep.nb_boundaries( b.id() ) != 6:
            raise ValueError("[Test] Number of block boundary should be 6" )
        if brep.nb_incidences( b.id() ) != 0:
            raise ValueError("[Test] Number of block incidences should be 0" )

if __name__ == '__main__':
    model_io.initialize_model_io()
    test_dir = os.path.dirname(__file__)
    data_dir = os.path.abspath(os.path.join(test_dir, "../../../../tests/data"))

    brep = model.BRep()
    model.load_brep(brep, os.path.join(data_dir, "cube_v22.msh" ))
    test_brep(brep)

    model.save_brep( brep, "cube_v22.og_brep")
    reloaded_brep = model.BRep()
    model.load_brep(reloaded_brep, "cube_v22.og_brep")
    test_brep(reloaded_brep)