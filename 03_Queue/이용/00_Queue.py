import queue


q = queue.Queue()


q.put(10)
q.put(20)
q.put(30)
q.put(40)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print("=================")
q.put(10)
print(q.get())
