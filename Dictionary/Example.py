count = {}

message = 'God please guide me in joining amFOSS'

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
