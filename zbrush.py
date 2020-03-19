
"""
Stubs for zbrush specific functions

Note that these exists just to support code completion and so on, they are mapped 1:1 to 
commands with the same names by the transpiler

"""


def BackColorSet(Red, Green, Blue):
    """
    Sets the pen background color

    """


def ButtonFind(InterfaceItemPath, ButtonText, InitiallyDisabled=0):
    """
    Locates a ZBrush interface item
    """
    pass


def ButtonPress(InterfaceItemPath, ButtonText, InitiallyDisabled=0):
    """
    Locates and presses a ZBrush interface item

    """
    pass


def ButtonSet(InterfaceItemPath, Value, ButtonText, InitiallyDisabled=0):
    """
    Locates and sets a new value to a ZBrush interface item

    """
    pass


def ButtonUnPress(InterfaceItemPath, ButtonText, InitiallyDisabled=0):
    """
    Locates and unpresses a ZBrush interface item

    """
    pass


def CanvasClick(*positions):
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


def CanvasPanGetH():
    """
    Returns the H pan value of the active document view
    Output: The current H Pan value.

    """
    pass


def CanvasPanGetV():
    """
    Returns the V pan value of the active document view
    Output: The current V Pan value.

    """
    pass


def CanvasPanSet(HValue, VValue):
    """
    Pans (Scrolls) the active document view

    """
    pass


def CanvasStroke(StrokeData, Delayed, Rotation, HScale, VScale, HOffset, VOffset):
    """
    Emulates a brush stroke within the current canvas area

    """
    pass


def CanvasStrokes(StrokesData, Delayed, Rotation, HScale, VScale, HOffset, VOffset, HRotateCenter, VRotateCenter):
    """
    Emulates multiple brush strokes within the current canvas area

    """
    pass


def CanvasZoomGet():
    """
    Returns the zoom value of the active document view
    Output: The current zoom value.
    """
    pass


def CanvasZoomSet(ZoomFactor):
    """
    Sets the zoom factor of the active document view

    """
    pass


def Caption(Text):
    """
    Displays a text line using the current Caption settings

    """
    pass


def CurveAddPoint(CurveIndex, XPos, YPos, ZPos):
    """
    Add a new point to the specified curve
    Output: Returns the point index (zero based) or -1 if failed.

    """
    pass


def CurvesCreateMesh(Name, Action, Thickness):
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


def CurvesDelete():
    """
    Deletes named curves list.

    """
    pass


def CurvesNewCurve():
    """
    Creates a new curve in the current curves list.
    Output: Returns the curve index (zero based) or -1 if failed.

    """
    pass


def CurvesNew():
    """
    Creates a new curves list.

    """
    pass


def CurvesToUI():
    """
    Copy the ZScript curves to UI
    Output: Returns zero of OK or -1 if failed.

    """
    pass


def Delay(DelaySeconds):
    """
    Delays execution of ZScript for specified amount of time

    """
    pass


def DispMapCreate(ImageWidth, ImageHeight, Smooth=1, SubPoly=0, Border=8, UVTile=0, UseHD=1):
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


def FileDelete(FileName):
    """
    Delete specific file.
    Output: Returns zero if command executed successfully.

    """
    pass


def FileExecute(FileName, MethodName, Text="", Number="", InOutMem1=None, InOutMem2=None):
    """
    Executes the specified plugin file (DLL).
    Output: Returns the result value which was returned by the executed routine. Returns zero if error

    """
    pass


def FileExists(FileName):
    """
    Check if a specific file exists.
    Output: Returns 1 if file exists. Returns zero if does not exists

    """
    pass


def FileGetInfo(FileName, InfoIndex):
    """
    Retrieve information about a specified file.
    Output: Returns the requested information or zero if file not found.

    """
    pass


def FileNameAdvance(FileNameBase, NumDigits, AddCopyTag):
    """
    Increments the index value contained within a filename string  
    Output: Updated file Name

    """
    pass


def FileNameAsk(Extensions, DefaultName, DialogTitle):
    """
    Asks user for a file name
    If DefaultName is omitted, it's an Open dialog
    Output: Result file name or an empty string if user canceled operation.

    """
    pass


def FileNameExtract(FileName, Component):
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


def FileNameMake(BaseFileName, Index, NumDigits):
    """
    Combines a base filename with an index number
    Output: Combined file name Variable

    """
    pass


def FileNameResolvePath(LocalFileName):
    """
    Resolves local path to full path
    Output: Full path.

    """
    pass


def FileNameSetNext(FileName, TemplatePath=None):
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


def FontSetColor(Red, Green, Blue):
    """
    Sets the color of the text-flow font

    """
    pass


def FontSetOpacity(Opacity):
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


def FrontColorSet(Description, Red, Green, Blue, Disabled=0):
    """
    Sets the main interface color to a new value

    """
    pass


def GetActiveToolPath():
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


def HotKeyText(InterfacePath):
    """
    Displays a hot-key for the specified interface item
    """
    pass


def IButton(ButtonText, PopupText, Commands, Disabled=0, Width=0, Hotkey='', Icon='', Height=0):
    """
    Creates an interactive push button
    """
    pass


def IClick(InterfacePath, *positions):
    """
    Emulates a click within a specified ZBrush interface item

    """
    pass


