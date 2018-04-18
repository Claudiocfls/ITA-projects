# [TODO]
import threading
import time
import random
lista = 0
class producer(object):
	lock = threading.RLock()
	def __init__(self):
		pass
	def run(self):
		producer.lock.acquire()
		for i in range(10):
			lista += 1
			print('Producer notify: item')
			time.sleep(1)
		producer.lock.release()

class consumer(object):
	lock = threading.RLock()
	def __init__(self):
		pass
	def run(self):
		consumer.lock.acquire()
		while True:
			item -= 1
			print('consumer notify')
			if item < 2:
				break
		consumer.lock.release()

if __name__ == '__main__':
	t1 = threading.Thread(target=producer, args=())
	t2 = threading.Thread(target=consumer, args=())
	t3 = threading.Thread(target=consumer, args=())
	t4 = threading.Thread(target=consumer, args=())
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()