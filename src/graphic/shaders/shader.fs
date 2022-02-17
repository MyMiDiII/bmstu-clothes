#version 330 core

uniform float ambientCoef;
uniform vec4 lightColor;
uniform vec4 curColor;

out vec4 FragColor;

void main()
{
    vec3 ambient = ambientCoef * vec3(lightColor);

    FragColor = vec4(ambient * vec3(curColor), lightColor.w * curColor.w);
}
