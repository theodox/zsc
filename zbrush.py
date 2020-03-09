# def Assert (test,  message):
# 	    """
# 	(ZScript debugging helper) aborts execution if specified condition is not true
# 	    """

def BackColorSet (Red, Green, Blue):
    """
    Sets the pen background color

    """

def ButtonFind (Interface item path, Button Text, Initially Disabled? (0=Enabled(ByDefault) NonZero=Disabled)):
    """
    Locates a ZBrush interface item

    """
    pass

def ButtonPress (Interface item path, Button Text, Initially Disabled? (0=Enabled(ByDefault) NonZero=Disabled)):
    """
    Locates and presses a ZBrush interface item

    """
    pass

def ButtonSet (Interface item path, Value, Button Text, Initially Disabled? (0=Enabled(ByDefault) NonZero=Disabled)):
    """
    Locates and sets a new value to a ZBrush interface item

    """
    pass

def ButtonUnPress (Interface item path, Button Text, Initially Disabled? (0=Enabled(ByDefault) NonZero=Disabled)):
    """
    Locates and unpresses a ZBrush interface item

    """
    pass

def CanvasClick (*positions):
    """
    Emulates a click within the current canvas area

    """
    pass

def CanvasGyroHide():
    """
    Hides the Transformation Gyro

    """
    pass

def CanvasGyroShow():
    """
    Shows the Transformation Gyro

    """
    pass

def CanvasPanGetH ():
    """
    Returns the H pan value of the active document view
    Output: The current H Pan value.

    """
    pass

def CanvasPanGetV ():
    """
    Returns the V pan value of the active document view
    Output: The current V Pan value.

    """
    pass

def CanvasPanSet (H_value , V_value):
    """
    Pans (Scrolls) the active document view

    """
    pass

def CanvasStroke (StrokeData, delayed, Rotation, HScale, VScale, HOffset, VOffset):
    """
    Emulates a brush stroke within the current canvas area

    """
    pass

def CanvasStrokes (StrokesData, Delayed, Rotation, HScale, VScale, HOffset, VOffset, HRotateCenter, VRotateCenter):
    """
    Emulates multiple brush strokes within the current canvas area

    """
    pass

def CanvasZoomGet ():
    """
    Returns the zoom value of the active document view
    Output: The current zoom value.
    """
    pass

def CanvasZoomSet (ZoomFactor):
    """
    Sets the zoom factor of the active document view

    """
    pass

def Caption (Text):
    """
    Displays a text line using the current Caption settings

    """
    pass

def CurveAddPoint (CurveIndex, XPos, YPos, ZPos):
    """
    Add a new point to the specified curve
    Output: Returns the point index (zero based) or -1 if failed.

    """
    pass

def CurvesCreateMesh (Name, Action, Thickness):
    """
    Creates a mesh from the current curves.

    Action values:
        0(default)=Append mesh to the active mesh,  
        1=Add as a new subtool,  
        2=Export OBJ file if does not exists,  
        3=Export Obj file and overwrite if exsits,

    Output: Returns the number of points in the new mesh. 
        zero=error, 1=file exists
    """
    pass

def CurvesDelete ():
    """
    Deletes named curves list.

    """
    pass

def CurvesNewCurve ():
    """
    Creates a new curve in the current curves list.
    Output: Returns the curve index (zero based) or -1 if failed.

    """
    pass

def CurvesNew ():
    """
    Creates a new curves list.

    """
    pass

def CurvesToUI ():
    """
    Copy the ZScript curves to UI
    Output: Returns zero of OK or -1 if failed.

    """
    pass

def Delay (DelaySeconds):
    """
    Delays execution of ZScript for specified amount of time

    """
    pass

def DispMapCreate (ImageWidth, ImageHeight, Smooth = 1, SubPoly = 0, Border=8, UVTile=0, UseHD=1):
    """
    Creates DisplacementMap
    Output: Returns zero if executed successfully. Any other value indicates an error

    """
    pass

def Exit():
    """
    Aborts execution and exits the current ZScript

    """
    pass

def FileDelete (FileName):
    """
    Delete specific file.
    Output: Returns zero if command executed successfully.

    """
    pass

def FileExecute (FileName, MethodName, Text="", Number="", InOutMem1=None, InOutMem2=None):
    """
    Executes the specified plugin file (DLL).
    Output: Returns the result value which was returned by the executed routine. Returns zero if error

    """
    pass

def FileExists (FileName):
    """
    Check if a specific file exists.
    Output: Returns 1 if file exists. Returns zero if does not exists

    """
    pass

def FileGetInfo (FileName, InfoIndex):
    """
    Retrieve information about a specified file.
    Output: Returns the requested information or zero if file not found.

    """
    pass

def FileNameAdvance (FileNameBase, NumDigits, AddCopyTag):
    """
    Increments the index value contained within a filename string  
    Output: Updated file Name

    """
    pass

def FileNameAsk (Extensions, DefaultName, DialogTitle):
    """
    Asks user for a file name
    If DefaultName is omitted, it's an Open dialog
    Output: Result file name or an empty string if user canceled operation.

    """
    pass

def FileNameExtract (FileName, Component):
    """
    Extracts filename components. Component of 1 = path, 2= name, 4 = extension
    Output: The extracted filename component/s.

    @todo: this should be more pythonic
    """
    pass

def FileNameGetLastTyped():
    """
    Retrieves the latest file name that was typed by the user in a Save/Load action
    Output: Latest file name that was typed by the user. Returned Variable will be empty if the user has canceled the action.

    """
    pass

def FileNameGetLastUsed():
    """
    Retrieves the latest file name that was used (by the user or by ZBrush) in a Save/Load action
    Output: Latest file name that was used. Returned Variable will be empty if the user has canceled the action.

    """
    pass

def FileNameGetNext():
    """
    Get the preset file name that will be used in the next Save/Load action,  if it has been preset
    Output: File name that will be used in the next Save/Load action. Returned Variable will be empty if no next file name is preset.

    """
    pass


def FileNameHasNext():
    """
    Test if the preset file name that will be used in the next Save/Load action have been set or not
    Output: Returns 1 if next file name has been set,  0 otherwise.

    """
    pass

