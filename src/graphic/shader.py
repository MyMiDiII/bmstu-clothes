import OpenGL.GL as gl
from graphic.config import SHADER_PATH

# !!! если что-то не так, проверь value_ptr


class Shader:
    def __init__(self, vsFilename, fsFilename):
        self.programID = self.__getProgram(SHADER_PATH + vsFilename,
                                           SHADER_PATH + fsFilename)


    def __getProgram(self, vsFilename, fsFilename):
        vShader = self.__getShader(vsFilename, "v")
        fShader = self.__getShader(fsFilename, "f")

        shaderProgram = gl.glCreateProgram()
        gl.glAttachShader(shaderProgram, vShader)
        gl.glAttachShader(shaderProgram, fShader)
        gl.glLinkProgram(shaderProgram)
        self.__checkCompileErrors(shaderProgram, "program")

        gl.glDeleteShader(vShader)
        gl.glDeleteShader(fShader)

        return shaderProgram


    def __readShader(self, filename):
        shaderText = None

        try:
            with open(filename, "r") as file:
                shaderText = file.read() 
        except:
            print("No shader file!")

        return shaderText


    def __getShader(self, filename, shaderType):
        shaderText = self.__readShader(filename)

        shader = gl.glCreateShader(gl.GL_VERTEX_SHADER
                                       if shaderType == "v" else
                                           gl.GL_FRAGMENT_SHADER)
        gl.glShaderSource(shader, shaderText)
        gl.glCompileShader(shader)
        self.__checkCompileErrors(shader, "shader")

        return shader


    def __checkCompileErrors(self, obj, mode):
        if mode == "shader":
            success = gl.glGetShaderiv(obj, gl.GL_COMPILE_STATUS)

            if not success:
                infoLog = gl.glGetShaderInfoLog(obj)
                print("Shader compilation error!" + infoLog.decode())
        else:
            success = gl.glGetProgramiv(obj, gl.GL_LINK_STATUS)

            if not success:
                infoLog = gl.glGetProgramInfoLog(obj)
                print("Program linking error!\n" + infoLog.decode())

    def use(self):
        gl.glUseProgram(self.programID)

    def setVec4(self, name, *values):
        location = gl.glGetUniformLocation(self.programID, name)

        if len(values) == 1 and type(values[0]) == glm.vec4:
            gl.glUniform4fv(location, 1, *values)
        elif (len(values) == 4):
            gl.glUniform4f(location, *values)
