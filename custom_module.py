class Test:
    def __init__(self, test: str) -> None:
        print('hello -----------------')
        self.test = test

    def __format__(self, format_spec: str) -> str:
        if format_spec == 'len':
            return str(len(self.test))
        elif format_spec == 'upper':
            return self.test.upper()
