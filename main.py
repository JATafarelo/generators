import sys
import cProfile

#----------------Reading a large file-------------------
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
def read_large_file():
    # csv_gen = csv_reader("some_csv.txt")
    csv_gen = (row for row in open("some_csv.txt"))
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print(f"Row count is {row_count}")
#--------------------------------------------------------

#-----------Generating an infinite sequence--------------
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def generate_sequence():
    for i in infinite_sequence():
        print(i, end=" ")

def create_sequence():
    gen = infinite_sequence()

    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

#--------------------------------------------------------

#-----------------Detecting Palindromes------------------

def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False

def detect():
    for i in infinite_sequence():
        pal = is_palindrome(i)
        if pal:
            print(i)

#--------------------------------------------------------

#-------------------Building Generators------------------
def build_generator():
    nums_squared_lc = [i * 2 for i in range(10000)]
    print(sys.getsizeof(nums_squared_lc))

    nums_squared_gc = (i ** 2 for i in range(10000))
    print(sys.getsizeof(nums_squared_gc))

#--------------------------------------------------------

#----------------------Profiling Generator---------------

def profile():
    cProfile.run('sum([i * 2 for i in range(10000)])')
    cProfile.run('sum((i * 2 for i in range(10000)))')

#--------------------------------------------------------

#---------------------Python Yield-----------------------

def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

def python_yield():

    multi_obj = multi_yield()
    print(next(multi_obj))

    print(next(multi_obj))

    print(next(multi_obj))

def for_with_generator():
    letters = ["a", "b", "c", "y"]
    it = iter(letters)
    while True:
        try:
            letter = next(it)
        except StopIteration:
            break
        print(letter)

#--------------------------------------------------------

#------------------------Advanced Methods----------------

def infinite_palindromes_methods():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

def methods_send():
    pal_gen = infinite_palindromes_methods()
    for i in pal_gen:
        digits = len(str(i))
        print(pal_gen.send(10 ** (digits)))

def methods_throw():
    pal_gen = infinite_palindromes_methods()
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        if digits == 5:
            pal_gen.throw(ValueError("We don't like large palindromes"))
        pal_gen.send(10 ** (digits))

def methods_close():
    pal_gen = infinite_palindromes_methods()
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        if digits == 5:
            pal_gen.close()
        pal_gen.send(10 ** (digits))

#--------------------------------------------------------


def main():
    methods_close()

if __name__ == '__main__':
    main()

