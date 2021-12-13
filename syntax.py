Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello")
Hello
>>> print("Bharat")
Bharat
>>> print "hi"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hi")?
>>> name="bharat"
>>> print name
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(name)?
>>> print(name)
bharat
>>> import calendar

cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal
SyntaxError: multiple statements found while compiling a single statement
>>> import calendar
>>> cal = calendar.month(2008, 1)
>>> print "Here is the calendar:"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Here is the calendar:")?
>>> print(cal)
    January 2008
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

>>> str = raw_input("Enter your name:")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    str = raw_input("Enter your name:")
NameError: name 'raw_input' is not defined
>>> conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="12345678")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    conn = psycopg2.connect(
NameError: name 'psycopg2' is not defined
>>> 