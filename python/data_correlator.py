
def run():
    message_file = open("messages", "r")

    messages = message_file.read().split('\n')
    
    msg_len = 2
    previous = byteify_messages(messages[0], msg_len)
    current = messages[1]

    correlate_data(previous, current, 1)

def byteify_messages(previous, msg_len):
    previous_bytes = []
    for i in range(0, len(previous) -1, msg_len):
        previous_bytes.append(previous[i] + previous[i+1])
    return previous_bytes

def correlate_data(previous, current, additional_bytes):
    for byte in previous:
        if byte in current:
            print(f"data<{byte}> in current @{hex(current.find(byte))}")

if __name__ == "__main__":
    run()