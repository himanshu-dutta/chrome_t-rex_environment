from gym.envs.registration import register

register(
    id='Chrome_Trex-v0',
    entry_point='chrome_trex.envs:chrome_trex',
)