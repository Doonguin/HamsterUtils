# Scripts
from lib.window import createWindow
from lib.buttons import createSelectFolderButton, createColorButton, createResetButton
from lib.labels import selectedLocLabel, explainationFolder, createPreview
from lib.commands import fileSelect, openColorPicker, resetColors

# Create the window
mainWindow = createWindow()

# Add buttons to window
folderButton = createSelectFolderButton(mainWindow)
colorButton = createColorButton(mainWindow)
resetButton = createResetButton(mainWindow)

# Add labels to window
explainationLabel = explainationFolder(mainWindow)
folderLocationLabel = selectedLocLabel(mainWindow)
imgLabel = createPreview(mainWindow)

# Button commands
folderButton.configure(command=lambda: fileSelect(folderLocationLabel, imgLabel))
colorButton.configure(command=lambda: openColorPicker(folderLocationLabel, folderLocationLabel.cget('text'), imgLabel))
resetButton.configure(command=lambda: resetColors(folderLocationLabel.cget('text'), imgLabel))

# Start application
mainWindow.mainloop()