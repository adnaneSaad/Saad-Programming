#!/usr/bin/env python3
import sys, os
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase

class FlightSim(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.disableMouse()
        self.setBackgroundColor(0.1, 0.4, 0.8)

        # 1. GROUND
        cm = CardMaker('ground')
        cm.setFrame(-1000, 1000, -1000, 1000)
        self.ground = self.render.attachNewNode(cm.generate())
        self.ground.setPos(0, 0, -50)
        self.ground.setHpr(0, -90, 0)
        self.ground.setColor(0.1, 0.3, 0.1, 1)
        
        # 2. LOAD PLANE
        self.raw_model = self.loader.loadModel("models/scene.gltf")

        # Create a clean 'plane' node
        self.plane = self.render.attachNewNode("plane_container")

        # Reparent the model to our clean node
        self.raw_model.reparentTo(self.plane)

        # CLEAR THE WEIRD ROTATION:
        # We rotate the raw_model until it looks 'flat' and 'forward'
        # Adjust these values (e.g., -45, 90, 180) until it sits perfectly straight
        self.raw_model.setHpr(0, 0, 0)

        self.plane.setScale(1.0)
        self.plane.setPos(0, 0, 0)

        # 3. CAMERA PIVOT
        self.cam_pivot = self.render.attachNewNode("pivot")
        self.camera.reparentTo(self.cam_pivot)
        self.camera.setPos(0, -50, 15)
        self.camera.lookAt(self.plane)

        # 4. CONTROLS
        self.keys = {"w": False, "s": False, "a": False, "d": False, "q": False, "e": False}
        for k in self.keys: 
            self.accept(k, self.set_k, [k, True])
            self.accept(f"{k}-up", self.set_k, [k, False])
        self.accept("escape", sys.exit)
        
        self.taskMgr.add(self.update, "Update")

    def set_k(self, key, val): 
        self.keys[key] = val

    def update(self, task):
        dt = globalClock.getDt()
        
        # W = Pitch Down, S = Pitch Up
        if self.keys["w"]: 
            self.plane.setP(self.plane.getP() + 60 * dt)
        if self.keys["s"]: 
            self.plane.setP(self.plane.getP() - 60 * dt)
        
        # Roll
        if self.keys["a"]: 
            self.plane.setR(self.plane.getR() + 80 * dt)
        if self.keys["d"]: 
            self.plane.setR(self.plane.getR() - 80 * dt)
        
        # Yaw
        if self.keys["q"]: 
            self.plane.setH(self.plane.getH() + 50 * dt)
        if self.keys["e"]: 
            self.plane.setH(self.plane.getH() - 50 * dt)

        # Movement (Relative to nose)
        self.plane.setPos(self.plane, (40 * dt, 0, 0))
        self.cam_pivot.setPos(self.plane.getPos())
        return task.cont

if __name__ == "__main__":
    app = FlightSim()
    app.run()
