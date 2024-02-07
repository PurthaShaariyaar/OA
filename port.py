# Required modules
import math
import os
import random
import re
import sys

def sentTimes(numberOfPorts, transmissionTime, packetIds):
    # Keeps track of the next available time for each port
    portAvailability = [0] * numberOfPorts
    # Stores the final port each packet is sent to
    finalPorts = []

    currentTime = 1
    for packetId in packetIds:
        desiredPort = packetId % numberOfPorts
        # Find the next available port
        while currentTime < portAvailability[desiredPort]:
            desiredPort = (desiredPort + 1) % numberOfPorts

        # Update the port's next available time
        portAvailability[desiredPort] = max(currentTime, portAvailability[desiredPort]) + transmissionTime
        # Record the port to which the packet is sent
        finalPorts.append(desiredPort)
        currentTime += 1

    return finalPorts

numberOfPorts = 3
transmissionTime = 2
packetIds = [4, 7, 10, 6]
output = sentTimes(numberOfPorts, transmissionTime, packetIds)
print(output)
