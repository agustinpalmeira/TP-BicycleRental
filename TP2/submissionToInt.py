import numpy as np
import pandas as pd


submission = pd.read_csv('/home/florencia/Escritorio/submission32.csv', low_memory=False)
submission.duration = submission.duration.astype(int)
submission.to_csv("submission32int.csv", index=False)

