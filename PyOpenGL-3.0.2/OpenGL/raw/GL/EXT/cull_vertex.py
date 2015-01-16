'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_cull_vertex'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_cull_vertex',False)
_p.unpack_constants( """GL_CULL_VERTEX_EXT 0x81AA
GL_CULL_VERTEX_EYE_POSITION_EXT 0x81AB
GL_CULL_VERTEX_OBJECT_POSITION_EXT 0x81AC""", globals())
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glCullParameterdvEXT( pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glCullParameterfvEXT( pname,params ):pass


def glInitCullVertexEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )