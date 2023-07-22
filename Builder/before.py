class HomePage:
    """A Web Page."""
    def __init__(self):
        self.page = "Home Page"
        self.header = "Home Page Header"
        self.body = "Home Page Body"
        self.footer = "Home Page Footer"

    def show(self):
        """Show Web Page."""
        print("Web Page Created")
        print(self.page)
        print(self.header)
        print(self.body)
        print(self.footer)


class Content:
    """A Content."""
    def __init__(self):
        self.page = "Home Page"
        self.header = "Home Page Header Content"
        self.body = "Home Page Body Content"
        self.footer = "Home Page Footer Content"

    def show(self):
        """Show Content."""
        print("Content Created")
        print(self.page)
        print(self.header)
        print(self.body)
        print(self.footer)


def main():
    user_input = input("Enter desired web page with content (home page): ")

    if user_input not in ["home page"]:
        print("Selected Web Page Not Available")
        return

    if user_input == "home page":
        home_page = HomePage()
        home_page.show()
        home_content = Content()
        home_content.show()


if __name__ == "__main__":
    main()
