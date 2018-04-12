import matplotlib

# remember to scale back up!!!
scale_by = 5


for i in range(pred_depth[0].shape[0]):
    depth_im = pred_depth[0,i,:,:,0]
    depth_im = np.stack((depth_im[:,:],)*4, -1)/scale_by
    depth_im[:,:,3] = mask[0,i,:,:,0].astype('uint8')
    print(depth_im.shape)
    matplotlib.image.imsave('./depth_maps/'+str(i)+'.png', depth_im)
