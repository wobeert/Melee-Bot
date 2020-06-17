from gym.envs.registration import register

register(
    id='melee-v0',
    entry_point='gym_melee.envs:MeleeEnv',
)
register(
    id='melee-extrahard-v0',
    entry_point='gym_melee.envs:MeleeExtraHardEnv',
)
