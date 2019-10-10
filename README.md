# Chrome T-Rex Environment

![](https://github.com/moriarity101/chrome_t-rex_environment/blob/master/images/Screenshot.png)

### Description:
Oen AI Gym Version for The Chrome T-Rex game.

### Technology:
Built using pygame and gym library. Additionally requires you to install numpy as well, which you  anyway would be having if you are looking for this, lol!

### Version and Release:
Version 1.0

### Target Platforms:
Windows/Linux

### Instructions and Prerequisites:   
To run this environment:  
* Make sure you have Python installed alongwith pygame (http://www.pygame.org/) library and gym library.
* Additionally it required you to have pip installed.
* In the main directory, open terminal and type the following:
    pip install -e Chrome-Trex
* This would install and register the following game as an Environmnet.
* Now, to import the environment in your code:
    import gym
    env = gym.make("chrome_trex:Chrome_Trex-v0")
  This will import the environmnet.

##### Description:
* Press UP or SPACE to make T-Rex jump over the obstacles
* Press DOWN key to crouch
* Avoid getting hit by obstacles. 

### Developed by: 
Himanshu Dutta
Email: meet.himanshu.dutta@gmail.com  

#### Credits:
* Sprites : https://chromedino.com/assets/offline-sprite-2x-black.png
* Logo : https://textcraft.net/
* Speech Bubble : http://pixelspeechbubble.com/
* Sounds : https://github.com/vicboma1/T-Rex-Game/tree/master/Unity/Sounds

#### References:
* http://www.pygame.org/docs
* https://github.com/wayou/t-rex-runner
* https://github.com/shivamshekhar/Chrome-T-Rex-Rush/
