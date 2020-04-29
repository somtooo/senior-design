from socketengine import host
import time

h = host()
h.start()
validate = True
while validate:
	data = h.get_ALL("test")
	if data is not None:
		for item in data:
			print(item)
			validate = False
			time.sleep(10)
			h.write_ALL("test", ["Completed, 3 students attended out of 3. Thanks for using me"])
			break

h.close()