def IClose(InterfacePath, ShowZoom=0, TargetParent=0):
    """
    Closes an interface item.

    """
    pass


def IColorSet(Red, Green, Blue):
    """
    Sets the active color to a new value

    """
    pass


def IConfig(Config):
    """
    Sets ZBrush internal version-configuration

    """
    pass


def IDialog(Title, TitleMode=0, Icon='', LeftInset=0, RightInset=0, LeftTop=0, RightBottom=0):
    """
    Adds a subpalette to ZBrush interface.
    Mode :
     mode? (0=Show Title and minimize button(ByDefault) 1=Show Title without minimize button 2=Hide Title )

    Icon:  Optional subpalette gray-scale (8-bits) icon (Standrad size of 20x20 pixels)

    Output: Returns 1 if subpalette added succesfuly. Returns 0 if subpalette could not be added or if it already exsists.

    """
    pass


def IDisable(WindowPath, WindowID):
    """
    Disables a ZScript interface item (can only be used for ZScript-generated interface items)

    """
    pass


def IEnable(WindowPath, WindowID):
    """
    Enables a ZScript interface item (can only be used for ZScript-generated interface items)

    """
    pass


def IExists(InterfaceItemPath):
    """
    Verifies that a specified interface item exists.
    Output: 1 if item exists, 0 otherwise

    """
    pass


def IFadeIn(FadeOutSpeed=0.5):
    """
    Fades ZBrush window to black.

    """
    pass


def IFadeOut(FadeOutSpeed=0.5):
    """
    Fades ZBrush window to black.

    """
    pass


def IFreeze(CommandS, FadeOutSpeed=0.05):
    """
    Disables interface updates.

    """


def IGet(InterfaceItemPath):
    """
    Returns the current value of a ZBrush or ZScript interface item
    Output: The item value

    """
    pass


def IGetFlags(InterfaceItemPath):
    """
    Returns the status flags of the specified interface item
    Output: The flags

    """
    pass


def IGetHotkey(InterfaceItemPath):
    """
    Returns the hotkey of the specified interface item
    Output: The Hotkey

    """
    pass


def IGetID(InterfaceItemPath):
    """
    Returns the window ID code of the specified interface item
    Output: The Title

    """
    pass


def IGetInfo(InterfaceItemPath):
    """
    Returns the info (popup info) of the specified interface item
    Output: The info

    """
    pass


def IGetMax(InterfaceItemPath):
    """
    Returns the maximum possible value of a ZBrush or ZScript interface item
    Output: The item maximum value

    """
    pass


def IGetMin(InterfaceItemPath):
    """
    Returns the minimum possible value of a ZBrush or ZScript interface item
    Output: The item minimum value

    """
    pass


def IGetSecondary(InterfaceItemPath):
    """
    Returns the the scondary value of a 2D interface item
    Output: The item value
    """
    pass


def IGetStatus(InterfaceItemPath):
    """
    Returns the Enabled/Disabled status of a ZBrush or ZScript interface item
    Output: The item status
        0=Disabled
        1=Enabled
    """
    pass


def IGetTitle(InterfaceItemPath, ReturnFullPath):
    """
    Returns the title of the specified interface item
    Output: The Title of the button

    """
    pass


def IHeight(InterfaceItemPath):
    """
    Returns the pixel-height of an interface item.
    Output: The height of the interface item.

    """
    pass


def IHide(InterfaceItemPath, ShowZoomRectangles=0, TargetParentWindow=0):
    """
    Hides an interface item.

    """
    pass


def IHPos(InterfaceItemPath, UseGlobalCoords=0):
    """
    Returns the H position of the interface item in Canvas or Global coordinates.
    Output: The H position of the interface item.

    """
    pass


def IKeyPress(KeyCode, Commands, HCursor=None, VCursor=None):
    """
    Simulates a key press

    """
    pass


def ILock(WindowPath, WindowID):
    """
    Locks an interface item 

    """
    pass


def Image(FileName, Align, ResizedWidth):
    """
    Loads and displays an image
    Align (0=center 1=left 2=right
    """


def IMaximize(InterfaceItemPath, MaximizeSubPalettes):
    """
    Locates an interface item and (if possible) maximize its size.

    """
    pass


def IMinimize(InterfaceItemPath, MinimizeSubPalettes):
    """
    Locates an interface item and (if possible) minimize its size.

    """
    pass


def IModGet(InterfaceItemPath):
    """
    Returns the current modifiers binary state of a ZBrush or ZScript interface item
    Output: The item value

    """
    pass


def IModSet(InterfaceItemPath, value):
    """
    Sets the modifiers binary value of a ZBrush or a ZScript interface item

    """
    pass


def Interpolate(Time, Value1, Value2, Value3, Value4, AngleInterpolate=0):
    """
    Performs time-based interpolation

    Time: (0=AtStart 0.5=half 1=AtEnd)	
    Values are (Num,  VarName or ListName)

    Output: Interpolated value or list

    """
    pass


def IPress(InterfaceItemPath):
    """
    Presses a ZBrush or ZScript interface item

    """
    pass


def IReset(ItemToReset=0, ZBrushVersion=1.5):
    """
    Interface Reset
    ItemToReset = 0=All, 1=Interface, 2=Document, 3=Tools, 4=Lights, 5=Materials, 6=Stencil

    Output: Returns the button that the user clicked. ( 0=NO,  1=YES )

    """
    pass


