# -*- coding: utf-8 -*-
"""
Times how long 100 requests to localhost take!
"""

import timeit
import urllib

def test_url(times = [-2.001+0.01*x for x in range(200)]):
    for t in times:
        # using 'localhost' instaed of 127.0.0.1 takes ~1s
        # per request!
        s = "http://127.0.0.1:8080/%s/%s/%s/%s/64" % (
                        t, t, t+2.0, t+2.0)
        print "Fetching",s
        urllib.urlopen(s).read()
        
print timeit.timeit(stmt=test_url, number=1)

"""Some results:
in s, first time (cached)
go: 3.0 1.63
python: 21.9 0.7
trying again 2013-11-10 (MBP, plugged in, VM, 100images):
python: 10.2 (0.43)
go: 1.4 (0.85)

As above 200 images:
Go: 2.55 (1.55)
Python: 20.4 (0.84)
Python: mand2 13.4 (0.84)  # we don't use complex data and cache re and im squared
node.js 4.6 (0.55 - caching already pngd data)

Python caches the png, whereas go caches the raw data and has to
compress each time.

NB Python with sending blank ramps into png takes 4.5s (ie the png encoding is
slower than both go and node.js total time)

Still not sure what takes so long with the Python code. cProfile says
select.select takes all the time, but I think that could be waiting for 
the multithreaded Python calls to finish? Might be interesting to know
if it's the png writing or the mandelbrot calculations that take so long

"""