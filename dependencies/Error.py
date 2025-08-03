class CompilationError(Exception):
    """ 编译过程中出现错误 """
    def __init__(self, message="编译过程中出现错误"):
        self.message = message
        super().__init__(self.message)

class EnvironmentError(Exception):
    """ OleanderJS环境配置错误 """
    def __init__(self, message="OleanderJS环境配置错误"):
        self.message = message
        super().__init__(self.message)

class IllegalAccessError(Exception):
    """ 非法访问错误 """
    def __init__(self, message="非法访问错误"):
        self.message = message
        super().__init__(self.message)
