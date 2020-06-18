'''
Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If method gets number, it should return string.

Examples:

# returns test_controller
to_underscore('TestController')

# returns movies_and_books
to_underscore('MoviesAndBooks')

# returns app7_test
to_underscore('App7Test')

# returns "1"
to_underscore(1)

'''

def to_underscore(string):
    if isinstance(string, str):
        l=string[0].lower()
        for s in string[1:]:
            if s.isupper():
                l=l+'_'+s.lower()
            else:
                l=l+s
        print(l)
    else:
        print(str(string))


to_underscore('TestController')
to_underscore('MoviesAndBooks')
to_underscore('App7Test')   
to_underscore(1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
