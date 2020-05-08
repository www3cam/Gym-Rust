from gym.envs.registration import register

register(
    id='RustEnvv0',
    entry_point='gym_rust.envs:RustEnv',
)
