# -*- coding: utf-8 -*-

#  将Matplotlib嵌入wxPython的GUI界面中

import wx
import numpy as np
import matplotlib
import pandas as pd
import math
 
# matplotlib采用WXAgg为后台,将matplotlib嵌入wxPython中
matplotlib.use("WXAgg")
 
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.ticker import MultipleLocator, FuncFormatter
 
import pylab
from matplotlib import pyplot 
 
######################################################################################
class MPL_Panel_base(wx.Panel):
    ''''' #MPL_Panel_base面板,可以继承或者创建实例'''
 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=-1)
 
        self.Figure = matplotlib.figure.Figure(figsize=(4, 3))
        self.axes = self.Figure.add_axes([0.1, 0.1, 0.8, 0.8])
        self.FigureCanvas = FigureCanvas(self, -1, self.Figure)
 
        self.NavigationToolbar = NavigationToolbar(self.FigureCanvas) 
        self.StaticText = wx.StaticText(self, -1, label='Show information here!')
 
        self.SubBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SubBoxSizer.Add(self.NavigationToolbar, proportion=-5, border=2) #flag=wx.ALL | wx.EXPAND
        self.SubBoxSizer.Add(self.StaticText, proportion=-4, border=2)
 
        self.TopBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.TopBoxSizer.Add(self.SubBoxSizer, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
        self.TopBoxSizer.Add(self.FigureCanvas, proportion=-10, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.SetSizer(self.TopBoxSizer)
 
        ###方便调用
        self.pylab = pylab
        self.pl = pylab
        self.pyplot = pyplot
        self.numpy = np
        self.np = np
        self.plt = pyplot
 
    def UpdatePlot(self):
        '''''#修改图形的任何属性后都必须使用self.UpdatePlot()更新GUI界面 '''
        self.FigureCanvas.draw()
 
    def plot(self, *args, **kwargs):
        '''''#最常用的绘图命令plot '''
        self.axes.plot(*args, **kwargs)
        self.UpdatePlot()
 
    def plot_vlines(self, *args, **kwargs):
        '''''#最常用的绘图命令plot '''
        self.axes.vlines(*args, **kwargs)
        self.UpdatePlot()
        
 
    def plot_axvline(self, *args, **kwargs):
        '''''#最常用的绘图命令plot '''
        self.axes.axvline(*args, **kwargs)
        self.UpdatePlot()       
 
    def semilogx(self, *args, **kwargs):
        ''''' #对数坐标绘图命令 '''
        self.axes.semilogx(*args, **kwargs)
        self.UpdatePlot()
 
    def semilogy(self, *args, **kwargs):
        ''''' #对数坐标绘图命令 '''
        self.axes.semilogy(*args, **kwargs)
        self.UpdatePlot()
 
    def loglog(self, *args, **kwargs):
        ''''' #对数坐标绘图命令 '''
        self.axes.loglog(*args, **kwargs)
        self.UpdatePlot()
 
    def grid(self, flag=True):
        ''''' ##显示网格  '''
        if flag:
            self.axes.grid()
        else:
            self.axes.grid(False)
 
    def title_MPL(self, TitleString="wxMatPlotLib Example In wxPython"):
        ''''' # 给图像添加一个标题   '''
        self.axes.set_title(TitleString)
 
    def xlabel(self, XabelString="X"):
        ''''' # Add xlabel to the plotting    '''
        self.axes.set_xlabel(XabelString)
 
    def ylabel(self, YabelString="Y"):
        ''''' # Add ylabel to the plotting '''
        self.axes.set_ylabel(YabelString)
 
    def xticker(self, major_ticker=1.0, minor_ticker=0.1):
        ''''' # 设置X轴的刻度大小 '''
        self.axes.xaxis.set_major_locator(MultipleLocator(major_ticker))
        self.axes.xaxis.set_minor_locator(MultipleLocator(minor_ticker))
 
    def yticker(self, major_ticker=1.0, minor_ticker=0.1):
        ''''' # 设置Y轴的刻度大小 '''
        self.axes.yaxis.set_major_locator(MultipleLocator(major_ticker))
        self.axes.yaxis.set_minor_locator(MultipleLocator(minor_ticker))
 
    def legend(self, *args, **kwargs):
        ''''' #图例legend for the plotting  '''
        self.axes.legend(*args, **kwargs)
 
    def xlim(self, x_min, x_max):
        ''' # 设置x轴的显示范围  '''
        self.axes.set_xlim(x_min, x_max)
 
    def ylim(self, y_min, y_max):
        ''' # 设置y轴的显示范围   '''
        self.axes.set_ylim(y_min, y_max)
 
    def savefig(self, *args, **kwargs):
        ''' #保存图形到文件 '''
        self.Figure.savefig(*args, **kwargs)
 
    def cla(self):
        ''' # 再次画图前,必须调用该命令清空原来的图形  '''
        self.axes.clear()
        self.Figure.set_canvas(self.FigureCanvas)
        self.UpdatePlot()
 
    def ShowHelpString(self, HelpString="Show Help String"):
        ''''' #可以用它来显示一些帮助信息,如鼠标位置等 '''
        self.StaticText.SetLabel(HelpString)
 
        ################################################################
 
 
class MPL_Panel(MPL_Panel_base):
    ''''' #MPL_Panel重要面板,可以继承或者创建实例 '''
 
    def __init__(self, parent):
        MPL_Panel_base.__init__(self, parent=parent)
 
        # 测试一下
        self.FirstPlot()
 
 
        # 仅仅用于测试和初始化,意义不大
 
    def FirstPlot(self):
        # self.rc('lines',lw=5,c='r')
        self.cla()
        x = np.arange(-5, 5, 0.25)
        y = np.sin(x)
        self.yticker(0.5, 0.1)
        self.xticker(1.0, 0.2)
        self.xlabel('X')
        self.ylabel('Y')
        self.title_MPL("图像")
        self.grid()
        self.plot(x, y, '--^g')
 
 
        ###############################################################################
 
 
# MPL_Frame添加了MPL_Panel的1个实例
###############################################################################
class MPL_Frame(wx.Frame):
    """MPL_Frame可以继承,并可修改,或者直接使用"""
 
    def __init__(self, title="App TITLE", size=(1000, 600)):
        wx.Frame.__init__(self, parent=None, title=title, size=size)
 
        self.MPL = MPL_Panel_base(self)
 
        # RightPanel
        # 创建FlexGridSizer
        self.FlexGridSizer = wx.FlexGridSizer(rows=9, cols=1, vgap=5, hgap=5)
        self.FlexGridSizer.SetFlexibleDirection(wx.BOTH)
 
        self.RightPanel = wx.Panel(self, -1)
 
        # Import按钮
        self.BtnImport = wx.Button(self.RightPanel, -1, "导入数据", size=(100, 40), pos=(10, 10))
        self.BtnImport.Bind(wx.EVT_BUTTON, self.BtnImportEvent)
        
        # std
        self.StaticText_STD = wx.StaticText(self.RightPanel, -1, label='\n测试点STD:',size=(100, 30), pos=(10, 10))
        self.txtCtrl_STD = wx.TextCtrl(self.RightPanel, -1, value ='950.0',size=(100, 20), pos=(10, 10))
        #self.BtnPlotCPK.Bind(wx.EVT_BUTTON, self.BtnPlotCPKEvent)
        
        #lsl
        self.StaticText_LSL = wx.StaticText(self.RightPanel, -1, label='\n下限LSL:',size=(100, 30), pos=(10, 10))
        self.txtCtrl_LSL = wx.TextCtrl(self.RightPanel, -1, value ='930.5',size=(100, 20), pos=(10, 10))

        
        # usl
        self.StaticText_USL = wx.StaticText(self.RightPanel, -1, label='\n上限USL:',size=(100, 30), pos=(10, 10))
        self.txtCtrl_USL = wx.TextCtrl(self.RightPanel, -1,value ='969.5', size=(100, 20), pos=(10, 10))
        
        
        # PlotCPK按钮
        self.BtnPlotCPK = wx.Button(self.RightPanel, -1, "生成CPK曲线", size=(100, 40), pos=(10, 10))
        self.BtnPlotCPK.Bind(wx.EVT_BUTTON, self.BtnPlotCPKEvent)
 
        # About按钮
        self.BtnAbout = wx.Button(self.RightPanel, -1, "关于", size=(100, 40), pos=(10, 10))
        self.BtnAbout.Bind(wx.EVT_BUTTON, self.BtnAboutEvent)
 
        # 加入Sizer中
        self.FlexGridSizer.Add(self.BtnImport, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.StaticText_STD, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.txtCtrl_STD, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.StaticText_LSL, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.txtCtrl_LSL, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.StaticText_USL, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.txtCtrl_USL, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.BtnPlotCPK, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.BtnAbout, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
 
        self.RightPanel.SetSizer(self.FlexGridSizer)
 
        self.BoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.BoxSizer.Add(self.MPL, proportion=-10, border=2, flag=wx.ALL | wx.EXPAND)
        self.BoxSizer.Add(self.RightPanel, proportion=0, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.SetSizer(self.BoxSizer)
 
        # 状态栏
        self.StatusBar()
        self.MPL.ShowHelpString("1. Import the sample date in xlsx files!\r\n2. Fill STD,USL,LSL\r\n3. Press the Plotting button to genarate the Probability Density curve.")
 
        # MPL_Frame界面居中显示
        self.Centre(wx.BOTH) 
        self.pd_data = None
 
 
    # 按钮事件,用于测试 
    def BtnPlotCPKEvent(self, event):
    
        if self.pd_data is  None: 
            dlg = wx.MessageDialog(self, 'Please import data first~~~~!!!!\n')
            dlg.ShowModal()
            dlg.Destroy()
            return
        
        self.MPL.cla()  # 必须清理图形,才能显示下一幅图
        
        #x = np.arange(-10, 10, 0.25)
        #y = np.cos(x)
        
        #self.MPL.plot(x, y, '--*g')
        #self.MPL.xticker(2.0, 0.5)
        #self.MPL.yticker(0.5, 0.1)
        #self.MPL.title_MPL("MPL1")   
        usl = 969.5
        lsl = 930.5
        std = 950   

        usl = float(self.txtCtrl_USL.GetValue())
        lsl = float(self.txtCtrl_LSL.GetValue())
        std = float(self.txtCtrl_STD.GetValue())
        print(usl,lsl,std)
        
        self.cpk_calc(self.pd_data,usl,lsl,std) 
        
        
        self.MPL.grid()
        self.MPL.UpdatePlot()  # 必须刷新才能显示
        
        
    def cpk_calc(self,df_data:pd.DataFrame, usl, lsl,std):
        """
        :param df_data: 数据dataframe
        :param usl: 数据指标上限
        :param lsl: 数据指标下限
        :return:
        """
        title = None
        legendlist = []
        
        sigma = 3
        
        # 若下限为0, 则使用上限反转负值替代
        if int(lsl) == 0:
            lsl = 0 - usl
     
        # 数据平均值
        s = df_data.mean()
        #self.MPL.figure(figsize=(15,10))
        
        for i in range(len(s.values)):
            serialTitle = s.index[i]
            u = s.values[i]

            # 数据标准差
            stdev = np.std(df_data.values, ddof=1)

            # 生成横轴数据平均分布
            #x1 = np.linspace(std - sigma * stdev-0.5, std + sigma * stdev + 0.5, 1000)
            x1 = np.linspace(lsl - 0.5, usl + 0.5, 1000)

            # 计算正态分布曲线
            y1 = np.exp(-(x1 - u) ** 2 / (2 * stdev ** 2)) / (math.sqrt(2 * math.pi) * stdev)
            
            # 得出cpk
            cpu = (usl - u) / (sigma * stdev)
            cpl = (u - lsl) / (sigma * stdev)       
            cpk = min(cpu, cpl)

            # 使用matplotlib画图
            #self.MPL.xlim(x1[0] - 0.5, x1[-1] + 0.5)
            self.MPL.xlim(lsl - 0.5, usl + 0.5)
            
            self.MPL.plot(x1, y1)
            #plt.hist(df_data.values, 15, density=True)   # bar
            if title is None:  #{:20}\t{:28}\t{:32}
                title = "{:<10} :CPK={:<15},mean = {:.2f},stdev = {:.6f}\n".format(serialTitle,cpk,u,stdev)
            else:
                title = title + ("{:<10} :CPK={:<15},mean = {:.2f},stdev = {:.6f}\n".format(serialTitle,cpk,u,stdev))
                
            
            
            legendlist.append(serialTitle)
            self.MPL.plot_vlines([x1[np.argmax(y1)]],ymin = 0,ymax = y1[np.argmax(y1)], color='gray', linestyle='--')  # 

            
        self.MPL.plot_axvline(usl, color='r', linestyle='--', label='USL')
        legendlist.append('USL')
        
        self.MPL.plot_axvline(lsl, color='r', linestyle='--', label='LSL')
        legendlist.append('LSL')
        
        self.MPL.plot_axvline(std, color='r', linestyle='--', label='STD')   
        legendlist.append('STD')
        
        self.MPL.plot_axvline(std - sigma * stdev, color='blue', linestyle='--', label='-3 Sigma')
        legendlist.append('-3 Sigma')
        
        self.MPL.plot_axvline(std + sigma * stdev, color='blue', linestyle='--', label='3 Sigma')
        legendlist.append('3 Sigma')
        
        self.MPL.legend(legendlist)
        self.MPL.xlabel(title)
        self.MPL.ylabel('Probability Density')
        #self.MPL.title_MPL(title)
        #self.MPL.ShowHelpString(title)
        
        self.MPL.savefig('cpk1.png',bbox_inches='tight')
        #plt.show()

 
    def BtnAboutEvent(self, event):
        self.AboutDialog() 
 
    # 打开文件,用于测试
    def BtnImportEvent(self,event):
        wildcard = r"Excel files (*.xlsx)|*.xlsx|ALL Files (*.*)|*.*"  #|Data files (*.dat)|*.dat|Text files (*.txt)|*.txt|
        open_dlg = wx.FileDialog(self, message='Choose a file', defaultFile="cpkdata.xlsx", wildcard=wildcard, style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if open_dlg.ShowModal() == wx.ID_CANCEL:
            return     # the user changed their mind

        # Proceed loading the file chosen by the user
        pathname = open_dlg.GetPath()

        try:
            self.pd_data = pd.read_excel(pathname, usecols=[1, 2, 3, 4, 5,6])
            if self.pd_data is not None: 
                #print(self.pd_data)
                self.statusbar.SetStatusText(pathname)
                #self.MPL.ShowHelpString(pathname)
        except:
            dlg = wx.MessageDialog(self, 'Error opening file\n')
            dlg.ShowModal()
            dlg.Destroy()

        open_dlg.Destroy()
        
        # with wx.FileDialog(self, message='Choose a file', wildcard=wildcard,style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            # # ask the user what new file to open
            # if fileDialog.ShowModal() == wx.ID_CANCEL:
                # return     # the user changed their mind

            # # Proceed loading the file chosen by the user
            # pathname = fileDialog.GetPath()
            # try:
                # with open(pathname, 'r') as xlsx_file:
                    # self.pd_data = pd.read_excel(xlsx_file, usecols=[1, 2, 3, 4, 5,6])
                    
            # except IOError:
                # wx.LogError("Cannot open file '%s'." % pathname)
 
 
 
    # 自动创建状态栏 
    def StatusBar(self):
        self.statusbar = self.CreateStatusBar(2)
        #self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-7, -5]) 
        self.statusbar.SetStatusText('Field 1 here!')
        self.statusbar.SetStatusText('CPK Curve Tool V1.0 ,Copyright 2021, by Bob Cao(yongbo.cao@fluke.com)', 1)
        
 
    # About对话框 
    def AboutDialog(self):
        dlg = wx.MessageDialog(self,
                               '\tUsing wx + MatPlotLib\t\nAnd inherit from opensource:MPL_Panel_base,MPL_Panel,MPL_Frame and MPL2_Frame \n Created by Bob Cao\n Version 1.0.0 \n 2021-04-01',
                               'About CPK Tool', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
 
        ###############################################################################
 
 
###  MPL2_Frame添加了MPL_Panel的两个实例
###############################################################################
class MPL2_Frame(wx.Frame):
    """MPL2_Frame可以继承,并可修改,或者直接使用"""
 
    def __init__(self, title="MPL2_Frame Example In wxPython", size=(850, 500)):
        wx.Frame.__init__(self, parent=None, title=title, size=size)
 
        self.BoxSizer = wx.BoxSizer(wx.HORIZONTAL)
 
        self.MPL1 = MPL_Panel_base(self)
        self.BoxSizer.Add(self.MPL1, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.MPL2 = MPL_Panel_base(self)
        self.BoxSizer.Add(self.MPL2, proportion=-1, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.RightPanel = wx.Panel(self, -1)
        self.BoxSizer.Add(self.RightPanel, proportion=0, border=2, flag=wx.ALL | wx.EXPAND)
 
        self.SetSizer(self.BoxSizer)
 
        # 创建FlexGridSizer
        self.FlexGridSizer = wx.FlexGridSizer(rows=9, cols=1, vgap=5, hgap=5)
        self.FlexGridSizer.SetFlexibleDirection(wx.BOTH)
 
        # 测试按钮1
        self.Button1 = wx.Button(self.RightPanel, -1, "TestButton", size=(100, 40), pos=(10, 10))
        self.Button1.Bind(wx.EVT_BUTTON, self.Button1Event)
 
        # 测试按钮2
        self.Button2 = wx.Button(self.RightPanel, -1, "AboutButton", size=(100, 40), pos=(10, 10))
        self.Button2.Bind(wx.EVT_BUTTON, self.Button2Event)
 
        # 加入Sizer中
        self.FlexGridSizer.Add(self.Button1, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
        self.FlexGridSizer.Add(self.Button2, proportion=0, border=5, flag=wx.ALL | wx.EXPAND)
 
        self.RightPanel.SetSizer(self.FlexGridSizer)
 
        # 状态栏
        self.StatusBar()
 
        # MPL2_Frame界面居中显示
        self.Centre(wx.BOTH)
 
 
 
        # 按钮事件,用于测试
 
    def Button1Event(self, event):
        self.MPL1.cla()  # 必须清理图形,才能显示下一幅图
        x = np.arange(-5, 5, 0.2)
        y = np.cos(x)
        self.MPL1.plot(x, y, '--*g')
        self.MPL1.xticker(2.0, 1.0)
        self.MPL1.yticker(0.5, 0.1)
        self.MPL1.title_MPL("MPL1")
        self.MPL1.ShowHelpString("You Can Show MPL1 Helpful String Here !")
        self.MPL1.grid()
        self.MPL1.UpdatePlot()  # 必须刷新才能显示
 
        self.MPL2.cla()
        self.MPL2.plot(x, np.sin(x), ':^b')
        self.MPL2.xticker(1.0, 0.5)
        self.MPL2.yticker(0.2, 0.1)
        self.MPL2.title_MPL("MPL2")
        self.MPL2.grid()
        self.MPL2.UpdatePlot()
 
    def Button2Event(self, event):
        self.AboutDialog()
 
 
 
        # 自动创建状态栏
 
    def StatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-2, -2, -1])
 
 
        # About对话框
 
    def AboutDialog(self):
        dlg = wx.MessageDialog(self,
                               '\twxMatPlotLib\t\nMPL_Panel_base,MPL_Panel,MPL_Frame and MPL2_Frame \n Created by Wu Xuping\n Version 1.0.0 \n 2012-02-01',
                               'About MPL_Frame and MPL_Panel', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
 
 
 
 
        ########################################################################
 
 
# 主程序测试
if __name__ == '__main__':
    app = wx.App()
    #frame = MPL2_Frame()
    frame = MPL_Frame(title="CPK Curve Analyzer", size=(1000, 600))
    frame.SetIcon(wx.Icon("./title.ico"))
    frame.Center()
    frame.Show()
    app.MainLoop()