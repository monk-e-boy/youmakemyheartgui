import builtins

_original_print = builtins.print


def start_print_capture(write):
    """Send a copy of everything print()ed to write(text)."""
    def intercepted_print(*args, **kwargs):
        write(' '.join(str(arg) for arg in args))
        _original_print(*args, **kwargs)
    builtins.print = intercepted_print


def stop_print_capture():
    builtins.print = _original_print