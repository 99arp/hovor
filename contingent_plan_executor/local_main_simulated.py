from hovor.core import simulate_interaction
from local_run_utils import *


def run_local_conversation(output_files_path):
    simulate_interaction(initialize_local_run(output_files_path))


def simulate_local_conversation(output_files_path, simulated_out_path):
    simulate_interaction(initialize_local_run_simulated(output_files_path), simulated_out_path)


if __name__ == "__main__":
    simulate_local_conversation(
        "C:\\Users\\Rebecca\\Desktop\\work\\coding\\plan4dial\\plan4dial\\local_data\\rollout_no_system_gold_standard_bot\\output_files",
        "sample_conversations/gold_standard_bot"
    )
