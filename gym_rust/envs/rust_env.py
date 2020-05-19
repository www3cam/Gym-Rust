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
    self.action_space = spaces.MultiDiscrete([[0,1]])
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
    self.date = self.date + 1
    if self.date > 116:
        done1 = True
    else:
        done1 = False
    
    return [self.miles], 1., done1, {}
      
  def reset(self):
    # resetvals is the empirical distribution of the buses starting milage
    resetdate = [68,68,68,68,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    resetvals = [0.002208,0.001976,0.002445,0.001743,0.003369,0.016782,0.016037,0.012911,0.008958,0.003753,0.004445,0.017483,0.003083,0.01904,0.012215,0.016878,0.017925,0.00386,0.008364,0.02357,0.021487,0.004701,0.008577,0.015557,0.010105,0.019469,0.008254,0.005355,0.005539,0.005804,0.003023,0.002491,0.006556,0.008639,0.016147,0.00295,0.013175,0.011846,0.009728,0.004325,0.001888,0.017471,0.015879,0.020423,0.00613,0.00855,0.016019,0.019368,0.023614,0.017306,0.013301,0.007064,0.000504,0.000537,0.000508,0.000525,0.000586,0.000575,0.000504,0.000524,0.000517,0.000491,0.000483,0.000518,0.000523,0.000531,0.000545,0.002353,0.000129,0.003246,0.000532,0.001667,0.001758,0.002486,0.002145,0.004091,0.003146,0.000916,0.001137,0.002626,0.000182,0.002539,0.00164,0.002412,0.002033,0.002372,0.002487,0.001954,0.000741,0.001462,0.001321,0.001533,0.000921,0.001364,0.001277,0.001106,0.000554,0.000463,0.001325,0.000961,0.001914,0.001978,0.000432,0.000871]
    integer = np.random.randint(len(resetvals))
    
    self.miles = resetvals[integer]*1000000
    self.date =  resetdate[integer]
    return [self.miles]
    ...
  def render(self, mode='human', close=False):
    return False
