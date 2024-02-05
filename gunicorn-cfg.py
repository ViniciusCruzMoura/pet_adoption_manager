#from multiprocessing import cpu_count

bind = '0.0.0.0:8000'
workers = 1 #2 * cpu_count() + 1
accesslog = '-'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True