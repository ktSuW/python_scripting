
def decor_wish(func):
    def inner(name):
        names = ["Sakura", "Sally", "Tanaka"]
        if name in names:
            print("#" *  20)
            print(f"{name}, Ohaiyo gosaimasu!")
            print("#" *  20)
        else:
            func(name)
    return inner 

@decor_wish
def wish(name):
    print(f"Good morning {name}")

wish("Sakura")
wish("Sally")
wish("Lai")
