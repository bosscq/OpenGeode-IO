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
import opengeode_io_py_mesh as mesh_io

if __name__ == '__main__':
    mesh_io.initialize_mesh_io()
    test_dir = os.path.dirname(__file__)
    data_dir = os.path.abspath(os.path.join(test_dir, "../../../../tests/data"))
    
    surface = mesh.PolygonalSurface3D.create()
    mesh.load_polygonal_surface3D(surface, os.path.join(data_dir, "TopHat.obj"))
    if surface.nb_vertices() != 363:
        raise ValueError("[Test] Number of vertices in the loaded Surface is not correct" )
    if surface.nb_polygons() != 380:
        raise ValueError("[Test] Number of polygons in the loaded Surface is not correct" )

    mesh.save_polygonal_surface3D(surface, "TopHat_save.obj")
