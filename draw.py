"""
draw.py

The draw module defines functions that allow the user to create a
drawing.  A drawing appears on the canvas.  The canvas appears
in the window.  As a convenience, the module also imports the
commonly used Color objects defined in the color module.
"""

import os
import sys
import time

import pygame
import pygame.font
import pygame.gfxdraw

import color

if sys.hexversion < 0x03000000:
    import tkinter
else:
    import tkinter
    import tkinter.messagebox as tk_message_box
    import tkinter.filedialog as tk_file_dialog

# -----------------------------------------------------------------------

# Default Sizes and Values

_BORDER = 0.0
# _BORDER = 0.05
_DEFAULT_XMIN = 0.0
_DEFAULT_XMAX = 1.0
_DEFAULT_YMIN = 0.0
_DEFAULT_YMAX = 1.0
_DEFAULT_CANVAS_SIZE = 512
_DEFAULT_PEN_RADIUS = .005  # Maybe change this to 0.0 in the future.
_DEFAULT_PEN_COLOR = color.BLACK

_DEFAULT_FONT_FAMILY = 'Helvetica'
_DEFAULT_FONT_SIZE = 12

_xmin = 0.0
_ymin = 0.0
_xmax = 0.0
_ymax = 0.0

_fontFamily = _DEFAULT_FONT_FAMILY
_fontSize = _DEFAULT_FONT_SIZE

_canvasWidth = float(_DEFAULT_CANVAS_SIZE)
_canvasHeight = float(_DEFAULT_CANVAS_SIZE)
_pen_radius = 1.0
_penColor = _DEFAULT_PEN_COLOR
_keysTyped = []

# Has the window been created?
_windowCreated = False

# -----------------------------------------------------------------------
# Begin added by Alan J. Broder
# -----------------------------------------------------------------------

# Keep track of mouse status

# Has the mouse been left-clicked since the last time we checked?
_mousePressed = False

# The position of the mouse as of the most recent mouse click
_mousePos = None


# -----------------------------------------------------------------------
# End added by Alan J. Broder
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------

def _pygame_color(c):
    """
    Convert c, an object of type color.Color, to an equivalent object
    of type pygame.Color.  Return the result.
    """
    r = c.get_red()
    g = c.get_green()
    b = c.get_blue()
    return pygame.Color(r, g, b)


# -----------------------------------------------------------------------

# Private functions to scale and factor X and Y values.

def _scale_x(x):
    return _canvasWidth*(x - _xmin)/(_xmax - _xmin)


def _scale_y(y):
    return _canvasHeight*(_ymax - y)/(_ymax - _ymin)


def _factor_x(w):
    return w*_canvasWidth/abs(_xmax - _xmin)


def _factor_y(h):
    return h*_canvasHeight/abs(_ymax - _ymin)


# -----------------------------------------------------------------------
# Begin added by Alan J. Broder
# -----------------------------------------------------------------------

def _user_x(x):
    return _xmin + x*(_xmax - _xmin)/_canvasWidth


def _user_y(y):
    return _ymax - y*(_ymax - _ymin)/_canvasHeight


# -----------------------------------------------------------------------
# End added by Alan J. Broder
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------

def set_canvas_size(image, w=_DEFAULT_CANVAS_SIZE, h=_DEFAULT_CANVAS_SIZE):
    """
    Set the size of the canvas to w pixels wide and h pixels high.
    Calling this function is optional. If you call it, you must do
    so before calling any drawing function.
    """
    global _background
    global _surface
    global _canvasWidth
    global _canvasHeight
    global _windowCreated

    if _windowCreated:
        raise Exception('The stddraw window already was created')

    if (w < 1) or (h < 1):
        raise Exception('width and height must be positive')

    _canvasWidth = w
    _canvasHeight = h
    _background = pygame.display.set_mode([w, h])
    pygame.display.set_caption('Billard Simulator 3000')
    _surface = pygame.Surface((w, h))
    if image != None:
        _surface = image  # todo KATZEN
        # surface = pygame.transform.scale(_surface, (w, h))                        # Verändert den angezeigten Bild ausschnitt
    else:
        _surface.fill(_pygame_color(color.WHITE))
    _windowCreated = True


def set_x_scale(min=_DEFAULT_XMIN, max=_DEFAULT_XMAX):
    """
    Set the x-scale of the canvas such that the minimum x value
    is min and the maximum x value is max.
    """
    global _xmin
    global _xmax
    min = float(min)
    max = float(max)
    if min >= max:
        raise Exception('min must be less than max')
    size = max - min
    _xmin = min - _BORDER*size
    _xmax = max + _BORDER*size


