class Site():
    def __init__(self, url: str, pattern: str = None) -> None:
        self.url = url
        self.pattern = pattern

    def __str__(self) -> str:
        return self.url

    def __repr__(self) -> str:
        return self.url