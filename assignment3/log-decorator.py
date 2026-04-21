#Task 1
import logging
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__ + "_parameter_log")
        logger.setLevel(logging.INFO)
        
        #ecrepeats 3 times w/o check
        if not logger.handlers:
            logger.addHandler(logging.FileHandler("./decorator.log","a"))

        # To write a log record:
        logger.log(logging.INFO, "this string would be logged")
        a_list = ()
        a_dict = {}
        
        if not args:
            a_list = "none"
        else:
            a_list = list(args)
            
        if not kwargs:
            a_dict ="none"
        else:
            a_dict = dict(kwargs)
            
        result = func(*args, **kwargs)

        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args}")
        logger.info(f"keyword parameters: {kwargs}")
        logger.info(f"return: {result} \n")
        return result
    return wrapper

@logger_decorator
def say_hey():
    print("Hello, World!")

say_hey()

@logger_decorator
def pos_args(*args):
    len(args)
    return True

pos_args(3,4,5)

@logger_decorator
def key_args(**kwargs):
    len(kwargs)
    return logger_decorator

key_args(a=1, b=2)