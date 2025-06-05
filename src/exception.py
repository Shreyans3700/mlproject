import sys


def error_message_details(error, error_detail: sys):
    """
    it provides us error details
    First two params are not important
    3rd one gives us details about error
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_numner = exc_tb.tb_lineno
    err = str(error)

    error_msg = f"Error message occoured in python script {file_name} line number {line_numner}, error message {err}"

    return error_msg


class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_messgae = error_message_details(
            error=error_message, error_detail=error_details
        )

    def __str__(self):
        return self.error_messgae
