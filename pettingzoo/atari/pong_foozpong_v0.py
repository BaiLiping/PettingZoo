from .base_atari_env import BaseAtariEnv, base_env_wrapper_fn


def raw_env(num_players=4, **kwargs):
    assert num_players == 2 or num_players == 4, "pong only supports 2 or 4 players"
    mode_mapping = {2: 19, 4: 21}
    mode = mode_mapping[num_players]
    return BaseAtariEnv(game="pong", num_players=num_players, mode_num=mode, **kwargs)


env = base_env_wrapper_fn(raw_env)
