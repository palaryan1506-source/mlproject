import sys 
import logging

def error_message_detail(error,error_detail:sys):  ## means: this error detail will be present inside this sys
    _,_,exc_tb=error_detail.exc_info()  ## means for first 2 info we are not interested , 3rd is gonna recorded
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message
     ## REMEMBER!! :- This is not gonna change everytime



class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message =error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message










### this can be used everywhere,something else also was said by sir.