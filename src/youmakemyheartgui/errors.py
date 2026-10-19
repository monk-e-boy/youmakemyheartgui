import os
import traceback


def where_in_student_code(tb):
    """' (line 12 of main.py)' for the innermost frame NOT in our library."""
    library_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep
    for frame in reversed(traceback.extract_tb(tb)):
        if not os.path.abspath(frame.filename).startswith(library_dir):
            return f" (line {frame.lineno} of {os.path.basename(frame.filename)})"
    return ""


def friendly_excepthook(exc_type, exc, tb):
    print(f"❌ Error{where_in_student_code(tb)}:\n   {exc_type.__name__}: {exc}")