#mandelbrot.py
#creates a mandelbrot for the given coordinates
import numpy as np
from matplotlib import pyplot

def mand(iters, tl, br, xpx, ypx=None):
    ypx = ypx or xpx
    c=np.add(*np.ogrid[tl[0]*1j:br[0]*1j:xpx*1j,
                       tl[1]   :br[1]   :ypx*1j])
    m=c.copy()
    ret=np.ones(c.shape, dtype=np.int32)
    for it in xrange(iters):
        m *= m
        m += c
        ret += np.real(m*m.conjugate()) < 4
    #want inf. iterations to be a single color, not based on # of iterations
    ret += -(iters+1)*(np.abs(m) < 2)
    return ret

def mand2(iters, tl, br, xpx, ypx=None):
    ypx = ypx or xpx
    im, re = np.mgrid[tl[0]: br[0]: xpx*1j,
                      tl[1]: br[1]: ypx*1j]
    ore, oim = re.copy(), im.copy()
    ret=np.ones(ore.shape, dtype=np.int32)
    for it in xrange(iters):
        r2 = re**2
        i2 = im**2
        re, im = ore + r2 - i2, oim + 2 * re * im 
        ret += (r2 + i2) < 4  # faster for me than ret[(r2 + i2)< 4] += 1
    #want inf. iterations to be a single color, not based on # of iterations
    ret[(r2 + i2) < 4] = 0
    return ret


def mand_and_write(file, iters, tl, br, xpx, ypx=None):
    m=mand2(iters, tl, br, xpx, ypx)
    pyplot.imsave(file, m, cmap='spectral', vmin=0, vmax=255)
    
if __name__=="__main__":
    m=mand2(16, (-2, -2), (2, 2), 256)
    pyplot.imshow(m, cmap='spectral')	
    pyplot.show() 