def set_y_scale(min=_DEFAULT_YMIN, max=_DEFAULT_YMAX):
    """
    Set the y-scale of the canvas such that the minimum y value
    is min and the maximum y value is max.
    """
    global _ymin
    global _ymax
    min = float(min)
    max = float(max)
    if min >= max:
        raise Exception('min must be less than max')
    size = max - min
    _ymin = min - _BORDER*size
    _ymax = max + _BORDER*size


def set_pen_radius(r=_DEFAULT_PEN_RADIUS):
    """
    Set the pen radius to r, thus affecting the subsequent drawing
    of points and lines. If r is 0.0, then points will be drawn with
    the minimum possible radius and lines with the minimum possible
    width.
    """
    global _pen_radius
    r = float(r)
    if r < 0.0:
        raise Exception('Argument to setPenRadius() must be non-neg')
    _pen_radius = r*float(_DEFAULT_CANVAS_SIZE)


def set_pen_color(c=_DEFAULT_PEN_COLOR):
    """
    Set the pen color to c, where c is an object of class color.Color.
    c defaults to stddraw.BLACK.
    """
    global _penColor
    _penColor = c


def set_font_family(f=_DEFAULT_FONT_FAMILY):
    """
    Set the font family to f (e.g. 'Helvetica' or 'Courier').
    """
    global _fontFamily
    _fontFamily = f


def set_font_size(s=_DEFAULT_FONT_SIZE):
    """
    Set the font size to s (e.g. 12 or 16).
    """
    global _fontSize
    _fontSize = s


# -----------------------------------------------------------------------

def _make_sure_window_created():
    global _windowCreated
    if not _windowCreated:
        set_canvas_size()
        _windowCreated = True


# -----------------------------------------------------------------------

# Functions to draw shapes, text, and images on the background canvas.

def _pixel(x, y):
    """
    Draw on the background canvas a pixel at (x, y).
    """
    _make_sure_window_created()
    xs = _scale_x(x)
    xy = _scale_y(y)
    pygame.gfxdraw.pixel(
            _surface,
            int(round(xs)),
            int(round(xy)),
            _pygame_color(_penColor))


def point(x, y):
    """
    Draw on the background canvas a point at (x, y).
    """
    _make_sure_window_created()
    x = float(x)
    y = float(y)
    # If the radius is too small, then simply draw a pixel.
    if _pen_radius <= 1.0:
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)
        pygame.draw.ellipse(
                _surface,
                _pygame_color(_penColor),
                pygame.Rect(
                        xs - _pen_radius,
                        ys - _pen_radius,
                        _pen_radius*2.0,
                        _pen_radius*2.0),
                0)


def _thick_line(x0, y0, x1, y1, r):
    """
    Draw on the background canvas a line from (x0, y0) to (x1, y1).
    Draw the line with a pen whose radius is r.
    """
    xs0 = _scale_x(x0)
    ys0 = _scale_y(y0)
    xs1 = _scale_x(x1)
    ys1 = _scale_y(y1)
    if (abs(xs0 - xs1) < 1.0) and (abs(ys0 - ys1) < 1.0):
        filled_circle(x0, y0, r)
        return
    x_mid = (x0 + x1)/2
    y_mid = (y0 + y1)/2
    _thick_line(x0, y0, x_mid, y_mid, r)
    _thick_line(x_mid, y_mid, x1, y1, r)


def line(x0, y0, x1, y1):
    """
    Draw on the background canvas a line from (x0, y0) to (x1, y1).
    """

    thick_line_cutoff = 3  # pixels

    _make_sure_window_created()

    x0 = float(x0)
    y0 = float(y0)
    x1 = float(x1)
    y1 = float(y1)

    line_width = _pen_radius*2.0
    if line_width == 0.0:
        line_width = 1.0
    if line_width < thick_line_cutoff:
        x0s = _scale_x(x0)
        y0s = _scale_y(y0)
        x1s = _scale_x(x1)
        y1s = _scale_y(y1)
        pygame.draw.line(
                _surface,
                _pygame_color(_penColor),
                (x0s, y0s),
                (x1s, y1s),
                int(round(line_width)))
    else:
        _thick_line(x0, y0, x1, y1, _pen_radius/_DEFAULT_CANVAS_SIZE)


