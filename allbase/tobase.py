def do(n, bases):
    in_base_format = [b.to_str(n) for b in bases]
    return " ".join(in_base_format)