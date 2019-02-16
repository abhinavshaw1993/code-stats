import code_stats.definitions as definitions

def validate_message_input(msg_type):
    assert msg_type in definitions.kTypeColorMap.keys()