def IsDisabled(InterfaceItemPath):
    """
    Returns 1 if the specified ZBrush or ZScript interface item is currently disabled,  returns 0 otherwise
    Output: The item 'Disabled' status (1=Disabled 0=Enabled)

    """
    pass


def IsEnabled(InterfaceItemPath):
    """
    Returns 1 if the specified ZBrush or ZScript interface item is currently enabled,  returns 0 otherwise
    Output: The item 'Enabled' status (1=Enabled 0=Disabled)

    """
    pass


def ISet(InterfaceItemPath, Value, SecondaryValue=None):
    """
    Sets a new value to a ZBrush or ZScript interface item

    """
    pass


def ISetHotkey(InterfaceItemPath, Hotkey):
    """
    Sets the hotkey of the specified interface item
    0 = no hotkey
    """
    pass


def ISetMax(InterfaceItemPath, MaxValue):
    """
    Sets the maximum value for an ISlider interface item (can only be used for ZScript-generated interface items)

    """


def ISetMin(InterfaceItemPath, MinValue):
    """
    Sets the minimum value for an ISlider interface item (can only be used for ZScript-generated interface items)

    """
    pass


def ISetStatus(InterfaceItemPath, Status):
    """
    Enables or Disables a ZScript interface item (can only be used for ZScript-generated interface items)
    New status ( 0=Disable NotZero=Enable )
    """
    pass


def IShowActions(ShowActions):
    """
    Temorarily sets the status of ShowActions
    . 0=Disable ShowActions,  Positive value=enable show actions Negative value=Reset ShowActions 

    """
    pass


def IShow(InterfaceItemPath, ShowZoomRectangles=0, TargetParenWindow=0):
    """
    Locates an interface item and makes it visible.

    """
    pass


def ISlider(SliderText, CurValue, Resolution, MinValue, MaxValue, PopupText, ChangeCommand, InitiallyDisabled=0, ButtonWidth=0):
    """
    Creates an interactive slider
    ButtonWidth:  in pixels (0=AutoWidth NonZero=Specified width)
    """
    pass


def IsLocked(InterfaceItemPath):
    """
    Returns 1 if the specified ZBrush or ZScript interface item is currently locked,  returns 0 otherwise
    Output: The item 'Locked' status (1=Locked 0=Unlocked)

    """


def IsPolyMesh3DSolid():
    """
    Tests if current PolyMesh3D is a Solid
    Output: Returns 1 if current PolyMesh3D is a valid Solid,  0 otherwise.

    """
    pass


def IStroke(InterfaceItemPath, StrokeData):
    """
    Emulates a brush stroke within an interface item

    """
    pass


def ISubPalette(PaletteName, TitleMode=0,  Icon=None, LeftInset=0, RightInset=0, LeftTop=0, RightBottom=0):
    """
    Adds a subpalette to ZBrush interface.

    TitleMode: ? (0=Show Title and minimize button(ByDefault) 1=Show Title without minimize button 2=Hide Title ),
    Icon  (8-bits) icon (Standrad size of 20x20 pixels)

    Output: Returns 1 if subpalette added succesfuly. Returns 0 if subpalette could not be added or if it already exsists.

    """
    pass


def IsUnlocked(InterfaceItemPath):
    """
    Returns 1 if the specified ZBrush or ZScript interface item is currently unlocked,  returns 0 otherwise
    Output: The item 'Unlocked' status (1=Unlocked 0=locked)

    """
    pass


def ISwitch(ButtonText, InitialState, PopupText, PressCommands, UnpressedCommands, InitiallyDisabled=0, ButtonWidth=0):
    """
    Creates an interactive switch
    InitialState (1=pressed, 0=unpressed),
    """
    pass


def IToggle(InterfaceItemPath):
    """
    Toggles the state of a ZBrush or ZScript interface item

    """
    pass


def IUnlock(WindowPath, WindowID):
    """
    Unlocks an interface item

    """
    pass


def IUnPress(InterfaceItemPath):
    """
    Unpresses a ZBrush or ZScript interface item
    """
    pass


def IUpdate(RepeatCount=1, Redraw=0):
    """
    Updates the ZBrush interface.
    """
    pass


def IVPos(InterfaceItemPath, UseGlobalCoords=0):
    """
    Returns the V position of the interface item in Canvas or Global coordinates.
    Output: The V position of the interface item.

    """
    pass


def IWidth(InterfaceItemPath):
    """
    Returns the pixel-width of an interface item.
    Output: The width of the interface item.

    """
    pass


def MemCopy(FromBlock, FromOffset, ToBlock, ToOffset, NumBytes=None):
    """
    Copies data from one memory block into another.
    if NumBytes is supplied, limit to that number of b
    Output: Returns the mumber of bytes moved. (-1 indicates an error)

    """
    pass


def MemCreate(BlockID, BlockSize, InitialFill=None):
    """
    Creates a new memory block.
    If InitialFill is supplied, fil with that value

    Output: Returns the size of the new memory block or error code...0=Error -1=Memory already exists -2=Can't create memory block.

    """
    pass


def MemCreateFromFile(BlockId, FileName, FileOffset=0, MaxBytes=None):
    """
    Creates a new memory block from a disk file.
    if FileOffset is supplied, read fron that byte
    if MaxBytes is supplied, read only that many bytes

    Output: Returns the size of the new memory block or error code...0=Error -1=Memory already exists -2=Can't create memory block -3=File not found.

    """
    pass


