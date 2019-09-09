import numpy as np
from matplotlib import pyplot as plt

def plot_errors(x_test, y_test, output,n_max=600):
    """ Function the reporting in a script in order to
    breake the script if it is estimated to take to long time"""
    n_not_corr = np.sum(output != y_test )
    n = int(np.ceil(np.sqrt(n_not_corr)))
    j = 0
    if n_not_corr > n_max:
        print('more then '+str(n_max),n**2)
        return
    f, ax = plt.subplots(n, n, figsize=(25, 25))
    ax = ax.flatten()
    
    for i in range(np.shape(output)[0]):
            if output[i]!=y_test[i]:
                ax[j].set_title(str(y_test[i]) + ' as ' + str(output[i]))
                ax[j].imshow(x_test[i,:,:,0], cmap='gray')
                ax[j].axis('off')
                j+=1
    for x in ax.ravel():
        x.axis("off")
    plt.subplots_adjust(bottom=-0.09, wspace=0.03)
    plt.show()