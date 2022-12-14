import numpy as np
from psychopy.visual import TextStim, Line, RadialStim,Circle,DotStim


class FixationLines(object):

    def __init__(self, win, circle_radius, color, line_width, *args, **kwargs):
        self.color = color
        self.line_width = line_width
        self.line1 = Line(win, start=(-circle_radius, -circle_radius),
                          end=(circle_radius, circle_radius), lineColor=self.color, lineWidth=self.line_width, *args, **kwargs)
        self.line2 = Line(win, start=(-circle_radius, circle_radius),
                          end=(circle_radius, -circle_radius), lineColor=self.color, lineWidth=self.line_width, *args, **kwargs)

    def draw(self):
        self.line1.draw()
        self.line2.draw()

    def setColor(self, color):
        self.line1.color = color
        self.line2.color = color
        self.color = color

#fixation cross with dot in the middle
class FixationCross(object):
    
        def __init__(self, win, circle_radius, color, line_width, *args, **kwargs):
            self.color = color
            self.line_width = line_width
            self.line1 = Line(win, start=(-circle_radius, 0),
                            end=(circle_radius, 0), lineColor=self.color, lineWidth=self.line_width, *args, **kwargs)
            self.line2 = Line(win, start=(0, -circle_radius),
                            end=(0, circle_radius), lineColor=self.color, lineWidth=self.line_width, *args, **kwargs)
            self.dot = DotStim(win, color=self.color, *args, **kwargs)
    
        def draw(self):
            self.line1.draw()
            self.line2.draw()
            self.dot.draw()
    
        def setColor(self, color):
            self.line1.color = color
            self.line2.color = color
            self.dot.color = color
            self.color = color
    


class FixationBullsEye(object):

    def __init__(self, win, circle_radius, color, pos=[0,0], edges=360, *args, **kwargs):
        self.color = color
        self.line1 = Line(win, start=(-circle_radius+pos[0], -circle_radius+pos[1]),
                          end=(circle_radius+pos[0], circle_radius+pos[1]), lineColor=self.color, *args, **kwargs)
        self.line2 = Line(win, start=(-circle_radius+pos[0], circle_radius+pos[1]),
                          end=(circle_radius+pos[0], -circle_radius+pos[1]), lineColor=self.color, *args, **kwargs)
        self.circle1 = Circle(win, radius=circle_radius*0.5, edges=edges, fillColor=None, lineColor=self.color, *args, **kwargs)
        self.circle2 = Circle(win, radius=circle_radius*0.375, edges=edges, fillColor=None, lineColor=self.color, *args, **kwargs)
        self.circle3 = Circle(win, radius=circle_radius*0.25, edges=edges, fillColor=None, lineColor=self.color, *args, **kwargs)
        self.circle4 = Circle(win, radius=circle_radius*0.125, edges=edges, fillColor=None, lineColor=self.color, *args, **kwargs)

    def draw(self):
        self.line1.draw()
        self.line2.draw()
        self.circle1.draw()
        self.circle2.draw()
        self.circle3.draw()
        self.circle4.draw()

    def setColor(self, color):
        self.line1.color = color
        self.line2.color = color
        self.circle1.color = color
        self.circle2.color = color
        self.circle3.color = color
        self.circle4.color = color
        self.color = color


        