def MemDelete(BlockID):
    """
    Deletes a memory block.
    Output: Returns the size of the deleted memory block. Returns 0 if memory block could not be found.

    """
    pass


def MemGetSize(BlockID):
    """
    Returns the size of a memory block (Also useful for determining if a memory block already exists
    Output: Returns the size of the memory block. Returns 0 if data block could not be found.

    """
    pass


def MemMove(BlockID, FromOffset, ToOffset, NumBytes):
    """
    Move data within an existing memory block.
    Output: Returns the mumber of bytes moved.

    """
    pass


def MemMultiWrite(BlockID, Value, Format, Offset, RepeatCount, SubsequentOffset):
    """
    Write data to a memory block.
    Format: (0=omited=float,  1=signed char, 2=unsigned char, 3=signed short, 4=unsigned short, 5=signed long, 6=unsigned long, 7=fixed16 (16.16)
    Output: Returns the number of actual bytes written
    """
    pass


def MemRead(BlockID, ReadVariable, Format, Offset):
    """
    Reads data from a memory block.
    Data format (0=omited=float,  1=signed char, 2=unsigned char, 3=signed short, 4=unsigned short, 5=signed long, 6=unsigned long, 7=fixed16 (16.16)
    Output: Returns the number of actual bytes read

    """
    pass


def MemReadString(BlockID, StringVar, Offset, BreakAtLineEnd=0, SkipWhiteSpace=0, MaxReadLength=255):
    """
    Reads a string from a memory block.
    Output: Returns the number of bytes scanned. (may be larger than the actual bytes read)

    """
    pass


def MemResize(BlockID, NewSize, FillValue=None):
    """
    Resizes an exsiting memory block.
    if FillValue supplied, use it to fill newly allocated memory
    Output: Returns the new size of the memory block. Zero indicates an error.

    """
    pass


def MemSaveToFile(BlockID, FileName, OverwriteIfExists=0):
    """
    Saves an exisiting memory block to a disk file.
    Overwrite if exists? Set to nonzero value to save the file even if an identically named file already exists on disk. Default=Do not overwrite.
    Output: Returns the size of the new memory block or error code...0=Error -1=Memory does not exists -2=File already exits -3=File write error.

    """
    pass


def MemWrite(BlockID, Value, Format=0, Offset=0):
    """
    Write data to a memory block.
    Format (0=omited=float,  1=signed char, 2=unsigned char, 3=signed short, 4=unsigned short, 5=signed long, 6=unsigned long, 7=fixed16 (16.16)
    Output: Returns the number of actual bytes written

    """
    pass


def MemWriteString(BlockID, Value, Offset=0, WriteNullTerminator=1):
    """
    Writes a string into a memory block.
    Output: Returns the number of bytes written. (including the terminating zero)
    """
    pass


def MergeUndo():
    """
    Merge the next undo with the previous undo.

    """
    pass


def Mesh3DGet(Property, IndexInput,  OptionalInput, OptionalOutput1=None,  OptionalOutput2=None,  OptionalOutput3=None,  OptionalOutput4=None,  OptionalOutput5=None,  OptionalOutput6=None,  OptionalOutput7=None,  OptionalOutput8=None):
    """
    Gets information about the currently active  Mesh3D tool.
    Property: 0=PointsCount, 1=FacesCount, 2=XYZ bounds, 3=UVBounds, 4=1stUVTile, 5=NxtUVTile, 6=PolysInUVTile, 7=3DAreaOfUVTile, 8=Full3DMeshArea
    IndexInput:  Vertix/Face/Group/UVTile H index (0 based),
    OutputVariables will be filled based on chosen inputs
    Output: Returns zero if command executed successfully,  any other value indicates and error.

    """
    pass


def MessageOK(Message, Title):
    """
    Displays a user message with a single OK button

    """
    pass


def MessageOKCancel(Message, Title):
    """
    Displays a user message with CANCEL and OK buttons
    Output: Returns the button that the user clicked. (0=CANCEL,  1=OK)

    """
    pass


def MessageYesNo(Message, Title):
    """
    Displays a user message with YES and NO buttons
    Output: Returns the button that the user clicked. (0=NO,  1=YES)

    """
    pass


def MessageYesNoCancel(Message, Title):
    """
    Displays a user message with YES,  NO and CANCEL buttons
    Output: Returns the button that the user clicked. (0=NO,  1=YES CANCEL=-1)

    """
    pass


def MouseHPos(UseGlobalCoordinates=0):
    """
    Returns the current H position of the mouse in Canvas or Global coordinates.
    Output: The H position of the mouse

    """
    pass


def MouseLButton():
    """
    Returns the current state of the left mouse button 
    Output: Returns 1 if mouse button is pressed,  returns zero if unpressed

    """
    pass


def MouseVPos(UseGlobalCoordinates=0):
    """
    Returns the current V position of the mouse in Canvas or Global coordinates.
    Output: The V position of the mouse

    """
    pass


def MTransformGet(BlockID, VariableIndex=0):
    """
    Gets current transformation values into an existing memory block

    """
    pass


def MTransformSet(BlockID, VariableIndex=0):
    """
    Sets new transformation values from an existing memory block.

    """
    pass


