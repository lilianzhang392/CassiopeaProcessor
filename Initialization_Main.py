import InitiatlizationMethods as init
from pathlib import Path
import DataMethods as dm

# should all be in the same recording directory from Savio (recordingOutputDir)
recordingHomeDir = Path('/Users/kve/Box/JellyHackers/SavioTransition/TrainingData_Pink_onSavio')

#automatic procurement from home directories if labeled right
pathOfPreInitializationDFDir = recordingHomeDir / 'Initialization_DF'
pathOfPreInitializationDFPath = dm.getCSVFilePaths(pathOfPreInitializationDFDir)[0]
pathOfInitializationStack = recordingHomeDir / 'Initialization_Stack'

init.initialization_Main(pathOfPreInitializationDFPath, pathOfInitializationStack, recordingHomeDir, True)

