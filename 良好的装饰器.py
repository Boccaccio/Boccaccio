def log(*str):
    def decorator(func):
        def wrapper(*args, **kw):
            text =''.join(str)
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
import functools
def logger(text):
    def inter(func):        
        @functools.wraps(func)
        def warpper(*args, **kw):
            print('begin call: log%s(%s)' % ('' if callable(text) else "('%s')" % text, func.__name__))
            result = func(*args, **kw)
            print('end call: result is %s' % result)
            return result
        return warpper
    return inter(text) if callable(text) else inter    
