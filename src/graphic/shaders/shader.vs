#version 330 core

layout (location = 0) in vec3 vrtx;

uniform mat4 perspective;
uniform mat4 model;

void main()
{
    gl_Position = perspective * model * vec4(vrtx, 1.0f);
}

