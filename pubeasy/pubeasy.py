import matplotlib.font_manager as fm
from matplotlib.pylab import *
import os,sys

LARGE = 20
c1 = '#1f77b4'
c2 = '#f77f0e'
c3 = '#2ca02c'


class MakeFigure(object):

  def __init__(self,**argv):

      self.init_plotting()
      self.names = []


  def savefigure(self,prefix = './'):

   namefile =  prefix + sys.argv[0].split('.')[0]+'.png'

   savefig(namefile,dpi=500)
 
  def add_plot(self,x,y,name,marker=False):

     self.names.append(name) 
     self.ax.plot(x,y,marker = 'o' if marker else 'None') 

  def add_labels(self,x,y):

      f = self.fonts['regular']
      f.set_size(LARGE)
      self.ax.set_xlabel(x,fontproperties=self.fonts['regular'])
      self.ax.set_ylabel(y,fontproperties=self.fonts['regular'])

  def finalize(self,**argv):

       f = self.fonts['regular']
       f.set_size(18)
       legend(self.names,prop=f,frameon=True)
       xticks(fontproperties=self.fonts['regular'])
       yticks(fontproperties=self.fonts['regular'])
       grid('on',which='both')

       for child in gca().get_children(): 
        x = isinstance(child, matplotlib.text.Text)
        if x:
         child.set_font_propertie = self.fonts['regular']
       for child in gcf().get_children(): 
        x = isinstance(child, matplotlib.text.Text)
        if x:
         child.set_font_properties = self.fonts['regular']

       for label in gca().get_xticklabels():
        label.set_fontproperties(self.fonts['regular'])
       for label in gca().get_yticklabels():
        label.set_fontproperties(self.fonts['regular'])

       xscale(argv.setdefault('xscale','linear'))

       if 'xlim' in argv.keys():
         xlim(argv['xlim'])  
       if 'ylim' in argv.keys():
         ylim(argv['ylim'])  

       xscale(argv.setdefault('xscale','lin'))

       if argv.setdefault('write',False):
          self.savefigure() 
       
       if argv.setdefault('show',True):
        show()
      
    #-------------------


  def init_plotting(self,extra_x_padding = 0.0,extra_y_padding=0.0,extra_bottom_padding = 0.0,extra_top_padding=  0.0,paraview=False,square=False,delta_square = 0,presentation=False):


   rcParams['xtick.major.pad']='10'
   rcParams['mathtext.fontset'] = 'cm'
   rcParams['lines.linewidth'] = 4
   rcParams['font.size'] = LARGE
   rcParams['xtick.labelsize'] = LARGE
   rcParams['ytick.labelsize'] = LARGE
   if square:
    rcParams['figure.figsize'] = [4.0, 4.0]
   else:
    rcParams['figure.figsize'] = [8.0, 5.0]
   if presentation:
    rcParams['figure.figsize'] = [16.0, 12.0]
 

   #load fonts----
   filename = os.path.dirname(__file__) + '/fonts/cmunrm.ttf'
   prop_regular = fm.FontProperties(fname=filename,family='serif')
   filename = os.path.dirname(__file__) + '/fonts/cmunbx.ttf'
   prop_bold = fm.FontProperties(fname=filename,family='serif')
   filename = os.path.dirname(__file__) + '/fonts/cmunti.ttf'
   prop_italic = fm.FontProperties(fname=filename,family='serif')
   fonts = {'regular':prop_regular,'italic':prop_italic,'bold':prop_bold}

   rcParams['figure.dpi'] = 80
   rcParams['savefig.dpi'] = 400
   rcParams['xtick.major.size'] = 3
   rcParams['xtick.minor.size'] = 3
   rcParams['figure.edgecolor'] = 'k'
   rcParams['figure.facecolor'] = 'w'
   rcParams['xtick.major.width'] = 1
   rcParams['xtick.minor.width'] = 1
   rcParams['ytick.major.size'] = 3
   rcParams['ytick.minor.size'] = 3
   rcParams['ytick.major.width'] = 1
   rcParams['ytick.minor.width'] = 1
   rcParams['legend.frameon'] = False
   rcParams['legend.fontsize'] = 25
   rcParams['axes.linewidth'] = 1

   #self.fig = figure()
   #self.ax  = self.fig.add_subplot(1, 1,1)

   self.ax = axes([0.12+extra_x_padding,0.15+extra_bottom_padding,0.78-extra_x_padding-extra_y_padding,0.75-extra_bottom_padding-extra_top_padding])
   self.fonts = fonts


