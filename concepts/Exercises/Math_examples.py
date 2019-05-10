import math
signal_power = 20
noise_power = 6
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print("Decibels:", decibels)
radians = 0.7
height = math.sin(radians)
print("Height:", height)
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
height = math.sin(radians)
print("Height:", height)
print("Square root of 2 divided by 2:", math.sqrt(2) / 2.0)
x = math.sin(degrees / 360.0 * 2 * math.pi)
print('x:', x)
x = math.exp(math.log(x+1))
print('x:', x)
