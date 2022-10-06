import matplotlib.pyplot as plt
import matplotlib.image as mpimg # image module for image reading

# Imread and Imshow
img = mpimg.imread("subplot_figure.png") # give addres of image location
print(img)

print("Data type of img > ", type(img))
print("Shape of img > ", img.shape)
print("Dimention of img > ",img.ndim)


plt.imshow(img)
plt.show()

plt.figure(figsize=(16,9))
plt.axis("off")
plt.imshow(img)
plt.show()

plt.figure(figsize=(16,9))
plt.axis("off")
plt.imshow(img)
plt.colorbar() # Show color bar of above image
plt.show()

single_channel = img[:,:,1] # get single channel data from img
plt.figure(figsize=(16,9))
plt.axis("off")
plt.imshow(single_channel, cmap = "hot") # show image with hot color map
plt.colorbar()
plt.show()

img2 = mpimg.imread("subplot_figure.png")
plt.figure(figsize=(16,9))
plt.axis("off")
plt.imshow(img2)
plt.colorbar()
plt.show()

single_channel2_img = img2[:,:,1]
plt.figure(figsize=(16,9))
plt.axis("off")
plt.imshow(single_channel2_img, cmap="hot")
plt.colorbar()
plt.savefig("model_hot.png")
plt.show()

cmap = """Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis, viridis_r, winter, winter_r"""
 
cmap_name_list = cmap.split(sep = ", ")

save_image_addr_name = []
for i in range(len(cmap_name_list)):
    cmap_str = cmap_name_list[i]
    save_image_addr_name.append("D:\\\cmap_image\\\_"+"girl_" + cmap_name_list[i] + ".png")
    print(save_image_addr_name[i])

for i in range(len(cmap_name_list)): 
    cmap_name = cmap_name_list[i]
    plt.figure(figsize=(16,9))
    plt.axis("off")
     
    print(cmap_name)
 
    plt.imshow(single_channel2_img, cmap=cmap_name)
    #plt.colorbar()
    #save_image_name1 = "D:\\cmap_image\\"+"girl" + cmap_list[i]
    print(save_image_addr_name[i])
    plt.savefig(save_image_addr_name[i], orientation='portrate', facecolor= "k")
    plt.show()