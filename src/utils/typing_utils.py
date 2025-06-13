from typing import get_args,Literal,Union

def get_args_recursive(t) -> list:
    """
    Parses the type annotations and returns all values as a flattened list
    """
    args = get_args(t)
    flat_args = []

    for arg in args:
        if getattr(arg, '__origin__', None) is Literal:
            flat_args.extend(get_args(arg))
        elif getattr(arg, '__origin__', None) is Union:
            flat_args.extend(get_args_recursive(arg))  # Recursive call
        else:
            flat_args.append(arg)

    return flat_args