def circle(x, y, r):
    """
    Draw on the background canvas a circle of radius r centered on
    (x, y).
    """
    _make_sure_window_created()
    x = float(x)
    y = float(y)
    r = float(r)
    ws = _factor_x(2.0*r)
    hs = _factor_y(2.0*r)
    # If the radius is too small, then simply draw a pixel.
    if (ws <= 1.0) and (hs <= 1.0):
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)
        pygame.draw.ellipse(
                _surface,
                _pygame_color(_penColor),
                pygame.Rect(xs - ws/2.0, ys - hs/2.0, ws, hs),
                int(round(_pen_radius)))


def filled_circle(x, y, r):
    """
    Draw on the background canvas a filled circle of radius r
    centered on (x, y).
    """
    _make_sure_window_created()
    x = float(x)
    y = float(y)
    r = float(r)
    ws = _factor_x(2.0*r)
    hs = _factor_y(2.0*r)
    # If the radius is too small, then simply draw a pixel.
    if (ws <= 1.0) and (hs <= 1.0):
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)
        pygame.draw.ellipse(
                _surface,
                _pygame_color(_penColor),
                pygame.Rect(xs - ws/2.0, ys - hs/2.0, ws, hs),
                0)


def rectangle(x, y, w, h):
    """
    Draw on the background canvas a rectangle of width w and height h
    whose lower left point is (x, y).
    """
    global _surface
    _make_sure_window_created()
    x = float(x)
    y = float(y)
    w = float(w)
    h = float(h)
    ws = _factor_x(w)
    hs = _factor_y(h)
    # If the rectangle is too small, then simply draw a pixel.
    if (ws <= 1.0) and (hs <= 1.0):
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)
        pygame.draw.rect(
                _surface,
                _pygame_color(_penColor),
                pygame.Rect(xs, ys - hs, ws, hs),
                int(round(_pen_radius)))


def filled_rectangle(x, y, w, h):
    """
    Draw on the background canvas a filled rectangle of width w and
    height h whose lower left point is (x, y).
    """
    global _surface
    _make_sure_window_created()
    x = float(x)
    y = float(y)
    w = float(w)
    h = float(h)
    ws = _factor_x(w)
    hs = _factor_y(h)
    # If the rectangle is too small, then simply draw a pixel.
    if (ws <= 1.0) and (hs <= 1.0):
        _pixel(x, y)
    else:
        xs = _scale_x(x)
        ys = _scale_y(y)
        pygame.draw.rect(
                _surface,
                _pygame_color(_penColor),
                pygame.Rect(xs, ys - hs, ws, hs),
                0)


def square(x, y, r):
    """
    Draw on the background canvas a square whose sides are of length
    2r, centered on (x, y).
    """
    _make_sure_window_created()
    rectangle(x - r, y - r, 2.0*r, 2.0*r)


def filled_square(x, y, r):
    """
    Draw on the background canvas a filled square whose sides are of
    length 2r, centered on (x, y).
    """
    _make_sure_window_created()
    filled_rectangle(x - r, y - r, 2.0*r, 2.0*r)


def filled_diamond(x, y, r):
    _make_sure_window_created()
    filled_polygon([x + r, x, x - r, x], [y, y + r, y, y - r])


def polygon(x, y):
    """
    Draw on the background canvas a polygon with coordinates
    (x[i], y[i]).
    """
    global _surface
    _make_sure_window_created()
    # Scale X and Y values.
    x_scaled = []
    for xi in x:
        x_scaled.append(_scale_x(float(xi)))
    y_scaled = []
    for yi in y:
        y_scaled.append(_scale_y(float(yi)))
    points = []
    for i in range(len(x)):
        points.append((x_scaled[i], y_scaled[i]))
    points.append((x_scaled[0], y_scaled[0]))
    pygame.draw.polygon(
            _surface,
            _pygame_color(_penColor),
            points,
            int(round(_pen_radius)))


def filled_polygon(x, y):
    """
    Draw on the background canvas a filled polygon with coordinates
    (x[i], y[i]).
    """
    global _surface
    _make_sure_window_created()
    # Scale X and Y values.
    x_scaled = []
    for xi in x:
        x_scaled.append(_scale_x(float(xi)))
    y_scaled = []
    for yi in y:
        y_scaled.append(_scale_y(float(yi)))
    points = []
    for i in range(len(x)):
        points.append((x_scaled[i], y_scaled[i]))
    points.append((x_scaled[0], y_scaled[0]))
    pygame.draw.polygon(_surface, _pygame_color(_penColor), points, 0)


