class Top:
    def m_top(self):
        print("top")

    def m_middle(self):
        print("middle_top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


if __name__ == "__main__":
    object = Bottom()
    object.m_bottom() # bottom
    object.m_middle() # middle_left
    object.m_top()    # top
