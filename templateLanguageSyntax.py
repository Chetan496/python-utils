"""
This is a validator for Free marker like templating lanaguage.
Free marker allows arbitrary variablenames which can have nested properties
example names: myVar, myObject.property, myObject.property.subproperty and so on..
A freemarker placeholder is just preceded by enclosing some delimiter , followed by closing delimiter
example: ${myVar}, ${myObject.property}, ${myObject.property.subproperty}.  A property can be very deeply nested

Below code is an attempt to create a grammar for this and validate if given placeholder is valid
Each variable name inside placeholder has to be valid variable name
eg: ${Cost450.sales} is valid, but ${6Cost450.sales} is not valid and neither is ${Cost450.3sales}

A grammar for this syntax would be:
PLACEHOLDER -> DOLLAR OPEN_BRACE PROPERTY CLOSE_BRACE
PROPERTY -> VAR_NAME (NESTED_PROPERTY)*
NESTED_PROPERTY -> DOT VAR_NAME
DOLLAR -> $
OPEN_BRACE -> {
CLOSE_BRACE -> }
DOT -> .
VAR_NAME -> ALPHABET (REST)*
REST -> ALPHABET|DIGIT|UNDERSCORE
UNDERSCORE -> _
"""
import sys


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Type: %s, Value: %s " % (self.type, self.value)

def main():
    if len(sys.argv) < 2:
        raise ValueError('please pass the template placeholder to validate')

    placeholderToValidate = sys.argv[1]  
    print("placeholder to be validated: %s " % placeholderToValidate)   