# Scripts
from lib.window import createWindow
from lib.buttons import createSelectFolderButton, createColorButton
from lib.labels import selectedLocLabel, explainationFolder, createPreview
from lib.commands import fileSelect, openColorPicker

# Create the window
mainWindow = createWindow()

# Add buttons to window
folderButton = createSelectFolderButton(mainWindow)
colorButton = createColorButton(mainWindow)

# Add labels to window
explainationLabel = explainationFolder(mainWindow)
folderLocationLabel = selectedLocLabel(mainWindow)
imgLabel = createPreview(mainWindow)

# Button commands
folderButton.configure(command=lambda: fileSelect(folderLocationLabel, imgLabel))
colorButton.configure(command=lambda: openColorPicker(folderLocationLabel))

# Start application
mainWindow.mainloop()