def FileNameMake (Base file name, Index, Number of numeric digits to use):
    """
    Combines a base filename with an index number
    Output: Combined file name Variable

    """
    pass

def FileNameResolvePath (LocalFileName):
    """
    Resolves local path to full path
    Output: Full path.

    """
    pass

def FileNameSetNext (FileName, TemplatePath = None):
    """
    Pre-sets the file name that will be used in the next Save/Load action
    """
    pass


def FileTemplateGetNext():
    """
    Get the preset template file name that will be used in the next Save/Load action,  if it has been preset
    Output: Template file name that will be used in the next Save/Load action. Returned Variable will be empty if no next template file name is preset.

    """
    pass

def FontSetColor (Red, Green, Blue):
    """
    Sets the color of the text-flow font

    """
    pass

def FontSetOpacity (Opacity):
    """
    Sets the opacity of the text-flow font

    """
    pass

def FontSetSize(Size):    
    """
    Sets the intensity of the text-flow font
    :1=Small 2=Med 3=Large
    """
    pass

def FontSetSizeLarge():
    """
    Sets the size of the text-flow font to large
    """
    pass

def FontSetSizeMedium():
    """
    Sets the size of the text-flow font to medium

    """
    pass

def FontSetSizeSmall():
    """
    Sets the size of the text-flow font to small

    """
    pass

def FrontColorSet (Description, Red, Green, Blue, Disabled =0):
    """
    Sets the main interface color to a new value

    """
    pass


def  GetActiveToolPath():
    """
    Returns the full path of the active tool
    Output: The path of the active tool
    """
    pass


def GetPolyMesh3DVolume():
    """
    Get the volume of current PolyMesh3D SubTool
    Output: Returns the Volume of current PolyMesh3D SubTool,  or 0 if not a PolyMesh3D. Note: if PolyMesh3D is NOT a valid volume,  then resulting value may be not accurate.

    """
    pass

def HotKeyText (InterfacePath):
    """
    Displays a hot-key for the specified interface item
    """
    pass


def IButton (ButtonText, PopupText, commands, Disabled=0, Width=0, Hotkey='', Icon='', Height=0):
    """
    Creates an interactive push button

    """
    pass


def IClick (InterfacePath, *positions):
    """
    Emulates a click within a specified ZBrush interface item

    """
    pass


def IClose (InterfacePath, ShowZoom=0, TargetParent=0):
    """
    Closes an interface item.

    """
    pass


def IColorSet (Red (0-255), Green (0-255), Blue (0-255)):
    """
    Sets the active color to a new value

    """
    pass


def IConfig (ZBrush version-configuration (1.232=v1.23b,  1.5=v1.5 and newer.) ):
    """
    Sets ZBrush internal version-configuration

    """
    pass


def IDialog (Title, TitleMode=0, Icon='', LeftInset=0, RightInset=0, LeftTop=0, RightBottom=0): (0=default)
    """
    Adds a subpalette to ZBrush interface.
    Mode :
     mode? (0=Show Title and minimize button(ByDefault) 1=Show Title without minimize button 2=Hide Title )
    
    Icon:  Optional subpalette gray-scale (8-bits) icon (Standrad size of 20x20 pixels)

    Output: Returns 1 if subpalette added succesfuly. Returns 0 if subpalette could not be added or if it already exsists.

    """
    pass

def IDisable (Window path, Window ID or relative windowID(-100<->100)):
    """
    Disables a ZScript interface item (can only be used for ZScript-generated interface items)

    """
    pass

def IEnable (Window path, Window ID or relative windowID(-100<->100)):
    """
    Enables a ZScript interface item (can only be used for ZScript-generated interface items)

    """
    pass

def IExists (Interface item path):
    """
    Verifies that a specified interface item exists.
    Output: 1 if item exists, 0 otherwise

    """
    pass

def If (True Or False Evaluation, Commands group to be executed if true  (not zero), Commands group to be executed if false (is  zero)):
    """
    Provides conditional execution of a commands group

    """
    pass

def IFadeIn (Fade out speed in secs. (default=.5 secs) ):
    """
    Fades ZBrush window to black.

    """
    pass

def IFadeOut (Fade out speed in secs. (default=.5 secs) ):
    """
    Fades ZBrush window to black.

    """
    pass

def IFreeze (Commands group to be executed without updating the interface, Fade out speed in secs. (default=.5 secs) ):
    """
    Disables interface updates.

    """
    IGet, Interface item path
    """
    Returns the current value of a ZBrush or ZScript interface item
    Output: The item value

    """
    pass

def IGetFlags (Interface item path):
    """
    Returns the status flags of the specified interface item
    Output: The flags

    """
    pass

def IGetHotkey (Interface item path):
    """
    Returns the hotkey of the specified interface item
    Output: The Hotkey

    """
    pass

def IGetID (Interface item path):
    """
    Returns the window ID code of the specified interface item
    Output: The Title

    """
    pass

def IGetInfo (Interface item path):
    """
    Returns the info (popup info) of the specified interface item
    Output: The info

    """
    pass

def IGetMax (Interface item path):
    """
    Returns the maximum possible value of a ZBrush or ZScript interface item
    Output: The item maximum value

    """
    pass

def IGetMin (Interface item path):
    """
    Returns the minimum possible value of a ZBrush or ZScript interface item
    Output: The item minimum value

    """
    pass

def IGetSecondary (Interface item path):
    """
    Returns the the scondary value of a 2D interface item
    Output: The item value

    """
    IGetStatus, Interface item path
    """
    Returns the Enabled/Disabled status of a ZBrush or ZScript interface item
    Output: The item status
  0=Disabled
  1=Enabled

    """
    pass

def IGetTitle (Interface item path, Return full path? (0=no nonZero=yes)):
    """
    Returns the title of the specified interface item
    Output: The Title of the button

    """
    pass

def IHeight (Interface item path):
    """
    Returns the pixel-height of an interface item.
    Output: The height of the interface item.

    """
    pass

def IHide (Interface item path, Show Zoom Rectangles?, Target parent window?):
    """
    Hides an interface item.

    """
    pass

