class BrowserHistory:
    def __init__(self, homepage: str):
        self.main = []
        self.support = []
        self.main.append(homepage)

    def visit(self, url: str) -> None:
        self.main.append(url)
        self.support.clear()

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.main) > 1:
            self.support.append(self.main.pop())
            steps -= 1
        return self.main[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.support:
            self.main.append(self.support.pop())
            steps -= 1
        return self.main[-1]
