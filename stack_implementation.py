class Stack_Implementation:
	def __init_(self,stack_old):
		self.stack_old=stack_old
		
	def push_fun(self,value):
		self.stack_old=[10,20,30,40]
		print("The stack before pushing new element is: ",self.stack_old)
		self.stack_old.append(value)
		print("The stack after pushing new element is: ",self.stack_old)

	def pop_fun(self):
		#print("The stack before poping new element is: ",self.stack_old)
		#if(len(self.stack_old) <= 0):
		#	print("The stack is empty. The stack function does not work")
		#else:
		try:
			
			print("The stack after poping last element is: ",self.stack_old.pop())
		except:
			print("sorry there is an error")
	def peek_fun(self):
		#n=len(self.stack_old)
		print(self.stack_old[1])
		
			
	
stack_obj=Stack_Implementation()

stack_obj.push_fun(50)
stack_obj.push_fun(60)
stack_obj.pop_fun()
stack_obj.peek_fun()