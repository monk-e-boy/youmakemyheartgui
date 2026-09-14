import builtins
#
# UGH - this code is jank
#
from .__init__ import win

# Store the original print function
_original_print = builtins.print

# List to store captured print calls
captured_prints = []

def intercepted_print(*args, **kwargs):
    """
    Intercept print calls, capture them, then call original print
    """
    # Capture the print call (convert args to strings like print does)
    captured_output = ' '.join(str(arg) for arg in args)
    #captured_prints.append(captured_output)

    #
    # global variable win (see imports)
    #
    win.terminal_append(captured_output)
    
    # Call the original print function normally
    _original_print(*args, **kwargs)

def start_print_capture():
    """Start intercepting print calls"""
    builtins.print = intercepted_print

def stop_print_capture():
    """Stop intercepting print calls"""
    builtins.print = _original_print


# Automatically start capturing when module is imported
start_print_capture()