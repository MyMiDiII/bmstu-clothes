#version 330 core

layout (location = 0) in vec3 vrtx;

uniform mat4 transform;

void main()
{
    gl_Position = transform * vec4(vrtx, 1.0f);
}

