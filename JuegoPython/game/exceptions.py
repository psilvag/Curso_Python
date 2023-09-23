from constants import GAME_TYPE_ERROR_FILE_CODE,ERROR_MESSAGES

class gameBaseExceptions(Exception):
    def __init__(self, code,msg, extra) -> None:
        self.code=code
        self.msg=msg
        self.extra=extra


class gameTypeFileError(gameBaseExceptions):
    code=GAME_TYPE_ERROR_FILE_CODE

    def __init__(self):
        self.msg=ERROR_MESSAGES[self.code]
        super().__init__(self.code,self.msg)


