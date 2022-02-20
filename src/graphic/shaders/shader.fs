#version 330 core

in vec3 fragPos;
in vec3 normal;

uniform float ambientCoef;
uniform vec3 lightColor;
uniform vec3 lightPos;

uniform vec4 curColor;

out vec4 FragColor;

void main()
{
    vec3 ambient = ambientCoef * lightColor;

    vec3 norm = normalize(normal);
    vec3 lightDir = normalize(lightPos - fragPos);
    float diff = dot(norm, lightDir);

    if (diff < 0) { diff = -diff; }

    vec3 diffuse = diff * lightColor;

    FragColor = vec4((ambient + diffuse) * vec3(curColor), 1.0);
}
