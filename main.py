from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    line = Line(Point(1, 6), Point(7, 122))
    win.draw_line(line, "blue")
    win.wait_for_close()

main()