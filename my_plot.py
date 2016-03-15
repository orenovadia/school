import matplotlib.pyplot as plt

class My_Plot(object):
    colors = list('rgbygpmc')
    number_of_colors = len(colors)
    color_index=0
    def __init__(self,increment_colors=False):
        self._increment_colors = True
    def plot(self,*args,**kwargs):
        if 'color' not in kwargs:
            kwargs['colors'] = self.colors[self.color_index%self.number_of_colors]
            self.color_index += 1
        plt.plot(*args,**kwargs)
    def show(self):
        plt.show()