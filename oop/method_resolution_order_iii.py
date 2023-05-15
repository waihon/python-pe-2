class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Top, Middle):
    def m_bottom(self):
        print("bottom")


if __name__ == "__main__":
    object = Bottom()
    object.m_bottom()
    object.m_middle()
    object.m_top()

    """
    TypeError: Cannot create a consistent method resolution
    order (MRO) for bases Top, Middle
    """
