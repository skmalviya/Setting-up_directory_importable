from gym.envs.registration import register

register(
    id='silpa-v0',
    entry_point='gym_silpa.envs:SilpaEnv',
)
