# a CPK curve analysis tool
This is a CPK tool for Probability Density curve.Main Window：
![Main UI:](https://github.com/cyber211/CPKTool/blob/master/MAINUI.png)

## Main Function：
1. Import data from xlsx file， the format pls see cpkdata.xlsx for example;
2. According to STD,USL,LSL you filled, generate CPK curve for analysis:
  - ZOOM both for x and y axis;
  - rectangle zoom
  - SHIFT;
  - Save current figure as a .png file;
  
3. Will auto generate a screenshoot for the initial curve,named cpk1.png
screenshoots:
![Auto Generated picture:](https://github.com/cyber211/CPKTool/blob/master/cpk1.png)
![Save as picture:](https://github.com/cyber211/CPKTool/blob/master/image.png)

##  How to package with pyinstaller

command terminal :cd current dir
pyinstaller -D CPKTool.py


## Version history:
### v1.0
- Draft , finish UI frame, curve 

### v1.1
 - Fix the parameter passing issue that caused the curve are all the same level sigma
   - cpk_calc function : for each curve should be passing just one column data ,not the whole df_frame.