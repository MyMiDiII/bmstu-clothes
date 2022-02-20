#version 330 core

in vec3 fragPos;
in vec3 normal;

uniform float ambientCoef;
uniform vec3 lightColor;
uniform vec3 lightPos;

uniform vec3 viewPos;
uniform vec4 curColor;

out vec4 fragColor;

void main()
{
    vec3 ambient = ambientCoef * lightColor;

    vec3 norm = normalize(normal);
    vec3 lightDir = normalize(lightPos - fragPos);
    float diff = dot(norm, lightDir);
    if (diff < 0) { diff = -diff; }
    vec3 diffuse = diff * lightColor;

    float specularStrength = 0.01;
    vec3 viewDir = normalize(viewPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 256);
    vec3 specular = specularStrength * spec * lightColor;

    fragColor = vec4((ambient + diffuse + specular) * vec3(curColor), 1.0);
}
