import gym

from stable_baselines3 import DQN
from stable_baselines3.common.callbacks import CheckpointCallback

from mlagents_envs.environment import UnityEnvironment
from gym_unity.envs import UnityToGymWrapper


def main():
    unity_env = UnityEnvironment("./env/AutoDRIVE.x86_64", no_graphics = True)
    env = UnityToGymWrapper(unity_env, 0, uint8_visual=True)

    checkpoint_callback = CheckpointCallback(
        save_freq=1000,
        save_path="./logs/",
        name_prefix="rl_model",
        save_replay_buffer=True,
        save_vecnormalize=True,
    )

    model = DQN(
        "CnnPolicy",
        env,
        learning_rate=2.5e-4,
        buffer_size=50000,
        learning_starts=20000,
        train_freq=5,
        target_update_interval=50,
        exploration_fraction=0.05,
        exploration_final_eps=0.1,
        gamma=0.99,
        prioritized_replay=False,
        policy_kwargs=dict(dueling=True),
        verbose=1,
        tensorboard_log="./sb3_logs/"
    )

    model.learn(
        total_timesteps=1000000,
        callback=checkpoint_callback,
        log_interval=20
    )

    print("Saving model to unity_model.zip")
    model.save("unity_model")


if __name__ == "__main__":
    main()
