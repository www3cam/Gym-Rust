# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:59:10 2020

@author: camer
"""
import gym
from gym import spaces
import numpy as np

class RustEnv(gym.Env):
    

  def __init__(self):
    super(RustEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    self.action_space = spaces.Discrete(2)
    # Example for using image as input:
    self.observation_space = spaces.Box(low=0., high=10000000., shape=(1,)
                    , dtype=np.float32)

  def step(self, action):
    if action == 0:
      self.miles = self.miles + max(0.,-1.98803789e-03*self.miles + 1.76937179e+03 + 1445.332*np.random.normal())
    elif action == 1:
      self.miles = 0. + max(0.,-1.98803789e-03*self.miles + 1.76937179e+03 + 1445.332*np.random.normal())/2.
    else:
      print('error')
    return self.miles, 1., {}
      
  def reset(self):
    # resetvals is the empirical distribution of the buses starting milage
    resetvals = [0.149858,0.31933,0.13089,0.142341,0.176891,0.216474,0.089922,0.089104,0.038809,0.200628,0.109107,0.147286,0.061203,0.13158,0.104112,0.012942,0.101319,0.361319,0.12113,0.062208,0.082705,0.013382,0.08872,0.324934,0.047613,0.043688,0.059446,0.343587,0.088952,0.07951,0.343533,0.052488,0.074105,0.302478,0.027272,0.171336,0.342004,0.034947,0.062743,0.258546,0.20585,0.036967,0.024282,0.24916,0.058025,0.252507,0.088772,0.068822,0.264614,0.210399,0.122706,0.230985,0.253507,0.235965,0.253877,0.000716,0.235119,0.229855,0.000346,0.238767,0.023883,0.077751,0.244103,0.007813,0.041524,0.100508,0.010741,0.251141,0.195578,0.243359,0.006782,0.232819,0.008956,0.084059,0.013364,0.105197,0.105156,0.249801,0.237104,0.047947,0.23621,0.262015,0.182153,0.227868,0.215093,0.145533,0.150465,0.138935,0.13154,0.087139,0.082139,0.092741,0.054712,0.086739,0.069248,0.100409,0.090724,0.091128,0.093754,0.08937,0.082123,0.096065,0.087327,0.078971]
    integer = np.random.randint(len(resetvals))
    
    self.miles = resetvals[integer]*1000000
    return self.miles
    ...
  def render(self, mode='human', close=False):
    return False