def MVarDef(BlockID,  Count, InitialFill=0):
    """
    pass

    defines a new variables memory block.
    Output: Returns the variables count of the new memory block or error code...0=Error -1=Memory already exists -2=Can't create memory block.

    """
    pass


def MVarGet(BlockID, VariableIndex):
    """
    Reads a float value from a memory block.
    Output: Returns the float value.

    """
    pass


def MVarSet(BlockID, VariableIndex):
    """
    Writes a float value to a memory block.
    Output: Returns the old value of the variable.

    """
    pass


def NormalMapCreate(ImageWidth, ImageHeight, Smooth=1, SubPoly=0, Border=0, UVTile=None, UseTangentCoords=0):
    """
    Creates NormalMap
    Output: Returns zero if executed successfully. Any other value indicates an error

    """
    pass


def Note(Text, InterfaceItemPath=None, DisplayDuration=0, PopupBackgroundColor=0x606060, OffsetDistance=48, Width=400,  WindowFillColor=None, FrameHorizontalSize=1, FrameVerticalSize=1, FrameLeft=0,  FrameTop=0, IconFileName=None):
    """
    Displays a note to the user.

    BackgroundColor = x000000<->0xffffff,  default=0x606060,  0=NoBackground 

    FrameLeft ( 0=left (default) ,  .5=center,  1=right )
    FrameTop ( 0=top (default) ,  .5=center,  1=bottom )

    Output: If the note has UI buttons then the return value of the pressed buttons (1=1st button,  2=2nd button ...),  otherwise the return value will be zero.
    """
    pass


def NoteBar(Message=None, ProgressVarValue=0):
    """
    Displays a note in progress bar.

    """
    pass


def NoteIButton(ButtonText, ButtonIcon=None, InitiallyPressed=0, InitiallyDisabled=0, HRelativePos=0, VRelativePos=0, ButtonWidth=None, ButtonHeight=None, ButtonColor=0x000000,  TextColor=0xffffff, BGOpacity=1, TextOpacity=1, ImageOpacity=1):
    """
    pass

    defines a button to be included within the next Note to be shown.
    HRelativePos: (Positive value=offset from left,  Negative value=offset from right,  0=automatic),
    VRelativePos:  (Positive value=offset from top,  Negative value=offset from bottom,  0=automatic),
    colors :   0x000000<->0xffffff (blue + (green*256) + (red*65536) )
    """
    pass


def NoteIGet(NoteButtonIndexOrName):
    """
    Returns the value of am NoteIButton which was shown in the last displayed Note.
    Output: The item value

    """
    pass


def NoteISwitch(ButtonText, ButtonIcon=None, InitiallyPressed=0, InitiallyDisabled=0, HRelativePos=0, VRelativePos=0, ButtonWidth=None, ButtonHeight=None, ButtonColor=0x000000,  TextColor=0xffffff, BGOpacity=1, TextOpacity=1, ImageOpacity=1):
    """
    pass

    define a switch-button to be included within the next Note to be shown.

    """
    pass


def PageSetWidth(PageWidth):
    """
    Sets the width of the page

    """
    pass


def PaintBackground(Red, Green, Blue):
    """
    Paints the background using the current background color

    """
    pass


def PaintBackSliver(height, Red, Green, Blue):
    """
    Draws a full page-width rectangle using the current background color

    """
    pass


def PaintPageBreak():
    """
    Draws a visual page-break

    """
    pass


def PaintRect(Width, Height, Red, Green, Blue):
    """
    Draws a rectangle (in the ZScript window) using the current pen color

    """
    pass


def PaintTextRect(Width, Height, Text):
    """
    Draws a rectangle with imbedded text

    """
    pass


def PD():
    """
    Moves the pen position to the beginning of the next line (Same as PenMoveDown)

    """
    pass


def PenMoveCenter():
    """
    Moves the pen position to the horizontal center of the page

    """
    pass


def PenMoveDown():
    """
    Moves the pen position to the beginning of the next line

    """
    pass


def PenMoveLeft():
    """
    Moves the pen position to the left side of the page

    """
    pass


def PenMoveRight():
    """
    Moves the pen position to the right side of the page

    """
    pass


def PenMove(HOffset, VOffset):
    """
    Moves the pen a relative distance

    """
    pass


def PenSetColor(Red, Green, Blue):
    """
    Sets the pen main color

    """
    pass


def PixolPick(ComponentIndex, HPosition, VPosition):
    """
    Retrieves information about a specified Pixol
    componentIndex: 0=CompositeColor ( 0x000000<->0xffffff  or red*65536+green*256+blue) 1=Z(-32576 to 32576) 2=Red(0 to 255 ) 3=Green(0 to 255 ) 4=Blue(0 to 255 )  5=MaterialIndex(0 to 255 ) 6=XNormal(-1 to 1) 7=YNormal(-1 to 1) 8=ZNormal(-1 to 0) 

    Output: The value of the specified Pixol

    """
    pass


def PropertySet(CommandName, PropertyIndex, Value):
    """
    Modifies the setting of Title,  SubTitle and Caption text

    CommandName {Title, SubTitle, Caption}

    """
    pass


def Randomize(SeedValue):
    """
    Resets the Rand generator.
    SeedValue <= int16

    """
    pass


