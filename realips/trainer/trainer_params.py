class OffPolicyTrainerParams:
    def __init__(self):
        self.gamma_discount = 0.99
        self.rm_size = 1000000
        self.batch_size = 128
        self.learning_rate_actor = 0.001
        self.learning_rate_critic = 0.0001
        self.is_remote_train = False
        self.actor_freeze_step_count = 5000
        self.use_prioritized_replay = False
        self.pre_fill_exp = 10000
        self.target_action_noise = False
        self.training_epoch = 1