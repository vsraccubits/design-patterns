from abc import ABC, abstractmethod


class WebPage:
    """A Web Page."""
    def __init__(self) -> None:
        self.page = None
        self.header = None
        self.body = None
        self.footer = None

    def show(self) -> None:
        """Show Web Page."""
        print("Web Page Created")
        print(self.page)
        print(self.header)
        print(self.body)
        print(self.footer)


class Content:
    """A Content."""
    def __init__(self) -> None:
        self.page = None
        self.header = None
        self.body = None
        self.footer = None

    def show(self) -> None:
        """Show Web Page."""
        print("Web Page Content Created")
        print(self.page)
        print(self.header)
        print(self.body)
        print(self.footer)


class Builder(ABC):
    """A Builder."""
    @property
    @abstractmethod
    def product(self) -> None:
        """Product."""
        pass

    @abstractmethod
    def set_page(self) -> None:
        """Set Page."""
        pass

    @abstractmethod
    def set_header(self) -> None:
        """Set Header."""
        pass

    @abstractmethod
    def set_body(self) -> None:
        """Set Body."""
        pass

    @abstractmethod
    def set_footer(self) -> None:
        """Set Footer"""
        pass


class HomePageBuilder(Builder):
    """A Home Page Builder."""
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        """Reset."""
        self._product = WebPage()

    @property
    def product(self) -> WebPage:
        """Product."""
        product = self._product
        self.reset()
        return product

    def set_page(self) -> None:
        """Set Page."""
        self._product.page = "Home Page"

    def set_header(self) -> None:
        """Set Header."""
        self._product.header = "Home Page Header"

    def set_body(self) -> None:
        """Set Body."""
        self._product.body = "Home Page Body"

    def set_footer(self) -> None:
        """Set Footer."""
        self._product.footer = "Home Page Footer"


class HomePageContentBuilder(Builder):
    """A Home Page Content Builder."""
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        """Reset."""
        self._product = Content()

    @property
    def product(self) -> Content:
        """Product."""
        product = self._product
        self.reset()
        return product

    def set_page(self) -> None:
        """Set Page."""
        self._product.page = "Home Page Content"

    def set_header(self) -> None:
        """Set Header."""
        self._product.header = "Home Page Header Content"

    def set_body(self) -> None:
        """Set Body."""
        self._product.body = "Home Page Body Content"

    def set_footer(self) -> None:
        """Set Footer."""
        self._product.footer = "Home Page Footer Content"


class Director:
    """A Web Page Director."""
    def __init__(self):
        self.builder = None

    @property
    def builder(self) -> Builder:
        """Builder."""
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """Set Builder."""
        self._builder = builder

    def build_home_page(self):
        """Build Home Page."""
        self._builder.set_page()
        self._builder.set_header()
        self._builder.set_body()
        self._builder.set_footer()

    def build_home_page_content(self):
        """Build Home Page Content."""
        self._builder.set_page()
        self._builder.set_header()
        self._builder.set_body()
        self._builder.set_footer()


def main():
    user_input = input("Enter desired web page with content (home page): ")

    if user_input not in ["home page"]:
        print("Selected Web Page Not Available")
        return

    if user_input == "home page":
        director = Director()
        builder = HomePageBuilder()
        director.builder = builder
        director.build_home_page()
        builder.product.show()

        builder = HomePageContentBuilder()
        director.builder = builder
        director.build_home_page_content()
        builder.product.show()


if __name__ == "__main__":
    main()
