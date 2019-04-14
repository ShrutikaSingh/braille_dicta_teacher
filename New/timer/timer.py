import threading

def bang():
    threading.Timer(5.0, bang).start()
    print("Boom")

def main():
    bang()
    return 0

if __name__ == '__main__':
	main()
