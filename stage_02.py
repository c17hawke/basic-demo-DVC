STAGE = "TWO"

with open("output.txt", "r") as f:
    content = f.read()

print(f"content read in stage {STAGE}: {content}")

with open("output2.txt", "w+") as f:
    f.write(f"stage {STAGE} started successfully..")