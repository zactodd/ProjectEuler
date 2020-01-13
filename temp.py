import os

f_str = "answer{:03d}.py"

answer_files = "Answers"
for f in os.listdir(answer_files):
    _, n = f.split("question")
    os.rename("Answers/" + f, f_str.format(int(n[:-3])))
