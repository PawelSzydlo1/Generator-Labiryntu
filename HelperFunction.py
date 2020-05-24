
def check_coordinate_line(canvas, x, y, a, b, a1, b1):
    """
    Sprawdzenie czy w danym miejscu znajduje się obiekt
    """
    if canvas.find_overlapping(x + a, y + b, x + a1, y + b1) == ():
        return True
    else:
        return False

