

# fp = open('data.txt')
# data = fp.read()
# print(data)
# fp.close()

try:
    with open('data.txt','r') as fp:
        data = fp.read()
except FileNotFoundError:
    print("File not found")
except Exception:
    print("Unknown Error")
# else:
# finally: