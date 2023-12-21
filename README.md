# Fly_Swatter

Fly_Swatter is a fire control computer that calculate ballistics and angle to launch a projectile to hit a moving object. 

Examples contains a working example of the computer. 

![image](https://github.com/pvalle6/Fly_Swatter/assets/103479060/6501e363-5df1-4e3e-8a6b-2d28f2fcfab7)

![image](https://github.com/pvalle6/Fly_Swatter/assets/103479060/f454004c-f801-45d4-9b17-4b633c229a20)

![image](https://github.com/pvalle6/Fly_Swatter/assets/103479060/d2a03fbd-b9bf-4e0d-abda-1e491026e5ef)

## To Install:
```
!git clone https://github.com/pvalle6/Fly_Swatter.git
!mv /content/Fly_Swatter/setup.py /content/setup.py
!pip install .
```
## Requirements:
```
numpy
scipy
time
sched
random
matplotlib
```
## Before submitting PR, run tests

```python
!python -m unittest /content/Fly_Swatter/tests/test_fire.py
!python -m unittest /content/Fly_Swatter/tests/test_radar.py
!python -m unittest /content/Fly_Swatter/tests/test_target.py
```

