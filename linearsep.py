# Linear separability in Fourier transforms

# A simple example of linear separability in the Fourier transform. 

import numpy as np

grid_original = [[1,0,2,1],
                [2,1,2,3],
                [3,0,1,2],
                [2,1,2,3]]

subgrid_1 = [[1,0,1,1],
            [1,1,1,1],
            [1,0,1,1],
            [1,1,1,1]]

subgrid_2 = [[0,0,1,0],
            [1,0,1,1],
            [1,0,0,1],
            [1,0,1,1]]

subgrid_3 = [[0,0,0,0],
            [0,0,0,1],
            [1,0,0,0],
            [0,0,0,1]]

ft_grid_original = np.fft.fftshift(np.fft.fft2(grid_original))

ft_subgrid1 = np.fft.fftshift(np.fft.fft2(subgrid_1))

ft_subgrid2 = np.fft.fftshift(np.fft.fft2(subgrid_2))

ft_subgrid3 = np.fft.fftshift(np.fft.fft2(subgrid_3))

ft_linear_recombination = ft_subgrid1 + ft_subgrid2 + ft_subgrid3

print("Fourier transform of original grid: \n" + str(ft_grid_original))

print("Reconstructed transform from linear recombination: \n" + str(ft_linear_recombination))