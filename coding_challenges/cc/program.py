import re

class RunLengthEncoding:
    def encode(self, message: str) -> str:
        result = []

        for c in message:
            if len(result) == 0:
                result.append([c])
            elif result[-1][0] == c:
                result[-1].append(c)
            else:
                result.append([c])
        return ''.join([r[0] if len(r) == 1 else f'{len(r)}{r[0]}' for r in result])


    def decode(self, message: str) -> str:
        result = ''
        for group in [match.group() for match in re.finditer(r"[0-9]*[A-Za-z\s]", message)]:
            if len(group) == 1:
                result = result + group[0]
            else:
                multiplier, char = group[-1], int(group[0:len(group) - 1])
                result = result + (multiplier * char)
        return result

