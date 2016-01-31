import sys

print(sys.argv)
# проверка на вх данныхе в терминале
if len(sys.argv) < 3:
	print('2 argv are needed')
	exit()

if __name__ == '__main__':
	print(sys.argv[1] + ' : ' + sys.argv[2])