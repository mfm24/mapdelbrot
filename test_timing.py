# -*- coding: utf-8 -*-
"""
Times how long 100 requests to localhost take!
"""

import timeit
import urllib

def test_url(times = [-2.001+0.01*x for x in range(100)]):
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
Python caches the png, whereas go caches the raw data and has to
compress each time.

Still not sure what takes so long with the Python code. cProfile says
select.select takes all the time, but I think that could be waiting for 
the multithreaded Python calls to finish? Might be interesting to know
if it's the png writing or the mandelbrot calculations that take so long

"""