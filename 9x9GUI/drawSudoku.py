import config

def buildHLineList():
	hLineList = []

	for line in range(0,config.cpl-1):

		startHLine = []
		endHLine = []
		newHLine = []

		startHLine.append(config.marginSize) #Start point x
		startHLine.append(config.marginSize+(config.cellSize*line)+config.cellSize) #Start point y
		endHLine.append(config.screenSize-config.marginSize)#End point x
		endHLine.append(config.marginSize+(config.cellSize*line)+config.cellSize)#End point y

		
		newHLine.append(startHLine)
		newHLine.append(endHLine)
	
		hLineList.append(newHLine)

	return hLineList


def buildVLineList():
	vLineList = []

	for line in range(0,config.cpl-1):
		startVLine = []
		endVLine = []
		newVLine = []

		startVLine.append(config.marginSize+(config.cellSize*line)+config.cellSize) #Start point x
		startVLine.append(config.marginSize) #Start point y

		endVLine.append(config.marginSize+(config.cellSize*line)+config.cellSize)#End point x
		endVLine.append(config.screenSize-config.marginSize)#End point y


		newVLine.append(startVLine)
		newVLine.append(endVLine)
	
		vLineList.append(newVLine)

	return vLineList