def filled_raute(x, y, breite):
    haelfte = breite/2
    x = [x, x - haelfte, x, x + haelfte]
    y = [y - haelfte, y, y + haelfte, y]
    filled_polygon(x, y)


def text(x, y, s):
    """
    Draw string s on the background canvas centered at (x, y).
    """
    _make_sure_window_created()
    x = float(x)
    y = float(y)
    xs = _scale_x(x)
    ys = _scale_y(y)
    font = pygame.font.SysFont(_fontFamily, _fontSize)
    text = font.render(s, 1, _pygame_color(_penColor))
    textpos = text.get_rect(center = (xs, ys))
    _surface.blit(text, textpos)


def picture(pic, w, h, x=None, y=None):
    """
    Draw pic on the background canvas centered at (x, y).  pic is an
    object of class picture.Picture. x and y default to the midpoint
    of the background canvas.
    """
    global _surface
    _make_sure_window_created()
    # By default, draw pic at the middle of the surface.
    if x is None:
        x = (_xmax + _xmin)/2.0
    if y is None:
        y = (_ymax + _ymin)/2.0
    x = float(x)
    y = float(y)
    xs = _scale_x(x)
    ys = _scale_y(y)
    ws = pic.width()
    hs = pic.height()
    #ws = w # EDITED
    #hs = h # EDITED
    pic_surface = pic._surface  # violates encapsulation

    #_background.blit(pic, (100, 100))
    _surface.blit(pic_surface, [xs - ws/2.0, ys - hs/2.0, ws, hs])


def picture_improved(image, x, y):
    _background.blit(image, (x, y))
    pygame.display.flip()



def clear(c):
    """
    Clear the background canvas to color c, where c is an
    object of class color.Color. c defaults to stddraw.WHITE.
    """
    global _surface
    _make_sure_window_created()
    if c == None:
        _surface.fill(_pygame_color(color.WHITE))
    elif c == 'cat':
        _surface = pygame.transform.rotozoom(pygame.image.load("cat Kopie.jpg"), 0, 0.5)
    else:
        _surface = pygame.transform.rotozoom(pygame.image.load("lion 3001.jpg"), 0, 0.32)


def save(f):
    """
    Save the window canvas to file f.
    """
    _make_sure_window_created()

    # if sys.hexversion >= 0x03000000:
    #    # Hack because Pygame without full image support
    #    # can handle only .bmp files.
    #    bmpFileName = f + '.bmp'
    #    pygame.image.save(_surface, bmpFileName)
    #    os.system('convert ' + bmpFileName + ' ' + f)
    #    os.system('rm ' + bmpFileName)
    # else:
    #    pygame.image.save(_surface, f)

    pygame.image.save(_surface, f)


# -----------------------------------------------------------------------

def _show():
    """
    Copy the background canvas to the window canvas.
    """
    _background.blit(_surface, (0, 0))
    pygame.display.flip()
    _check_for_events()


def _show_and_wait_forever():
    """
    Copy the background canvas to the window canvas. Then wait
    forever, that is, until the user closes the stddraw window.
    """
    _make_sure_window_created()
    _show()
    quantum = .1
    while True:
        time.sleep(quantum)
        _check_for_events()


def show(msec=float('inf')):
    """
    Copy the background canvas to the window canvas, and
    then wait for msec milliseconds. msec defaults to infinity.
    """
    if msec == float('inf'):
        _show_and_wait_forever()

    _make_sure_window_created()
    _show()
    _check_for_events()

    # Sleep for the required time, but check for events every
    # QUANTUM seconds.
    quantum = .1
    sec = msec/1000.0
    if sec < quantum:
        time.sleep(sec)
        return
    seconds_waited = 0.0
    while seconds_waited < sec:
        time.sleep(quantum)
        seconds_waited += quantum
        _check_for_events()


# -----------------------------------------------------------------------

