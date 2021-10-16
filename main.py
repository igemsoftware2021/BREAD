#Import Neccesary packages and libraries

import cadquery as cq
import math
import sys
import module

def basic(Volume,H_D):

    #Get Volume and H:D Ratio

    Volume = int(Volume)
    H_D = float(H_D)

    #Compute rest of the Dimensions

    TotalVolume = int(10/8*Volume)*pow(10,6)
    #Diameter = pow((4/math.pi)*TotalVolume,1/3)
    Diameter=pow(24*TotalVolume/(5*math.pi),1/3)
    Height = Diameter*H_D
    Thickness = 2
    BaseThickness = 2
    Radius = Diameter/2
    BaffleLen = Diameter/8
    BaffleWid = BaffleLen/2

    #Make Tank

    Tank = module.dishedtank(Volume,H_D,Thickness)
    #Compute Shaft Diameter

    ShaftDiameter = Diameter / 100

    if ShaftDiameter<5:
        ShaftDiameter = 5
    else :
        ShaftDiameter = ShaftDiameter

    center = Height/4

    #Make Shaft

    Shaft = module.Shaft(center,ShaftDiameter,Height)

    #Baffle Parameters

    Baffle_count=4

    #Make Baffles

    Baffles = module.Baffles(Baffle_count,Radius,BaffleLen,BaffleWid,Height)

    #Join Tank with Baffles+Shaft

    Tank = Tank.union(Baffles,clean=False)

    #Impeller Parameters

    Hub_Diameter=Diameter/12
    Hub_Height=Hub_Diameter

    Blade_Length=(Diameter*0.45)-Hub_Diameter
    Blade_Angle=45
    Blade_Thickness=2.0
    Blade_Height=3/4*Hub_Height/math.sin(math.degrees(Blade_Angle))
    Blade_Count=4

    #Make Impeller

    Impeller=module.Pitchblade(ShaftDiameter,Hub_Diameter,Blade_Length,Hub_Height,Blade_Angle,Blade_Thickness,Blade_Height,Blade_Count)

    #Join Impeller With Shaft

    Impeller = Impeller.translate((0,0,center)).union(Shaft)

    #Join Reactor with Impeller

    Reactor = Tank.union(Impeller,clean=0)

    #Export as .stl

    cq.exporters.export(Reactor,'Reactor.stl')

    #Export as .STEP

    cq.exporters.export(Reactor, 'Reactor.step')

def advanced(Volume,H_D,BaffleLen,BaffleWid,Thickness,BaseThickness,ShaftDiameter,Baffle_count,Hub_Diameter,Hub_Height,Blade_Length,Blade_Angle,Blade_Thickness,Blade_Count):
    #Compute rest of the Dimensions

    TotalVolume = int(10/8*Volume)*pow(10,6)
    Diameter = pow((4/math.pi)*TotalVolume,1/3)
    #Diameter=pow(24*TotalVolume/(5*math.pi),1/3)
    Height = Diameter*H_D
    Radius = Diameter/2
    #Make Tank

    Tank = module.Tank(Radius,Thickness,BaseThickness,Height)

    #Compute Shaft Diameter

    if ShaftDiameter<5:
        ShaftDiameter = 5
    else :
        ShaftDiameter = ShaftDiameter

    center = Height/4

    #Make Shaft

    Shaft = module.Shaft(center,ShaftDiameter,Height)

    #Make Baffles

    Baffles = module.Baffles(Baffle_count,Radius,BaffleLen,BaffleWid,Height)

    #Join Tank with Baffles+Shaft

    Tank = Tank.union(Baffles,clean=0)

    #Impeller Parameters

    Blade_Height=3/4*Hub_Height/math.sin(math.degrees(Blade_Angle))

    #Make Impeller

    Impeller=module.Pitchblade(ShaftDiameter,Hub_Diameter,Blade_Length,Hub_Height,Blade_Angle,Blade_Thickness,Blade_Height,Blade_Count,center).translate()
    
    #Join Impeller With Shaft

    Impeller = Impeller.translate((0,0,center)).union(Shaft)

    #Join Reactor with Impeller

    Reactor = Tank.union(Impeller,clean=0)

    #Export as .stl

    cq.exporters.export(Reactor,'Reactor.stl')

    #Export as .STEP

    cq.exporters.export(Reactor, 'Reactor.step')


basic(50,2)
