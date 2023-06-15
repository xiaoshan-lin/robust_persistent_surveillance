"""
Env 2D
@author: huiming zhou
"""


class Env:
    def __init__(self, a, b):
        self.x_range = b+1  # size of background
        self.y_range = a+1
        self.motions = [(-0.5, 0), (-0.5, 0.5), (0, 0.5), (0.5, 0.5),
                        (0.5, 0), (0.5, -0.5), (0, -0.5), (-0.5, -0.5)]
        '''self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]'''
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        '''for i in range(x):
            obs.add((i, 0))
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
            obs.add((x - 1, i))'''

        return obs
