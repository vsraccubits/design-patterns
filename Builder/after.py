from abc import ABC, abstractmethod


class WebPage:
    """A Web Page."""
    def __init__(self, builder):
        self.page = builder.page
        self.header = builder.header
        self.body = builder.body
        self.footer = builder.footer

    def show(self):
        """Show Web Page."""
        print("Web Page Created")
        print(self.page)
        print(self.header)
        print(self.body)
        print(self.footer)


class Content:
    """A Content."""
    def __init__(self, builder):
        self.page = builder.page
        self.header = builder.header
        self.body = builder.body
        self.footer = builder.footer

    def show(self):
        """Show Content."""
        print("Content Created")
        print(self.page)
        print(self.header)
        print(self.body)
        print(self.footer)


class Builder(ABC):
    """A Builder."""
    def __init__(self):
        self.page = None
        self.header = None
        self.body = None
        self.footer = None

    @abstractmethod
    def set_page(self):
        """Set Page."""

    @abstractmethod
    def set_header(self):
        """Set Header."""

    @abstractmethod
    def set_body(self):
        """Set Body."""

    @abstractmethod
    def set_footer(self):
        """Set Footer"""

    def build(self):
        """Build."""


class HomePageBuilder(Builder):
    """A Home Page Builder."""
    def set_page(self):
        """Set Page."""
        self.page = "Home Page"

    def set_header(self):
        """Set Header."""
        self.header = "Home Page Header"

    def set_body(self):
        """Set Body."""
        self.body = "Home Page Body"

    def set_footer(self):
        """Set Footer."""
        self.footer = "Home Page Footer"

    def build(self):
        """Build."""
        return WebPage(self)


class HomePageContentBuilder(Builder):
    """A Home Page Content Builder."""
    def set_page(self):
        """Set Page."""
        self.page = "Home Page"

    def set_header(self):
        """Set Header."""
        self.header = "Home Page Header Content"

    def set_body(self):
        """Set Body."""
        self.body = "Home Page Body Content"

    def set_footer(self):
        """Set Footer."""
        self.footer = "Home Page Footer Content"

    def build(self):
        """Build."""
        return Content(self)


class WebPageDirector:
    """A Web Page Director."""
    def __init__(self, builder):
        self.builder = builder

    def build_home_page(self):
        """Build Home Page."""
        self.builder.set_page()
        self.builder.set_header()
        self.builder.set_body()
        self.builder.set_footer()
        return self.builder.build()


def main():
    user_input = input("Enter desired web page with content (home page): ")

    if user_input not in ["home page"]:
        print("Selected Web Page Not Available")
        return

    if user_input == "home page":
        home_page_builder = HomePageBuilder()
        director = WebPageDirector(home_page_builder)
        home_page = director.build_home_page()
        home_page.show()

        home_page_content_builder = HomePageContentBuilder()
        director = WebPageDirector(home_page_content_builder)
        home_page_content = director.build_home_page()
        home_page_content.show()


if __name__ == "__main__":
    main()
