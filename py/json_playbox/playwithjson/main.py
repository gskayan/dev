
import inspect



def main_impl():

	_n_ = inspect.currentframe().f_code.co_name

	print(f"Starting: {_n_}")
	''' Your code goes here '''
	print(f"Stopping: {_n_}")


if __name__ =="__main__":

	main_impl()

