/*
 * Copyright (c) 2019 - 2020 Geode-solutions
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 */

#pragma once

#include <fstream>

#include <assimp/Exporter.hpp>
#include <assimp/scene.h>

#include <geode/basic/logger.h>

#include <geode/geometry/point.h>

#include <geode/mesh/opengeode_io_mesh_export.h>

namespace geode
{
    namespace detail
    {
        template < typename SurfaceMesh >
        class AssimpMeshOutput
        {
        public:
            AssimpMeshOutput( absl::string_view filename,
                const SurfaceMesh& surface_mesh,
                absl::string_view assimp_export_id )
                : file_( filename ),
                  surface_mesh_( surface_mesh ),
                  export_id_( assimp_export_id )
            {
                OPENGEODE_EXCEPTION( std::ofstream( file_.data() ).good(),
                    "[AssimpMeshOutput] Error while opening file: ", file_ );
            }

            void build_assimp_scene()
            {
                initialize_scene();
                build_assimp_vertices();
                build_assimp_faces();
            }

            void write_file()
            {
                Assimp::Exporter exporter;
                const auto status = exporter.Export(
                    &assimp_scene_, export_id_.data(), file_.data() );
                OPENGEODE_EXCEPTION( status == AI_SUCCESS,
                    "[AssimpMeshOutput::write_file] Export in file \"", file_,
                    "\" has failed." );
            }

        private:
            void initialize_scene()
            {
                assimp_scene_.mRootNode = new aiNode;

                assimp_scene_.mMaterials = new aiMaterial*[1];
                assimp_scene_.mMaterials[0] = new aiMaterial;
                assimp_scene_.mNumMaterials = 1;

                assimp_scene_.mMeshes = new aiMesh*[1];
                assimp_scene_.mMeshes[0] = new aiMesh;
                assimp_scene_.mNumMeshes = 1;
                assimp_scene_.mMeshes[0]->mMaterialIndex = 0;

                assimp_scene_.mRootNode->mMeshes = new unsigned int[1];
                assimp_scene_.mRootNode->mMeshes[0] = 0;
                assimp_scene_.mRootNode->mNumMeshes = 1;
            }

            void build_assimp_vertices()
            {
                auto pMesh = assimp_scene_.mMeshes[0];
                pMesh->mVertices = new aiVector3D[surface_mesh_.nb_vertices()];
                pMesh->mNumVertices = surface_mesh_.nb_vertices();

                for( const auto p :
                    geode::Range{ surface_mesh_.nb_vertices() } )
                {
                    pMesh->mVertices[p] =
                        aiVector3D{ surface_mesh_.point( p ).value( 0 ),
                            surface_mesh_.point( p ).value( 1 ),
                            surface_mesh_.point( p ).value( 2 ) };
                }
            }

            void build_assimp_faces()
            {
                auto pMesh = assimp_scene_.mMeshes[0];
                pMesh->mFaces = new aiFace[surface_mesh_.nb_polygons()];
                pMesh->mNumFaces = surface_mesh_.nb_polygons();

                for( const auto t :
                    geode::Range{ surface_mesh_.nb_polygons() } )
                {
                    auto& face = pMesh->mFaces[t];

                    face.mIndices = new unsigned int[3];
                    face.mNumIndices = 3;
                    face.mIndices[0] = surface_mesh_.polygon_vertex( { t, 0 } );
                    face.mIndices[1] = surface_mesh_.polygon_vertex( { t, 1 } );
                    face.mIndices[2] = surface_mesh_.polygon_vertex( { t, 2 } );
                }
            }

        private:
            absl::string_view file_;
            const SurfaceMesh& surface_mesh_;
            absl::string_view export_id_;
            aiScene assimp_scene_;
        };
    } // namespace detail
} // namespace geode