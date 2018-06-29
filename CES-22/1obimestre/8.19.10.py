import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
	test(is_palindrome("abba"))
	test(not is_palindrome("abab"))
	test(is_palindrome("tenet"))
	test(not is_palindrome("banana"))
	test(is_palindrome("straw warts"))
	test(is_palindrome("a"))

def reverse(word):
	return word[::-1]

def is_palindrome(word):
	return word == reverse(word)
test_suite()   
