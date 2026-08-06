#version 330 core

in vec3 Normal;
out vec4 FragColor;

uniform vec3 lightDir;

void main() {
    float intensity = dot(normalize(Normal), normalize(lightDir));

    if (intensity > 0.75)
        intensity = 1.0;
    else if (intensity > 0.5)
        intensity = 0.7;
    else if (intensity > 0.25)
        intensity = 0.4;
    else
        intensity = 0.2;

    FragColor = vec4(vec3(intensity), 1.0);
}
