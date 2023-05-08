class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass


if __name__ == "__main__:"
    obj = Sub()
    
    # Python looks for object components (properties and methods)
    # in the following order:
    # - inside the object itself;
    # - in its superclasses, from bottom to top
    # - if there is more than one class on a particulr inheritance
    #   path, Python scans them from left to right
    print(obj.var, obj.var_left, obj.var_right, obj.fun()) # L LL RR Left