def IHPos (Interface item path, Global coordinates? set value to non-zero for global coordinates,  default=Canvas coordinates.):
    """
    Returns the H position of the interface item in Canvas or Global coordinates.
    Output: The H position of the interface item.

    """
    pass

def IKeyPress (The key to press with an optional CTRL/CMD,  ALT/OPT,  SHIFT or TAB combination. , Commands group to execute while the key is pressed, Optional H cursor position prior to key press, Optional V cursor position prior to key press):
    """
    Simulates a key press

    """
    pass

def ILock (Window path, Window ID or relative windowID(-100<->100)):
    """
    Locks an interface item 

    """
    pass

def Image (FileName (.psd .bmp  ), Align (0=center 1=left 2=right), Resized Width):
    """
    Loads and displays an image

    """
    IMaximize, Interface item path, Maximizeall sub palettes? (0=no,  NonZero=yes)
    """
    Locates an interface item and (if possible) maximize its size.

    """
    pass

def IMinimize (Interface item path, Minimize all sub palettes? (0=no,  NonZero=yes)):
    """
    Locates an interface item and (if possible) minimize its size.

    """
    pass

def IModGet (Interface item path):
    """
    Returns the current modifiers binary state of a ZBrush or ZScript interface item
    Output: The item value

    """
    pass

def IModSet (Interface item path, value):
    """
    Sets the modifiers binary value of a ZBrush or a ZScript interface item

    """
    pass

def Interpolate (Time (0=AtStart 0.5=half 1=AtEnd)	, Value1 (Num,  VarName or ListName), Value2 (Num,  VarName or ListName), Value3 (Num,  VarName or ListName), Value4 (Num,  VarName or ListName), Angle interpolation (0=no(default),  1=yes )):
    """
    Performs time-based interpolation
    Output: Interpolated value or list

    """
    pass

def IPress (Interface item path):
    """
    Presses a ZBrush or ZScript interface item

    """
    pass

def IReset (Optional item to reset (default=All). 0=All, 1=Interface, 2=Document, 3=Tools, 4=Lights, 5=Materials, 6=Stencil, Optional ZBrush version-configuration (default=1.5. if omitted,  configuration will default to version 1.23b )):
    """
    Interface Reset
    Output: Returns the button that the user clicked. ( 0=NO,  1=YES )

    """
    pass

def IsDisabled (Interface item path):
    """
    Returns 1 if the specified ZBrush or ZScript interface item is currently disabled,  returns 0 otherwise
    Output: The item 'Disabled' status (1=Disabled 0=Enabled)

    """
    pass

def IsEnabled (Interface item path):
    """
    Returns 1 if the specified ZBrush or ZScript interface item is currently enabled,  returns 0 otherwise
    Output: The item 'Enabled' status (1=Enabled 0=Disabled)

    """
    pass

def ISet (Interface item path, value, Secondary value):
    """
    Sets a new value to a ZBrush or ZScript interface item

    """
    pass

def ISetHotkey (Interface item path, Hotkey  (0=no Hotkey)):
    """
    Sets the hotkey of the specified interface item

    """
    pass

def ISetMax (Interface item path, New max value ):
    """
    Sets the maximum value for an ISlider interface item (can only be used for ZScript-generated interface items)

    """
    ISetMin, Interface item path, New min value 
    """
    Sets the minimum value for an ISlider interface item (can only be used for ZScript-generated interface items)

    """
    pass

def ISetStatus (Interface item path, New status ( 0=Disable NotZero=Enable )):
    """
    Enables or Disables a ZScript interface item (can only be used for ZScript-generated interface items)

    """
    pass

def IShowActions (The ShowActions status. 0=Disable ShowActions,  Positive value=enable show actions,  Negative value=Reset ShowActions ):
    """
    Temorarily sets the status of ShowActions

    """
    pass

def IShow (Interface item path, Show Zoom Rectangles?, Target parent window?):
    """
    Locates an interface item and makes it visible.

    """
    pass

def ISlider (Slider Text, CurValue, Resolution, MinValue, MaxValue, Popup info Text, Commands group to execute when value is changed, Initially Disabled? (0=Enabled(ByDefault) NonZero=Disabled), Button width in pixels (0=AutoWidth NonZero=Specified width)):
    """
    Creates an interactive slider

    """
    pass

def IsLocked (Interface item path):
    """
    Returns 1 if the specified ZBrush or ZScript interface item is currently locked,  returns 0 otherwise
    Output: The item 'Locked' status (1=Locked 0=Unlocked)

    """
    IsPolyMesh3DSolid
    """
    Tests if current PolyMesh3D is a Solid
    Output: Returns 1 if current PolyMesh3D is a valid Solid,  0 otherwise.

    """
    pass

def IStroke (Interface item path, StrokeData):
    """
    Emulates a brush stroke within an interface item

    """
    pass

def ISubPalette (Subpalette name, Title mode? (0=Show Title and minimize button(ByDefault) 1=Show Title without minimize button 2=Hide Title ), Optional subpalette gray-scale (8-bits) icon (Standrad size of 20x20 pixels), Left Inset (0=default), Right Inset (0=default), Left Top (0=default), Right Bottom (0=default)):
    """
    Adds a subpalette to ZBrush interface.
    Output: Returns 1 if subpalette added succesfuly. Returns 0 if subpalette could not be added or if it already exsists.

    """
    IsUnlocked, Interface item path
    """
    Returns 1 if the specified ZBrush or ZScript interface item is currently unlocked,  returns 0 otherwise
    Output: The item 'Unlocked' status (1=Unlocked 0=locked)

    """
    pass

def ISwitch (Button Text, Initial state (1=pressed, 0=unpressed), Popup info Text, Commands group to execute when button is pressed, Commands group to execute when button is unpressed, Initially Disabled? (0=Enabled(ByDefault) NonZero=Disabled), Button width in pixels (0=AutoWidth NonZero=Specified width)):
    """
    Creates an interactive switch

    """
    pass

def IToggle (Interface item path):
    """
    Toggles the state of a ZBrush or ZScript interface item

    """
    pass

