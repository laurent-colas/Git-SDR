#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:16:51 2020

@author: neuromap
"""
import numpy as np

class Words:
    def __init__(self):
        self.byte = 0
        
    def toBinary(self):
        binaryList = []
        # Transfer the data in binary array
        binaryList = [int(i) for i in list(format(self.byte, '08b'))]
        # Add the start and stop bit
        binaryList.insert(0,0)
        binaryList.append(1)
        
        return binaryList

class Preambule(Words):
    def __init__(self):
        self.byte = 170 # Corresponds to 0xAA
        
class StartFrame(Words):
    def __init__(self):
        self.byte = 114 # Corresponds to 0x72
        
class Type(Words):
    def __init__(self):
        self.byte = 0 #
        
class Address(Words):
    pass
        
class Sample(Words):
    pass

class Frame:
    def __init__(self):
        Pre = Preambule()
        Sta = StartFrame()
        Typ = Type()
        self.data = [Pre, Pre, Sta, Typ]
        
    def Add(self, Address, Sample):
        # Create address and sample object
        addr = Words()
        samp = Words()
        # Convert Hexadecimal Values to integers
        addr.byte = int(Address, 16)
        samp.byte = int(Sample, 16)
        # Append Frame data with the new Sample and its adress
        self.data.append(addr)
        self.data.append(samp)
    
    def toStream(self):
        stream =[]
        # Fetch all the words in the frame with the preambule
        for word in self.data:
            stream.extend(word.toBinary())
        
        # Add the end of frame
        stream.extend([1,1,1,1,1,1,1,1,1,1])
        return stream
    
    def toFile(self, filename, mult):
        stream = self.toStream()
        # Duplicate each element in stream mult times
        if mult != 0:
            multStream = []
            for element in stream:
                for i in range(mult):
                    multStream.append(element)
            newFile = open(filename + ".bin", "wb")
            newFile.write(bytes(multStream))
        else:
            newFile = open(filename + ".bin", "wb")
            newFile.write(bytes(stream))
            
# Main test
test = Frame()
test.Add("69", "42")
test.toFile("filename", 0)