#version 330 core

layout (location = 0) in vec3 vrtx;
layout (location = 1) in vec3 vrtxNormal;

out vec3 fragPos;
out vec3 normal;

uniform mat4 perspective;
uniform mat4 view;
uniform mat4 model;

void main()
{
    gl_Position = perspective * view * model * vec4(vrtx, 1.0f);
    fragPos = vec3(model * vec4(vrtx, 1.0f));
    normal = vrtxNormal;
}

