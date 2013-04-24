#mandelbrot.py
#creates a mandelbrot for the given coordinates
import numpy as np

def mand(iters, tl, br, xpx, ypx=None):
    ypx = ypx or xpx
    c=np.add(*np.ogrid[tl[0]*1j:br[0]*1j:xpx*1j,
                       tl[1]   :br[1]   :ypx*1j])
    m=c.copy()
    ret=np.ones(c.shape, dtype=np.int32)
    for it in xrange(iters):
        m *= m
        m += c
        ret += np.abs(m) < 2
    #want inf. iterations to be a single color, not based on # of iterations
    ret += -(iters+1)*(np.abs(m) < 2)
    return ret

def mand_and_write(file, iters, tl, br, xpx, ypx=None):
    from matplotlib import pyplot
    m=mand(iters, tl, br, xpx, ypx)
    pyplot.imsave(file, m, cmap='spectral', vmin=0, vmax=255)
    
if __name__=="__main__":
    from matplotlib import pyplot
    m=mand(16, (-2, -2), (2, 2), 256)
    pyplot.imshow(m, cmap='spectral')	
    pyplot.show() 

