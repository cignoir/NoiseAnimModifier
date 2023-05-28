Python Script for Adding Noise to Animations in Maya
---
![image](https://github.com/cignoir/NoiseAnimModifier/assets/247498/dbfebe82-3fda-4de9-b295-3d7de2445c58)

This is a simple Python script for Maya that allows you to add noise to animations. One notable feature is the ability to apply an easing function to random noise.

![image](https://github.com/cignoir/NoiseAnimModifier/assets/247498/c3328e11-c9d5-48aa-9845-02e35efd7f06)

## Installation
1. Download the scripts from this repository. https://github.com/cignoir/NoiseAnimModifier/releases
2. Copy the `NoiseAnimModifier` folder to Maya's script directory such as `C:\Users\<name>\Documents\maya\scripts`.
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
