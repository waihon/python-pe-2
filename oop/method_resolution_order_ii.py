class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom")


if __name__ == "__main__":
    object = Bottom()
    object.m_bottom() # bottom
    object.m_middle() # middle
    object.m_top()    # top
