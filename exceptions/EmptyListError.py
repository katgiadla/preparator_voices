class EmptyListError(Exception):
    def __init__(self, *args: object) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        if self.message:
            return 'Empty list error'
        else:
            return 'Empty list error has been raised'