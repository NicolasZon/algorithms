"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

"""

# Time O(n)
def reverseInParentheses(inputString):
    openParentheses = []

    for i in range(len(inputString)):
        if inputString[i] == '(':
            openParentheses.append(i + 1)
        elif inputString[i] == ')':
            op = openParentheses.pop()
            inputString = inputString[:op] + inputString[op:i][::-1] + inputString[i:]

    inputString = inputString.replace("(", "")
    return inputString.replace(")", "")

print(reverseInParentheses("((cancion) (test)) animal"))