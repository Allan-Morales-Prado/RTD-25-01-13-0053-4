def standard_arg(arg):
    print(arg)  # Puede llamarse por posición o con nombre

def pos_only_arg(arg, /):
    print(arg)  # Solo por posición

def kwd_only_arg(*, arg):
    print(arg)  # Solo con nombre

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)