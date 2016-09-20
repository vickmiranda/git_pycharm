
# This is a comment on line 2

def my_function():
    print ('Ending function\n')

class MyClass(object):
    def __init__(self):
        print ('init myclass')

    def run(self):
        print('run \n')

    def cleanup(self):
        print ('my cleanup\n')


if __name__ == '__main__':
    my_c = MyClass()
    my_c.run()



