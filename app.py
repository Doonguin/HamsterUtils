# Scripts
from lib.window import createWindow
from lib.buttons import createSelectFolderButton
from lib.labels import selectedLocLabel, explainationFolder
from lib.commands import fileSelect

# Create the window
mainWindow = createWindow()

# Add buttons to window
folderButton = createSelectFolderButton(mainWindow)

# Add labels to window
explainationLabel = explainationFolder(mainWindow)
folderLocationLabel = selectedLocLabel(mainWindow)

# Button commands
folderButton.configure(command=lambda: fileSelect(folderLocationLabel))

# Start application
mainWindow.mainloop()