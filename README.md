Python Script for Adding Noise to Animations in Maya
---
![image](https://github.com/cignoir/NoiseAnimModifier/assets/247498/aecf209e-3049-4e34-b712-77f4a99eacbd)

This is a simple Python script for Maya that allows you to add noise to animations. One notable feature is the ability to apply an easing function to random noise.

## Installation
1. Download the scripts from this repository.
2. Copy the entire folder to Maya's script directory.
3. Register the following code in the shelf: `from NoiseAnimModifier import *; main_dialog = MainDialog(); main_dialog.show()`

## Usage
1. Select an object.
2. Select the attribute to which you want to add noise.
3. Set the strength and step of the noise.
4. Optionally, choose an easing function to apply. You can refer to the following page for different types: https://easings.net/
5. Once you have set any other necessary parameters, click the Apply button.

## Features
* Generate random noise and apply it to animation curves.
* Customize the noise parameters, such as frequency, amplitude.
* Apply easing functions to the generated noise for smoother animation effects.
* Control the noise application on specific objects, attributes, or keyframes.

## Easing functions from https://easings.net/
![image](https://github.com/cignoir/NoiseAnimModifier/assets/247498/e37e398e-5ef9-488c-b74c-f0c1bd0c48b2)

## Contributions
Contributions, bug reports, and feature requests are welcome! Please feel free to open an issue or submit a pull request on the GitHub repository.

## License
This script is licensed under the MIT License.
