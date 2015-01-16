#! /usr/bin/env python
# -*- coding: utf-8 -*-

from jp.ac.kyoto_su.cse.wz.Bodies import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

TRACE = True
DEBUG = False

class Example(object):
    """例題プログラム：ドラゴンを実行する。"""
    
    @classmethod
    def main():
        """OpenGL立体データを読み込んで描画する。"""
        if TRACE: print __name__, main.__doc__
        
        a_model = DragonModel()
        a_model.open()
        
        a_model = WaspModel()
        a_model.open()
        
        a_model = BunnyModel()
        a_model.open()
        
        a_model = PenguinModel()
        a_model.open()
        
        a_model = OniModel()
        a_model.open()
        
        a_model = BabyModel()
        a_model.open()
        
        glutMainLoop()

        return 0