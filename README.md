# Continuous Action Reinforcement Learning Automaton
This program is using CARLA method in parameter learning and image processing.<br/>

## CARLA method usage
Build a new files, include:
```
import CARLA
class Equation(CARLA):
	def Consume(self, ImaGourp):
		Consume function you need

Equ = Equation([[max1, min1], [max2, min2], ...], Work Method, Total Loop, gw, gh)
"""
Work Method = "-t": For test. It will print final values
Work Method = "-a": For learning Automatic. It will learning automatic and will print nothing.
Work Method = "-p": For presentation. It will print final values and final PDF figure.
"""
Solution = Equ.Algorithm()
print(Solution)
```
Then you can get your first CARLA method learning result.