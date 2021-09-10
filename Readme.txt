##  How to package with pyinstaller

command terminal :cd current dir
pyinstaller -D CPKTool.py


## Version history:
### v1.0
- Draft , finish UI frame, curve 

### v1.1
 - Fix the parameter passing issue that caused the curve are all the same level sigma
   - cpk_calc function : for each curve should be passing just one <column data> ,not the<whole >df_frame.

### 2021/07/12
    Improvement： the auto screenshoot png file name is same as the standard point, not fixed as cpk1.png