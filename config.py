import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Shapenet config
SHAPENET_VOX = {
    32: os.path.join(BASE_DIR, 'data/shapenet_release/voxels/modelVoxels32'),
    64: os.path.join(BASE_DIR, 'data/shapenet_release/voxels/modelVoxels64')
}

SHAPENET_IM = os.path.join(BASE_DIR, 'data/shapenet_release/renders')
CUSTOM_SHAPENET_IM = os.path.join(BASE_DIR, 'data/rendered_images')
CUSTOM_SPLIT_JSON = os.path.join(BASE_DIR, 'data/custom_split.json')