def RGB(Red, Green, Blue):
    """
    Combines 3 color-components into one RGB value
    Output: Combined RGB

    """
    pass

# def RoutineCall (Name of the routine to be called, Input Var01, Input Var02, Input Var03, Input Var04, Input Var05, Input Var06, Input Var07, Input Var08, Input Var09, Input Var10):
#     """
#     Executes the specified defined routine

#     """
#     pass

# def RoutineDef (Name of the routine, Commands group that will be executed when the routine is called, Input Var01, Input Var02, Input Var03, Input Var04, Input Var05, Input Var06, Input Var07, Input Var08, Input Var09, Input Var10):
#     """
#     pass

#     defines a named commands group

#     """
#     pass


def SectionBegin(SectionTitle, Expanded, PopupText, ExpandCommands, CollapsCommands, InitiallyDisabled=0):
    """
    Begins a collapsible section

    """
    pass


def SectionEnd():
    """
    Ends a collapsible section

    """
    pass


def ShellExecute(ShellCommand):
    """
    Execute a shell command

    """
    pass


def Sleep(Time, AwakenCommands,  EventType, OutEventCode, OutWindow):
    """
    Exists ZScript and be awaken by specified event.

    EventType:  (default=1) (1=Timer, 2=Mouse Moved, 4=LButton down, 8=LButton up, 16=KeyDown, 32=keyUp, 64=ModifierKeyDown, 128=ModifierKeyUp, 256=Startup, 512=Shut down, 1024 InterfaceItem pressed/unpressed, 2048 tool selected, 4096 texture selected,  8192 alpha sele

    """
    pass


def SleepAgain(Time, EventType):
    """
    Exists ZScript and continues the Sleep command.
    EventType:  (default=1) (1=Timer, 2=Mouse Moved, 4=LButton down, 8=LButton up, 16=KeyDown, 32=keyUp, 64=ModifierKeyDown, 128=ModifierKeyUp, 256=Startup, 512=Shut down, 1024 InterfaceItem pressed/unpressed, 2048 tool selected, 4096 texture selected,  8192 alpha sele

    """
    pass


def SoundPlay(BlockID, PlayMode):
    """
    Plays the sounds loaded into a specified memory block.
    PlayMode: . 0=default=Play once,  dont wait for completion. 1=Play once,  wait for completion. 2=Play loop,  dont wait for completion.):

    Output: Returns the zero if command executed successfully.

    """
    pass


def SoundStop(BlockId):
    """
    Stops the currently specified sound.
    Output: Returns the zero if command executed successfully.

    """
    pass


def StrAsk(InitialString, Title=""):
    """
    Asks user to input a string.
    Output: Returns the text typed by user or an empty string if canceled.

    """
    pass


def StrExtract(Input string, Start character index(0=left), End character index(0=left)):
    """
    Returns specified portion of the input string
    Output: The extracted portion of the input string.

    """
    pass


def StrFind(find this string, in this string, Optional start search index(default=0)):
    """
    Locate a string within a string.
    Output: Returns the starting index of the 1st string within the 2nd string. returns -1 if not found.

    """
    pass


def StrFromAsc(Input Ascii value):
    """
    Returns the character of the specified Ascii value.
    Output: The character of the specified Ascii value.

    """
    pass


def StrLength(String to evaluate):
    """
    Returns the number of characters in the input string.
    Output: Number of characters in the input string.

    """
    pass


def StrLower(Input string):
    """
    Returns the lowercase version of the input string.
    Output: The lowercase version of the input string.

    """
    pass


def StrMerge(Str 1, Str 2, Optional Str 3, Opt Str 4, Opt Str 5, Opt Str 6, Opt Str 7, Opt Str 8, Opt Str 9, Opt Str 10, Opt Str 11, Opt Str 12):
    """
    Combines two (or more) strings into one string.
    Output: The combined string. Note: result string will not exceed 255 characters in length 

    """
    pass


def StrokeGetInfo(Stroke-type Variable, Info number, Point index(0 based)):
    """
    Retrieves the information from a specified Stroke-type Variable
    Output: StrokeInfo result

    """
    pass


def StrokeGetLast():
    """
    Retrieves the last drawn brush stroke
    Output: StrokeData

    """
    pass


def StrokeLoad(FileName):
    """
    Loads a brush-stroke text file
    Output: StrokeData

    """
    pass


def StrokesLoad(FileName):
    """
    Loads a brush-strokes text file
    Output: StrokesData

    """
    pass


def StrToAsc(Input string, Optional character offset(default=0)):
    """
    Returns the Ascii value of a character.
    Output: The Ascii value of a character.

    """
    pass


def StrUpper(Input string):
    """
    Returns the uppercase version of the input string.
    Output: The uppercase version of the input string.

    """
    pass


def SubTitle(Text):
    """
    Displays a text line using the current SubTitle settings

    """
    pass


def SubToolGetActiveIndex():
    """
    Returns the index of the active subtool
    Output: Returns the index of the active subtool (zero based).

    """
    pass


def SubToolGetCount():
    """
    Returns the number of subtools in the active tool
    Output: Returns the number of subtools.  Return 0 if error.

    """
    pass


def SubToolGetFolderIndex(SubtoolIndex):
    """
    Returns the folder index in which this subtool is contained
    If SubtoolIndex omited then use the currently selected tool.

    Output: Returns the foldr index or -1 if this subtool is not within a folder.


    """
    pass


