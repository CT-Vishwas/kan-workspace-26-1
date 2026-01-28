import datetime

# start_time = datetime.datetime.now()
# slow_func()
# end_time = datetime.datetime.now()
# duration = end_time - start_time

def func_timer(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args,**kwargs)
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        print(f"The function ran for {duration}s")
        return result
    return wrapper

@func_timer
def slow_func():
    for i in range(10,000):
        print(i,end='')

if __name__ == '__main__':
    slow_func()