def IUnlock (Window path, Window ID or relative windowID(-100<->100)):
    """
    Unlocks an interface item

    """
    pass

def IUnPress (Interface item path):
    """
    Unpresses a ZBrush or ZScript interface item

    """
    pass

def IUpdate (Repeat count (default=1), Redraw UI? (default==no,  1=yes)):
    """
    Updates the ZBrush interface.

    """
    pass

def IVPos (Interface item path, Global coordinates? set value to non-zero for global coordinates,  default=Canvas coordinates.):
    """
    Returns the V position of the interface item in Canvas or Global coordinates.
    Output: The V position of the interface item.

    """
    pass

def IWidth (Interface item path):
    """
    Returns the pixel-width of an interface item.
    Output: The width of the interface item.

    """
    pass

def Loop (RepeatCount, Commands group, Optional loop-counter variable (starts at Zero)):
    """
    Repeats execution of the specified commands group

    """
    LoopContinue
    """
    Continues execution from the beginning of the current Loop

    """
    LoopExit
    """
    Exits the current Loop

    """
    pass

def MemCopy (From Mem block identifier., From offset, To Mem block identifier., To offset, Number of bytes to move. (If omited,  max possible number of bytes will be copied)):
    """
    Copies data from one memory block into another.
    Output: Returns the mumber of bytes moved. (-1 indicates an error)

    """
    pass

def MemCreate (Mem block identifier., Mem block requested size., Initial fill? (omited=noFill=faster to create)):
    """
    Creates a new memory block.
    Output: Returns the size of the new memory block or error code...0=Error -1=Memory already exists -2=Can't create memory block.

    """
    pass

def MemCreateFromFile (Mem blMessageOKock identifier., File name including the extension (such as brush1.ztl )., Optional start file offset for partial file read. (Default=0), Optional max bytes to read. (Default=all file)):
    """
    Creates a new memory block from a disk file.
    Output: Returns the size of the new memory block or error code...0=Error -1=Memory already exists -2=Can't create memory block -3=File not found.

    """
    pass

def MemDelete (Data block identifier.):
    """
    Deletes a memory block.
    Output: Returns the size of the deleted memory block. Returns 0 if memory block could not be found.

    """
    pass

def MemGetSize (Memory block identifier.):
    """
    Returns the size of a memory block (Also useful for determining if a memory block already exists
    Output: Returns the size of the memory block. Returns 0 if data block could not be found.

    """
    pass

def MemMove (Mem block identifier., From offset, To offset, Number of bytes to move):
    """
    Move data within an existing memory block.
    Output: Returns the mumber of bytes moved.

    """
    pass