def SubToolGetFolderName(SubtoolIndex):
    """
    Returns the ffolder name of the specified subtool
    If SubtoolIndex omited then use the currently selected tool.
    Output: Result folder name or empty if subtool is not in a folder.

    """
    pass


def SubToolGetID(SubtoolIndex):
    """
    Returns the unique subtool ID
    If SubtoolIndex omited then use the currently selected tool.
    Output: Returns the unique subtool ID or zero if error.

    """
    pass


def SubToolGetStatus(SubtoolIndex):
    """
    Returns the status of a subtool
    If SubtoolIndex omited then use the currently selected tool.
    Output: Returns the status (Subtool Eye=0x01,  Folder Eye=0x02, UnionAdd=0x10, UnionSub=0x20, UnionClip=0x40, UnionStart=0x80, ClosedFolder=0x400, OpenedFolder=0x800) .

    """
    pass


def SubToolLocate(SubtoolID):
    """
    Locates a subtool by the specified unique ID
    Output: Returns the index of the located subtool or -1 if error.

    """
    pass


def SubToolSelect(SubtoolIndex):
    """
    Selects the specified subtool index
    Output: Returns zero if OK,  -1 if error.

    """
    pass


def SubToolSetStatus(SubtoolIndex, Value):
    """
    Sets the status of a subtool
    If SubtoolIndex omited then use the currently selected tool.
    Value: (Subtool Eye=0x01, Folder Eye=0x02, UnionAdd=0x10, UnionSub=0x20, UnionClip=0x40, UnionStart=0x80, ClosedFolder=0x400, OpenedFolder=0x800)
    """
    pass


def TextCalcWidth(Text):
    """
    Calculates the pixel-width of the specified string
    Output: Width of text in pixels

    """
    pass


def Title(Text):
    """
    Displays a text line using the current Title settings

    """
    pass


def TLDeleteKeyFrame(KeyIndex):
    """
    Delete specified key frame index of the active track
    Output: Returns the number of available key frames

    """
    pass


def TLGetActiveTrackIndex():
    """
    Returns the index of the active track
    Output: Returns the current active track index -1=None 

    """
    pass


def TLGetKeyFramesCount():
    """
    Returns the total number of key frames in the active track
    Output: Returns the number of key frames in the active track 0=None 

    """
    pass


def TLGetKeyFrameTime(KeyIndex):
    """
    Get the time of the specified key frame index of the active track
    Output: Returns the time of the selected key frame or -1 if error.

    """
    pass


def TLGetTime():
    """
    Returns the current TimeLine knob position in  0.0 to 1.0 range
    Output: Returns the current TimeLine knob time 0=start,  1=end

    """
    pass


def TLGotoKeyFrameTime(KeyIndex):
    """
    Move TimeLine knob position to specified key frame index of the active track
    Output: Returns the time of the selected key frame or -1 if error.

    """
    pass


def TLGotoTime(Time):
    """
    Sets the current TimeLine knob position in  0.0 to 1.0 range
    Output: Returns zero if OK,  -1 if error.

    """
    pass


def TLNewKeyFrame(Time=None):
    """
    Create a new key frame in the active track
    if Time is omitted, use current time
    Output: Returns the new key frame index or -1 if error.

    """
    pass


def TLSetActiveTrackIndex(TrackIndex):
    """
    Sets the active track index
    Output: Returns zero if OK,  -1 if error.

    """
    pass


def TLSetKeyFrameTime(KeyIndex, Time):
    """
    Set the time of the specified key frame index of the active track
    Time is 0-1
    Output: Returns the new key frame index or -1 if error.

    """
    pass

def ToolGetActiveIndex():
    """
    Returns the index of the active tool
    Output: Returns the index of the active tool (zero based).

    """
    pass

def ToolGetCount():
    """
    Returns the number of available tools
    Output:  Returns the number of available tools.

    """
    pass


def ToolGetPath(ToolIndex=None):
    """
    Returns the file path or name of the specified tool
    If ToolIndex is omited then use the currently selected tool.
    Output: Result path (without the .ztl). Empty if error.

    """
    pass


def ToolGetSubToolID(ToolIndex=None, SubtoolIndex=None):
    """
    Returns the unique subtool ID
    If ToolIndex is omited then use the currently selected tool.
    If SubtoolIndex omited then use the selected subtool.):
    Output: Returns the unique subtool ID or zero if error.

    """
    pass


def ToolGetSubToolsCount(ToolIndex):
    """
    Returns the number of subtools in the specified tool index
    If ToolIndex is omited then use the currently selected tool.
    Output: Returns the number of subtools.  Return 0 if error.

    """
    pass


def ToolLocateSubTool(Unique Subtool ID, Optional subtool index result):
    """
    Locates a subtool by the specified unique ID
    Output: Returns the index of the located tool and subtool or -1 if error.

    """
    pass


def ToolSelect(Tool Index(zero based).):
    """
    Selects the specified tool index
    Output: Returns zero if OK,  -1 if error.

    """
    pass


def ToolSetPath(Tool Index(zero based). If omited then use the currently selected tool., New Path. Path extension(such as .ztl) will be omited.):
    """
    Sets the file path or name of the specified tool
    Output: Returns zero if OK,  -1 if error.

    """
    pass


