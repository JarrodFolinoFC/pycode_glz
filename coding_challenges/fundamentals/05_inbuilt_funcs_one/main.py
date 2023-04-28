def described_input(input):
    return f'Is String: {isinstance(input, str)}, Is Integer: {isinstance(input, int)}'

def described_input_v2(input):
    return f'Type: {type(input)}, Length: {len(input)}'
