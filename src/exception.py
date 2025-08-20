import sys
from logger import logging
def raise_error_message(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    message="Error occured in python script [{0}] at line [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return message

class customexception(Exception):
    def __init__(self, error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=raise_error_message(error_message,error_details=error_details)
    def __str__(self):
        return self.error_message

try:
    q=1/0
except Exception as yy:
    logging.info("divide by 0")
    raise customexception(yy,sys)