def TransformGet(xPos, yPos, zPos, xScale, yScale, zScale, xRotate, yRotate, zRotate):
    """
    Gets current transformation values.

    """
    pass


def TransformSet(xPos, yPos, zPos, xScale, yScale, zScale, xRotate, yRotate, zRotate):
    """
    Sets new transformation values.

    """
    pass


def TransposeGet(Start xPos, Start yPos, Start zPos, End xPos, End yPos, End zPos, Action Line Length, x of red axis, y of red axis, z of red axis, x of green axis, y of green axis, z of green axis, x of blue axis, y of blue axis, z of blue axis):
    """
    Gets current Transpose Action Line values.

    """
    TransposeIsShown
    """
    Returns status of transpose line
    Output: Returns 1 if shown,  zero if not.

    """
    pass


def TransposeSet(Start xPos, Start yPos, Start zPos, End xPos, End yPos, End zPos, Action Line Length, x of red axis, y of red axis, z of red axis, x of green axis, y of green axis, z of green axis, x of blue axis, y of blue axis, z of blue axis):
    """
    Sets current Transpose Action Line values.

    """
    pass


def Val(Variable name):
    """
    Evaluates the input and returns a numerical value
    Output: Value of the named variable

    """
    pass


def VarAdd(Variable name, Value To Add):
    """
    Adds a value to an existing variable

    """
    pass


def VarDec(Variable name):
    """
    Subtracts 1 from the value of an existing variable

    """
    pass


def VarDef(Variable name, Variable defaultValue):
    """
    pass

    defines a variable

    """
    pass


def VarDiv(Variable name, Value to Divide By):
    """
    Divides an existing variable by a value

    """
    pass


def VarInc(Variable name):
    """
    Adds 1 to the value of an existing variable

    """
    pass


def VarListCopy(Destination list, Destination initial index, Source list, Source initial index, Number of items to copy. (if omitted or it is 0,  then all items will be copied)):
    """
    Copies items from a source list to a destination list

    """
    pass


def VarLoad(Variable name, FileName, Verify only(1=Only Verify that a proper saved variable file exists,  0=(default)Verifies and loads values):
            """
    Loads variable/s from a file
    Output: Number of loaded or verfied values

    """
            pass

            def VarMul(Variable name, Value to Multiply):
            """
    Multiplies an existing variable by a value

    """
            VarSave, Variable name, FileName
            """
    Saves variable value/s to file
    Output: Number of saved values

    """
            pass

            def VarSet(Variable name, New Value):
            """
    Sets the value of a named variable

    """
            pass

            def VarSize(Variable name):
            """
    Returns the number of items in a variable or in a list
    Output: The number of items in a list or 1 if it is a simple variable

    """
            pass

            def VarSub(Variable name, Value To Subtract):
            """
    Subtracts a value from an existing variable

    """
            pass

            def Var(Variable name):
            """
    Gets the value of a named variable
    Output: Value of the named variable

    """
            ZBrushInfo, The info type. 0=version number,  1=Demo/Beta/Full,  2=Runtime seconds,  3=Mem use, 4=VMem Use, 5=Free Mem, 6=operating system(0=PC, 1=Mac, 2=MacOSX), 7=Unique session ID, 8=Total RAM, 9=year, 10=mounth, 11=day, 12=hour, 13=minutes, 14=seconds, 15=Day Of The week, 16=cpu
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

            def ZBrushPrioritySet(The priority. -2=Low,  -1=BelowNormal,  0=normal,  1=Above Normal,  2=High):
            """
    Sets the task-priority of ZBrush.

    """
            pass

            def ZSphereAdd(xPos, yPos, zPos, Radius, Parent index(0 based), Optional Color   0x000000 < ->0xffffff  (RED*65536)+(GREEN*256)+BLUE, Optional Mask(0=unmasked to 255=fully masked), Optional TimeStamp, Optional Flags(0=default,  1=invisible link to parent)):
            """
    Adds new ZSphere to the currently active ZSpheres tool
    Output: Returns the the index of the new ZSphere or -1 if command failed.

    """
            pass

            def ZSphereDel(ZSphere index.  (Sphere 0 can't be deleted)):
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

            def ZSphereGet(Property: 0=ZSpheres count, 1=xPos, 2=yPos, 3=zPos, 4=radius, 5=color, 6=mask, 7=ParentIndex(-1=none), 8=LastClickedIndex(-1=none), 9=TimeStamp; 10=ChildsCount, 11=ChildIndex(2nd index), 12=TimeStampCount, 13=TimeStampIndex, 14=flags, 15=Twist Angle, 16=Membrane, 17=X Re, Optional ZSphere index(0 based), Optional 2nd index(0 based)):
            """
    Gets information about the currently active ZSpheres tool. (Must be placed within ZSphereEdit command)
    Output: Returns the value of the specified property

    """
            pass

            def ZSphereSet(Property: 0=unused,  1=xPos, 2=yPos, 3=zPos, 4=radius, 5=color, 6=mask, 7=ParentIndex, 8=unused, 9=TimeStamp, 10=unused, 11=unused, 12=unused, 13=unused, 14=flags, 15=Twist Angle, 16=Membrane, 17=X Res, 18=Y Res, 19=Z Res, 20=XYZ Res, 21=UserValue, ZSphere index(0 based), New property value]):
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
