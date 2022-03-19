from emoji import emojize
import time

print("...CONTAGEM REGRESSIVA...")
for c in range(10, 0, -1):
    print("{}..".format(c))
    time.sleep(1)
print(emojize(":sparkles: :fireworks: :star2: :fireworks: :star2: :fireworks: :sparkles:", use_aliases=True))
