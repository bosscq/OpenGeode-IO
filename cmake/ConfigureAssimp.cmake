# Copyright (c) 2019 Geode-solutions
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

set(ASSIMP_PATH ${PROJECT_BINARY_DIR}/third_party/assimp)
set(ASSIMP_INSTALL_PREFIX ${ASSIMP_PATH}/install)
ExternalProject_Add(assimp
    PREFIX ${ASSIMP_PATH}
    GIT_REPOSITORY https://github.com/Geode-solutions/assimp
    GIT_TAG 23be8a2e49e2837ab3dc5f3f9f7e4fb5e6d08cc0
    CMAKE_GENERATOR ${CMAKE_GENERATOR}
    CMAKE_GENERATOR_PLATFORM ${CMAKE_GENERATOR_PLATFORM}
    CMAKE_ARGS
        -DCMAKE_INSTALL_MESSAGE=LAZY
        -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
    CMAKE_CACHE_ARGS
        -DINJECT_DEBUG_POSTFIX:BOOL=OFF
        -DASSIMP_DOUBLE_PRECISION:BOOL=ON
        -DASSIMP_BUILD_ZLIB:BOOL=ON
        -DBUILD_SHARED_LIBS:BOOL=OFF
        -DASSIMP_BUILD_ASSIMP_TOOLS:BOOL=OFF
        -DASSIMP_BUILD_TESTS:BOOL=OFF
        -DASSIMP_BUILD_ALL_IMPORTERS_BY_DEFAULT:BOOL=FALSE
        -DASSIMP_BUILD_OBJ_IMPORTER:BOOL=TRUE
        -DASSIMP_BUILD_PLY_IMPORTER:BOOL=TRUE
        -DASSIMP_BUILD_STL_IMPORTER:BOOL=TRUE
        -DASSIMP_BUILD_ALL_EXPORTERS_BY_DEFAULT:BOOL=FALSE
        -DASSIMP_BUILD_OBJ_EXPORTER:BOOL=TRUE
        -DASSIMP_BUILD_PLY_EXPORTER:BOOL=TRUE
        -DASSIMP_BUILD_STL_EXPORTER:BOOL=TRUE
        -DCMAKE_INSTALL_PREFIX:PATH=${ASSIMP_INSTALL_PREFIX}
)