def MemMultiWrite (Mem block identifier., Value to write., Data format (0=omited=float,  1=signed char, 2=unsigned char, 3=signed short, 4=unsigned short, 5=signed long, 6=unsigned long, 7=fixed16 (16.16), Offset (in bytes) into memory block., Repeat count, Offset (in bytes) to subsequent writes):
    """
    Write data to a memory block.
    Output: Returns the number of actual bytes written

    """
    MemRead, Mem block identifier., Read variable., Data format (0=omited=float,  1=signed char, 2=unsigned char, 3=signed short, 4=unsigned short, 5=signed long, 6=unsigned long, 7=fixed16 (16.16), Offset (in bytes) into memory block.
    """
    Reads data from a memory block.
    Output: Returns the number of actual bytes read

    """
    pass

def MemReadString (Mem block identifier., The string variable., Offset (in bytes) into memory block., Break at line end? (default=no), Skip white space? (default=no), Max read length 1 - 255(default).):
    """
    Reads a string from a memory block.
    Output: Returns the number of bytes scanned. (may be larger than the actual bytes read)

    """
    pass

def MemResize (Mem block identifier., New size., Optional byte value to fill the newly added memory? (omited=no)):
    """
    Resizes an exsiting memory block.
    Output: Returns the new size of the memory block. Zero indicates an error.

    """
    pass

def MemSaveToFile (Mem block identifier., File name including the extension (such as brush1.ztl )., Overwrite if exists? Set to nonzero value to save the file even if an identically named file already exists on disk. Default=Do not overwrite.):
    """
    Saves an exisiting memory block to a disk file.
    Output: Returns the size of the new memory block or error code...0=Error -1=Memory does not exists -2=File already exits -3=File write error.

    """
    pass

def MemWrite (Mem block identifier., Value to write., Data format (0=omited=float,  1=signed char, 2=unsigned char, 3=signed short, 4=unsigned short, 5=signed long, 6=unsigned long, 7=fixed16 (16.16), Offset (in bytes) into memory block.):
    """
    Write data to a memory block.
    Output: Returns the number of actual bytes written

    """
    pass

def MemWriteString (Mem block identifier., The string ., Offset (in bytes) into memory block., Write terminating zero char (if omited=yes)):
    """
    Writes a string into a memory block.
    Output: Returns the number of bytes written. (including the terminating zero)

    """
    MergeUndo
    """
    Merge the next undo with the previous undo.

    """
    Mesh3DGet, Property: 0=PointsCount, 1=FacesCount, 2=XYZ bounds, 3=UVBounds, 4=1stUVTile, 5=NxtUVTile, 6=PolysInUVTile, 7=3DAreaOfUVTile, 8=Full3DMeshArea, Optional input 1 Vertix/Face/Group/UVTile H index (0 based), Optional input 2, Optional output variable1., Optional output variable2., Optional output variable3., Optional output variable4., Optional output variable5., Optional output variable6., Optional output variable7., Optional output variable8.
    """
    Gets information about the currently active  Mesh3D tool.
    Output: Returns zero if command executed successfully,  any other value indicates and error.

    """
    pass

def MessageOK (The Message that will be shown, The Title of the message):
    """
    Displays a user message with a single OK button

    """
    pass

def MessageOKCancel (The Message that will be shown, The Title of the message):
    """
    Displays a user message with CANCEL and OK buttons
    Output: Returns the button that the user clicked. (0=CANCEL,  1=OK)

    """
    pass

def MessageYesNo (The Message that will be shown, The Title of the message):
    """
    Displays a user message with YES and NO buttons
    Output: Returns the button that the user clicked. (0=NO,  1=YES)

    """
    pass

def MessageYesNoCancel (The Message that will be shown, The Title of the message):
    """
    Displays a user message with YES,  NO and CANCEL buttons
    Output: Returns the button that the user clicked. (0=NO,  1=YES CANCEL=-1)

    """
    pass

def MouseHPos (Global coordinates? set value to non-zero for global coordinates,  default=Canvas coordinates.):
    """
    Returns the current H position of the mouse in Canvas or Global coordinates.
    Output: The H position of the mouse

    """
    MouseLButton
    """
    Returns the current state of the left mouse button 
    Output: Returns 1 if mouse button is pressed,  returns zero if unpressed

    """
    pass

def MouseVPos (Global coordinates? set value to non-zero for global coordinates,  default=Canvas coordinates.):
    """
    Returns the current V position of the mouse in Canvas or Global coordinates.
    Output: The V position of the mouse

    """
    pass

def MTransformGet (Mem block identifier., Optional variable index (default=0).):
    """
    Gets current transformation values into an existing memory block

    """
    pass

def MTransformSet (Mem block identifier., Optional variable index (default=0).):
    """
    Sets new transformation values from an existing memory block.

    """
    MVarDef, Mem block identifier., Mem block variables count., Initial fill? (omited=noFill=faster to create)
    """
    pass

    defines a new variables memory block.
    Output: Returns the variables count of the new memory block or error code...0=Error -1=Memory already exists -2=Can't create memory block.

    """
    pass

def MVarGet (Mem block identifier., Variable index (0 based).):
    """
    Reads a float value from a memory block.
    Output: Returns the float value.

    """
    pass

def MVarSet (Mem block identifier., Variable index (0 based)., The value to write.):
    """
    Writes a float value to a memory block.
    Output: Returns the old value of the variable.

    """
    pass

def NormalMapCreate (Image Width, Image Height, Smooth (default=yes), SubPoly (default=0), Border (default=8), UVTile index (default=ignores UV tiles), Local(tangent) coordinates? (default=world coordinates)):
    """
    Creates NormalMap
    Output: Returns zero if executed successfully. Any other value indicates an error

    """
    pass

def Note (Text line, Optional path1 of an interface item to be pointed out. (default=none), Display Duration (in seconds). (zero= wait for user action,  -1=combine with next note command). (default=wait action), Popup background color. (  0x000000<->0xffffff,  default=0x606060,  0=NoBackground ), Prefered distance of the note from the specified interface item (default=48), Prefered Note width (in pixels,  default=400), optional marked windows fill color. ( 0x000000<->0xffffff  or blue + (green*256) + (red*65536) ) (Omitted value=No fill)  ), Frame horizontal size ( 1= (default) Max width ), Frame vertical size ( 1=(default) Max height ), Frame left side ( 0=left (default) ,  .5=center,  1=right ). Omit value for horizontal autocentering., Frame top side ( 0=top (default) ,  .5=center,  1=bottom ) Omit value for vertical auto-centering., Optional icon file name.):
    """
    Displays a note to the user.
    Output: If the note has UI buttons then the return value of the pressed buttons (1=1st button,  2=2nd button ...),  otherwise the return value will be zero.

    """
    pass

def NoteBar (The Message that will be shown (use empty string to clear current note), Optional progress-bar value (0=Min,  1=Max)):
    """
    Displays a note in progress bar.

    """
    pass

def NoteIButton (Button text, Optional button icon, Initially Pressed ?  (default=unpressed), Initially Disabled ? (default=enabled), Optional button H relative position. (Positive value=offset from left,  Negative value=offset from right,  0=automatic), Optional button V relative position. (Positive value=offset from top,  Negative value=offset from bottom,  0=automatic), Optional button width in pixels (default=automatic), Optional button height in pixels (default=automatic), Optional button color  0x000000<->0xffffff (blue + (green*256) + (red*65536) ) , Optional text color  0x000000<->0xffffff  (blue + (green*256) + (red*65536) ) , Optional background opacity (default=1) , Optional text opacity (default=1) , Optional image opacity (default=1) ):
    """
    pass

    defines a button to be included within the next Note to be shown.

    """
    pass

def NoteIGet (Note-button index (1=1st) or its name):
    """
    Returns the value of am NoteIButton which was shown in the last displayed Note.
    Output: The item value

    """
    NoteISwitch, Button text, Optional button icon, Initially Pressed ?  (default=unpressed), Initially Disabled ? (default=enabled), Optional button H relative position. (Positive value=offset from left,  Negative value=offset from right,  0=automatic), Optional button V relative position. (Positive value=offset from top,  Negative value=offset from bottom,  0=automatic), Optional button width in pixels (default=automatic), Optional button height in pixels (default=automatic), Optional button color  0x000000<->0xffffff (blue + (green*256) + (red*65536) ) , Optional text color  0x000000<->0xffffff  (blue + (green*256) + (red*65536) ) , Optional background opacity (default=1) , Optional text opacity (default=1) , Optional image opacity (default=1) 
    """
    pass

    define a switch-button to be included within the next Note to be shown.

    """
    pass

def PageSetWidth (Preferred PageWidth):
    """
    Sets the width of the page

    """
    pass

def PaintBackground (Red, Green, Blue):
    """
    Paints the background using the current background color

    """
    pass

def PaintBackSliver (height, Red, Green, Blue):
    """
    Draws a full page-width rectangle using the current background color

    """
    PaintPageBreak
    """
    Draws a visual page-break

    """
    pass

def PaintRect (Width, height, Red, Green, Blue):
    """
    Draws a rectangle (in the ZScript window) using the current pen color

    """
    pass

def PaintTextRect (Width, Height, Text):
    """
    Draws a rectangle with imbedded text

    """
    PD
    """
    Moves the pen position to the beginning of the next line (Same as PenMoveDown)

    """
    PenMoveCenter
    """
    Moves the pen position to the horizontal center of the page

    """
    PenMoveDown
    """
    Moves the pen position to the beginning of the next line

    """
    PenMoveLeft
    """
    Moves the pen position to the left side of the page

    """
    PenMoveRight
    """
    Moves the pen position to the right side of the page

    """
    pass

def PenMove (Horizontal Offset, Vertical Offset):
    """
    Moves the pen a relative distance

    """
    pass

def PenSetColor (Red, Green, Blue):
    """
    Sets the pen main color

    """
    PixolPick, Component Index. 0=CompositeColor ( 0x000000<->0xffffff  or red*65536+green*256+blue) 1=Z(-32576 to 32576) 2=Red(0 to 255 ) 3=Green(0 to 255 ) 4=Blue(0 to 255 )  5=MaterialIndex(0 to 255 ) 6=XNormal(-1 to 1) 7=YNormal(-1 to 1) 8=ZNormal(-1 to 0) , H Position, V Position
    """
    Retrieves information about a specified Pixol
    Output: The value of the specified Pixol

    """
    pass

def PropertySet (The base command name (Title, SubTitle, Caption), Property Index, The new Value):
    """
    Modifies the setting of Title,  SubTitle and Caption text

    """
    pass

def Randomize (Optional sid value (0 to 32767)):
    """
    Resets the Rand generator.

    """
    pass

def RGB (Red, Green, Blue):
    """
    Combines 3 color-components into one RGB value
    Output: Combined RGB

    """
    pass

def RoutineCall (Name of the routine to be called, Input Var01, Input Var02, Input Var03, Input Var04, Input Var05, Input Var06, Input Var07, Input Var08, Input Var09, Input Var10):
    """
    Executes the specified defined routine

    """
    pass

def RoutineDef (Name of the routine, Commands group that will be executed when the routine is called, Input Var01, Input Var02, Input Var03, Input Var04, Input Var05, Input Var06, Input Var07, Input Var08, Input Var09, Input Var10):
    """
    pass

    defines a named commands group

    """
    pass

def SectionBegin (Section Title, Initial state (1=Expanded, 0=Collapsed ), Popup Info Text, Commands group to execute when expanding to reveal content, Commands group to execute when collapsing to hide content, Initially Disabled? (0=Enabled(ByDefault) NonZero=Disabled)):
    """
    Begins a collapsible section

    """
    SectionEnd
    """
    Ends a collapsible section

    """
    pass

def ShellExecute (The shell command):
    """
    Execute a shell command

    """
    Sleep, Sleep amount in seconds., Commands group to execute when awaken., Optional event (default=1) (1=Timer, 2=Mouse Moved, 4=LButton down, 8=LButton up, 16=KeyDown, 32=keyUp, 64=ModifierKeyDown, 128=ModifierKeyUp, 256=Startup, 512=Shut down, 1024 InterfaceItem pressed/unpressed, 2048 tool selected, 4096 texture selected,  8192 alpha sele, Optional output variable which will contain the event code that has awaken the ZScript, Optional output variable which will contain the ID of the window pointed by the mouse.
    """
    Exists ZScript and be awaken by specified event.

    """
    pass

def SleepAgain (Optional new Sleep amount in seconds (default=unchanged), Optional event (default=unchanged) (1=Timer, 2=Mouse Moved, 4=LButton down, 8=LButton up, 16=KeyDown, 32=keyUp, 64=ModifierKeyDown, 256=Startup, 512=Shut down, 1024 InterfaceItem post pressed/unpressed, 2048 tool selected, 4096 texture selected,  8192 alpha selected, ):
    """
    Exists ZScript and continues the Sleep command.

    """
    pass

def SoundPlay (Mem block identifier., Oprional play mode. 0=default=Play once,  dont wait for completion. 1=Play once,  wait for completion. 2=Play loop,  dont wait for completion.):
    """
    Plays the sounds loaded into a specified memory block.
    Output: Returns the zero if command executed successfully.

    """
    pass

def SoundStop (Mem block identifier.):
    """
    Stops the currently specified sound.
    Output: Returns the zero if command executed successfully.

    """
    pass

def StrAsk (Optional initial string, Optional title):
    """
    Asks user to input a string.
    Output: Returns the text typed by user or an empty string if canceled.

    """
    pass

def StrExtract (Input string, Start character index (0=left), End character index (0=left)):
    """
    Returns specified portion of the input string
    Output: The extracted portion of the input string.

    """
    pass

def StrFind (find this string, in this string, Optional start search index (default=0)):
    """
    Locate a string within a string.
    Output: Returns the starting index of the 1st string within the 2nd string. returns -1 if not found.

    """
    pass

def StrFromAsc (Input Ascii value):
    """
    Returns the character of the specified Ascii value.
    Output: The character of the specified Ascii value.

    """
    pass

def StrLength (String to evaluate):
    """
    Returns the number of characters in the input string.
    Output: Number of characters in the input string.

    """
    pass

def StrLower (Input string):
    """
    Returns the lowercase version of the input string.
    Output: The lowercase version of the input string.

    """
    pass

def StrMerge (Str 1, Str 2, Optional Str 3, Opt Str 4, Opt Str 5, Opt Str 6, Opt Str 7, Opt Str 8, Opt Str 9, Opt Str 10, Opt Str 11, Opt Str 12):
    """
    Combines two (or more) strings into one string.
    Output: The combined string. Note: result string will not exceed 255 characters in length 

    """
    pass

def StrokeGetInfo (Stroke-type Variable, Info number, Point index (0 based)):
    """
    Retrieves the information from a specified Stroke-type Variable
    Output: StrokeInfo result

    """
    StrokeGetLast
    """
    Retrieves the last drawn brush stroke
    Output: StrokeData

    """
    pass

def StrokeLoad (FileName (.txt)):
    """
    Loads a brush-stroke text file
    Output: StrokeData

    """
    pass

def StrokesLoad (FileName (.txt)):
    """
    Loads a brush-strokes text file
    Output: StrokesData

    """
    pass

def StrToAsc (Input string, Optional character offset (default=0)):
    """
    Returns the Ascii value of a character.
    Output: The Ascii value of a character.

    """
    pass

def StrUpper (Input string):
    """
    Returns the uppercase version of the input string.
    Output: The uppercase version of the input string.

    """
    pass

def SubTitle (Text):
    """
    Displays a text line using the current SubTitle settings

    """
    SubToolGetActiveIndex
    """
    Returns the index of the active subtool
    Output: Returns the index of the active subtool (zero based).

    """
    SubToolGetCount
    """
    Returns the number of subtools in the active tool
    Output: Returns the number of subtools.  Return 0 if error.

    """
    pass

def SubToolGetFolderIndex (Subtool Index (zero based).  If omited then use the currently selected subtool.):
    """
    Returns the folder index in which this subtool is contained
    Output: Returns the foldr index or -1 if this subtool is not within a folder.

    """
    pass

def SubToolGetFolderName (Tool Index (zero based). If omited then use the currently selected tool.):
    """
    Returns the ffolder name of the specified subtool
    Output: Result folder name or empty if subtool is not in a folder.

    """
    pass

def SubToolGetID (Subtool Index (zero based).  If omited then use the currently selected subtool.):
    """
    Returns the unique subtool ID
    Output: Returns the unique subtool ID or zero if error.

    """
    pass

def SubToolGetStatus (Subtool Index (zero based).  If omited then use the currently selected subtool.):
    """
    Returns the status of a subtool
    Output: Returns the status (Subtool Eye=0x01,  Folder Eye=0x02, UnionAdd=0x10, UnionSub=0x20, UnionClip=0x40, UnionStart=0x80, ClosedFolder=0x400, OpenedFolder=0x800) .

    """
    pass

def SubToolLocate (Unique Subtool ID):
    """
    Locates a subtool by the specified unique ID
    Output: Returns the index of the located subtool or -1 if error.

    """
    pass

def SubToolSelect (Subtool Index (zero based).):
    """
    Selects the specified subtool index
    Output: Returns zero if OK,  -1 if error.

    """
    pass

def SubToolSetStatus (Subtool Index (zero based).  If omited then use the currently selected subtool., New Value (Subtool Eye=0x01, Folder Eye=0x02, UnionAdd=0x10, UnionSub=0x20, UnionClip=0x40, UnionStart=0x80, ClosedFolder=0x400, OpenedFolder=0x800)):
    """
    Sets the status of a subtool

    """
    pass

def TextCalcWidth (The text to be evaluated):
    """
    Calculates the pixel-width of the specified string
    Output: Width of text in pixels

    """
    pass

def Title (Text):
    """
    Displays a text line using the current Title settings

    """
    pass

def TLDeleteKeyFrame (Key Frame Index):
    """
    Delete specified key frame index of the active track
    Output: Returns the number of available key frames

    """
    TLGetActiveTrackIndex
    """
    Returns the index of the active track
    Output: Returns the current active track index -1=None 

    """
    TLGetKeyFramesCount
    """
    Returns the total number of key frames in the active track
    Output: Returns the number of key frames in the active track 0=None 

    """
    pass

def TLGetKeyFrameTime (Key Frame Index):
    """
    Get the time of the specified key frame index of the active track
    Output: Returns the time of the selected key frame or -1 if error.

    """
    TLGetTime
    """
    Returns the current TimeLine knob position in  0.0 to 1.0 range
    Output: Returns the current TimeLine knob time 0=start,  1=end

    """
    pass

def TLGotoKeyFrameTime (Key Frame Index):
    """
    Move TimeLine knob position to specified key frame index of the active track
    Output: Returns the time of the selected key frame or -1 if error.

    """
    pass

def TLGotoTime (Time 0.0 to 1.0 range.):
    """
    Sets the current TimeLine knob position in  0.0 to 1.0 range
    Output: Returns zero if OK,  -1 if error.

    """
    pass

def TLNewKeyFrame (Optional time (if omited then use current time)):
    """
    Create a new key frame in the active track
    Output: Returns the new key frame index or -1 if error.

    """
    pass

def TLSetActiveTrackIndex (Track Index 0=main track):
    """
    Sets the active track index
    Output: Returns zero if OK,  -1 if error.

    """
    pass

def TLSetKeyFrameTime (Key Frame Index, Time 0.0 to 1.0 range.):
    """
    Set the time of the specified key frame index of the active track
    Output: Returns the new key frame index or -1 if error.

    """
    ToolGetActiveIndex
    """
    Returns the index of the active tool
    Output: Returns the index of the active tool (zero based).

    """
    ToolGetCount
    """
    Returns the number of available tools
    Output:  Returns the number of available tools.

    """
    pass

def ToolGetPath (Tool Index (zero based). If omited then use the currently selected tool.):
    """
    Returns the file path or name of the specified tool
    Output: Result path (without the .ztl). Empty if error.

    """
    pass

def ToolGetSubToolID (Tool Index (zero based).  If omited then use the currently selected tool., Subtool Index (zero based).  If omited then use the selected subtool.):
    """
    Returns the unique subtool ID
    Output: Returns the unique subtool ID or zero if error.

    """
    pass

def ToolGetSubToolsCount (Tool Index (zero based). If omited then use the currently selected tool.):
    """
    Returns the number of subtools in the specified tool index
    Output: Returns the number of subtools.  Return 0 if error.

    """
    pass

def ToolLocateSubTool (Unique Subtool ID, Optional subtool index result):
    """
    Locates a subtool by the specified unique ID
    Output: Returns the index of the located tool and subtool or -1 if error.

    """
    pass

def ToolSelect (Tool Index (zero based).):
    """
    Selects the specified tool index
    Output: Returns zero if OK,  -1 if error.

    """
    pass

def ToolSetPath (Tool Index (zero based). If omited then use the currently selected tool., New Path. Path extension (such as .ztl) will be omited.):
    """
    Sets the file path or name of the specified tool
    Output: Returns zero if OK,  -1 if error.

    """
    pass

def TransformGet (xPos, yPos, zPos, xScale, yScale, zScale, xRotate, yRotate, zRotate):
    """
    Gets current transformation values.

    """
    pass

def TransformSet (xPos, yPos, zPos, xScale, yScale, zScale, xRotate, yRotate, zRotate):
    """
    Sets new transformation values.

    """
    pass

def TransposeGet (Start xPos, Start yPos, Start zPos, End xPos, End yPos, End zPos, Action Line Length, x of red axis, y of red axis, z of red axis, x of green axis, y of green axis, z of green axis, x of blue axis, y of blue axis, z of blue axis):
    """
    Gets current Transpose Action Line values.

    """
    TransposeIsShown
    """
    Returns status of transpose line
    Output: Returns 1 if shown,  zero if not.

    """
    pass

def TransposeSet (Start xPos, Start yPos, Start zPos, End xPos, End yPos, End zPos, Action Line Length, x of red axis, y of red axis, z of red axis, x of green axis, y of green axis, z of green axis, x of blue axis, y of blue axis, z of blue axis):
    """
    Sets current Transpose Action Line values.

    """
    pass

def Val (Variable name):
    """
    Evaluates the input and returns a numerical value
    Output: Value of the named variable

    """
    pass

def VarAdd (Variable name, Value To Add):
    """
    Adds a value to an existing variable

    """
    pass

def VarDec (Variable name):
    """
    Subtracts 1 from the value of an existing variable

    """
    pass

def VarDef (Variable name, Variable defaultValue):
    """
    pass

    defines a variable

    """
    pass

def VarDiv (Variable name, Value to Divide By):
    """
    Divides an existing variable by a value

    """
    pass

def VarInc (Variable name):
    """
    Adds 1 to the value of an existing variable

    """
    pass

def VarListCopy (Destination list, Destination initial index, Source list, Source initial index, Number of items to copy. (if omitted or it is 0,  then all items will be copied)):
    """
    Copies items from a source list to a destination list

    """
    pass

def VarLoad (Variable name, FileName, Verify only (1=Only Verify that a proper saved variable file exists,  0=(default)Verifies and loads values):
    """
    Loads variable/s from a file
    Output: Number of loaded or verfied values

    """
    pass

def VarMul (Variable name, Value to Multiply):
    """
    Multiplies an existing variable by a value

    """
    VarSave, Variable name, FileName
    """
    Saves variable value/s to file
    Output: Number of saved values

    """
    pass

def VarSet (Variable name, New Value):
    """
    Sets the value of a named variable

    """
    pass

def VarSize (Variable name):
    """
    Returns the number of items in a variable or in a list
    Output: The number of items in a list or 1 if it is a simple variable

    """
    pass

def VarSub (Variable name, Value To Subtract):
    """
    Subtracts a value from an existing variable

    """
    pass

def Var (Variable name):
    """
    Gets the value of a named variable
    Output: Value of the named variable

    """
    ZBrushInfo, The info type. 0=version number,  1=Demo/Beta/Full,  2=Runtime seconds,  3=Mem use, 4=VMem Use, 5=Free Mem, 6=operating system (0=PC, 1=Mac, 2=MacOSX), 7=Unique session ID, 8=Total RAM, 9=year, 10=mounth, 11=day, 12=hour, 13=minutes, 14=seconds, 15=Day Of The week, 16=cpu 
    """
    Returns ZBrush info.
    Output: Result value

    """
    ZBrushPriorityGet
    """
    Returns the task-priority of ZBrush.
    Output: The current task-priority

    """
    pass

def ZBrushPrioritySet (The priority. -2=Low,  -1=BelowNormal,  0=normal,  1=Above Normal,  2=High):
    """
    Sets the task-priority of ZBrush.

    """
    pass

def ZSphereAdd (xPos, yPos, zPos, Radius, Parent index (0 based), Optional Color   0x000000<->0xffffff  (RED*65536)+(GREEN*256)+BLUE, Optional Mask (0=unmasked to 255=fully masked), Optional TimeStamp, Optional Flags (0=default,  1=invisible link to parent)):
    """
    Adds new ZSphere to the currently active ZSpheres tool
    Output: Returns the the index of the new ZSphere or -1 if command failed.

    """
    pass

def ZSphereDel (ZSphere index.  (Sphere 0 can't be deleted)):
    """
    Deletes a ZSphere from the currently active ZSpheres tool
    Output: Returns zero if command executed successfully.

    """
    ZSphereEdit, ZSpheres editing commands, Store undo? (0=Skip Undo,  1=Store undo)
    """
    Prepares the currently active ZSpheres tool for ZScript editing session.
    Output: Returns the zero if command executed successfully.

    """
    pass

def ZSphereGet (Property: 0=ZSpheres count, 1=xPos, 2=yPos, 3=zPos, 4=radius, 5=color, 6=mask, 7=ParentIndex(-1=none), 8=LastClickedIndex(-1=none), 9=TimeStamp;10=ChildsCount, 11=ChildIndex (2nd index), 12=TimeStampCount, 13=TimeStampIndex, 14=flags, 15=Twist Angle, 16=Membrane, 17=X Re, Optional ZSphere index (0 based), Optional 2nd index (0 based)):
    """
    Gets information about the currently active ZSpheres tool. (Must be placed within ZSphereEdit command)
    Output: Returns the value of the specified property

    """
    pass

def ZSphereSet (Property: 0=unused,  1=xPos, 2=yPos, 3=zPos, 4=radius, 5=color, 6=mask, 7=ParentIndex, 8=unused, 9=TimeStamp, 10=unused, 11=unused, 12=unused, 13=unused, 14=flags, 15=Twist Angle, 16=Membrane, 17=X Res, 18=Y Res, 19=Z Res, 20=XYZ Res, 21=UserValue, ZSphere index (0 based), New property value]):
    Modifies a property of the currently active ZSpheres tool. (Must be placed within ZSphereEdit command)
    Output: Returns zero if command executed successfully.

    Math Functions:
    SIN(angle)
    COS(angle)
    TAN(angle)
    ASIN(value)
    ACOS(value)
    ATAN(value)
    ATAN2(value, value)
    LOG(value)
    LOG10(value)
    SQRT(value)
    ABS(value)
    RAND(value)
    IRAND(value)
    BOOL(value)
    INT(value)
    FRAC(value)
    NEG(value)
    MIN(value1, value2)
    MAX(value1, value2)
   