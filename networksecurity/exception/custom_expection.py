import sys


def get_error_message(error_message,error_details):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    error_message=f'Error occured at line number [{line_number}] of file [{file_name}. Error says: [{error_message}]]'
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=get_error_message(error_message,error_details)

    def __str__(self):
        return self.error_message