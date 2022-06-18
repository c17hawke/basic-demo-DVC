STAGE = "THREE"

with open("output.txt", "r") as f:
    content = f.read()

print(f'out: {content}')

print(f"stage {STAGE} started successfully..")