def _save_to_file():
    """
    Display a dialog box that asks the user for a file name.  Save the
    drawing to the specified file.  Display a confirmation dialog box
    if successful, and an error dialog box otherwise.  The dialog boxes
    are displayed using Tkinter, which (on some computers) is
    incompatible with Pygame. So the dialog boxes must be displayed
    from child processes.
    """
    import subprocess
    _make_sure_window_created()

    stddraw_path = os.path.realpath(__file__)

    child_process = subprocess.Popen(
            [sys.executable, stddraw_path, 'getFileName'],
            stdout = subprocess.PIPE)
    so, se = child_process.communicate()
    file_name = so.strip()

    if sys.hexversion >= 0x03000000:
        file_name = file_name.decode('utf-8')

    if file_name == '':
        return

    if not file_name.endswith(('.jpg', '.png')):
        child_process = subprocess.Popen(
                [sys.executable, stddraw_path, 'reportFileSaveError',
                 'File name must end with ".jpg" or ".png".'])
        return

    try:
        save(file_name)
        child_process = subprocess.Popen(
                [sys.executable, stddraw_path, 'confirmFileSave'])
    except (pygame.error) as e:
        child_process = subprocess.Popen(
                [sys.executable, stddraw_path, 'reportFileSaveError', str(e)])


def _check_for_events():
    """
    Check if any new event has occured (such as a key typed or button
    pressed).  If a key has been typed, then put that key in a queue.
    """
    global _surface
    global _keysTyped

    # -------------------------------------------------------------------
    # Begin added by Alan J. Broder
    # -------------------------------------------------------------------
    global _mousePos
    global _mousePressed
    # -------------------------------------------------------------------
    # End added by Alan J. Broder
    # -------------------------------------------------------------------

    _make_sure_window_created()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _keysTyped = [event.unicode] + _keysTyped
        elif (event.type == pygame.MOUSEBUTTONUP) and\
                (event.button == 3):
            _save_to_file()

        # ---------------------------------------------------------------
        # Begin added by Alan J. Broder
        # ---------------------------------------------------------------
        # Every time the mouse button is pressed, remember
        # the mouse position as of that press.
        elif (event.type == pygame.MOUSEBUTTONDOWN) and\
                (event.button == 1):
            _mousePressed = True
            _mousePos = event.pos
            # ---------------------------------------------------------------
            # End added by Alan J. Broder
            # ---------------------------------------------------------------


# -----------------------------------------------------------------------

# Functions for retrieving keys

def has_next_key_typed():
    """
    Return True if the queue of keys the user typed is not empty.
    Otherwise return False.
    """
    global _keysTyped
    return _keysTyped != []


def next_key_typed():
    """
    Remove the first key from the queue of keys that the the user typed,
    and return that key.
    """
    global _keysTyped
    return _keysTyped.pop()


# -----------------------------------------------------------------------
# Begin added by Alan J. Broder
# -----------------------------------------------------------------------

# Functions for dealing with mouse clicks 

def mouse_pressed():
    """
    Return True if the mouse has been left-clicked since the 
    last time mousePressed was called, and False otherwise.
    """
    global _mousePressed
    if _mousePressed:
        _mousePressed = False
        return True
    return False


def mouse_position():
    """
    Return the x and y coordinate in user space of the location at
    which the mouse is positioned at the moment.
    """
    x_mouse, y_mouse = pygame.mouse.get_pos()
    x_mouse /= _canvasWidth
    y_mouse /= _canvasHeight
    y_mouse = 1 - y_mouse
    return (x_mouse, y_mouse)


# -----------------------------------------------------------------------
# End added by Alan J. Broder
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------

# Initialize the x scale, the y scale, and the pen radius.

set_x_scale()
set_y_scale()
set_pen_radius()
pygame.font.init()


# -----------------------------------------------------------------------

# Functions for displaying Tkinter dialog boxes in child processes.

def _get_file_name():
    """
    Display a dialog box that asks the user for a file name.
    """
    root = tkinter.Tk()
    root.withdraw()
    reply = tk_file_dialog.asksaveasfilename(initialdir = '.')
    sys.stdout.write(reply)
    sys.stdout.flush()
    sys.exit()


def _confirm_file_save():
    """
    Display a dialog box that confirms a file save operation.
    """
    root = tkinter.Tk()
    root.withdraw()
    tk_message_box.showinfo(title = 'File Save Confirmation',
                            message = 'The drawing was saved to the file.')
    sys.exit()


def _report_file_save_error(msg):
    """
    Display a dialog box that reports a msg.  msg is a string which
    describes an error in a file save operation.
    """
    root = tkinter.Tk()
    root.withdraw()
    tk_message_box.showerror(title = 'File Save Error', message = msg)
    sys.exit()
