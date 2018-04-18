# from multiprocessing import Process
# import time
# contador = 0
# running = True

# def slow_worker():
# 	while running:
# 		print("rodando = ", contador)

# def control():
# 	while contador < 50:
# 		contador += 1
# 		print("<<<<<<<<")
# 	running = False

# if __name__ == '__main__':
# 	p = Process(target=slow_worker)
# 	p2 = Process(target=control)
# 	p.start()
# 	p2.start()
# 	p.join()
# 	p2.join()

# 	# p.terminate()
# 	# p.join()

# import multiprocessing
# import time
# from random import randint

# PROCESSES = 5
# WORKER_CALLS = 7

# def worker(num):
#     """worker function"""
#     print('Starting worker', num)
#     time.sleep(randint(2,4))
#     print('Exiting worker', num)
#     return "ok"

# if __name__ == '__main__':
#     pool = multiprocessing.Pool(processes=PROCESSES)
#     pool_outputs = pool.map(worker, range(WORKER_CALLS))
#     pool.close()
#     pool.join()
# print('Pool:', pool_outputs)

from multiprocessing import Process, Value
def func1(controler):
  print('func1: starting')
  for i in range(10000000): pass
  controler.value = 0
  print('func1: finishing')

def func2(controler):
  print('func2: starting')
  while controler.value == 1:
      pass
  print('func2: finishing')

if __name__ == '__main__':
  n = Value('i', 1)
  p1 = Process(target=func1, args=(n,))
  p1.start()
  p2 = Process(target=func2, args=(n,))
  p2.start()
  p1.join()
  p2.join()

  print('aqui')

#   def runInParallel(*fns):
#   proc = []
#   for fn in fns:
#     p = Process(target=fn)
#     p.start()
#     proc.append(p)
#   for p in proc:
#     p.join()

# runInParallel(func1, func2)