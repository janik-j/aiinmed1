import re

text = """
Epoch:   0%|          | 0/20 [00:00<?, ?epoch/s]
	Train Epoch: 1 	Loss: 1.870694 Acc@1: 37.639290 (ε = 2.78, δ = 0.1)
	Train Epoch: 1 	Loss: 1.521313 Acc@1: 51.265313 (ε = 4.88, δ = 0.1)
Epoch:   5%|▌         | 1/20 [00:25<08:10, 25.82s/epoch]
	Train Epoch: 2 	Loss: 0.879527 Acc@1: 73.743299 (ε = 6.70, δ = 0.1)
	Train Epoch: 2 	Loss: 0.814949 Acc@1: 75.952395 (ε = 8.20, δ = 0.1)
Epoch:  10%|█         | 2/20 [00:52<07:56, 26.45s/epoch]
	Train Epoch: 3 	Loss: 0.676986 Acc@1: 81.366120 (ε = 9.78, δ = 0.1)
	Train Epoch: 3 	Loss: 0.678645 Acc@1: 81.931848 (ε = 11.18, δ = 0.1)
Epoch:  15%|█▌        | 3/20 [01:18<07:25, 26.20s/epoch]
	Train Epoch: 4 	Loss: 0.625982 Acc@1: 83.894716 (ε = 12.64, δ = 0.1)
	Train Epoch: 4 	Loss: 0.616555 Acc@1: 84.268402 (ε = 13.84, δ = 0.1)
Epoch:  20%|██        | 4/20 [01:45<07:01, 26.31s/epoch]
	Train Epoch: 5 	Loss: 0.591769 Acc@1: 85.081581 (ε = 15.22, δ = 0.1)
	Train Epoch: 5 	Loss: 0.579098 Acc@1: 85.278059 (ε = 16.37, δ = 0.1)
Epoch:  25%|██▌       | 5/20 [02:12<06:40, 26.72s/epoch]
	Validation set: Loss: 0.289651 Acc: 92.943892 
	Train Epoch: 6 	Loss: 0.552787 Acc@1: 86.191972 (ε = 17.75, δ = 0.1)
	Train Epoch: 6 	Loss: 0.551069 Acc@1: 86.372237 (ε = 18.91, δ = 0.1)
Epoch:  30%|███       | 6/20 [02:39<06:13, 26.67s/epoch]
	Train Epoch: 7 	Loss: 0.535597 Acc@1: 86.583534 (ε = 20.20, δ = 0.1)
	Train Epoch: 7 	Loss: 0.522646 Acc@1: 87.096841 (ε = 21.33, δ = 0.1)
Epoch:  35%|███▌      | 7/20 [03:04<05:43, 26.38s/epoch]
	Train Epoch: 8 	Loss: 0.491882 Acc@1: 87.221206 (ε = 22.63, δ = 0.1)
	Train Epoch: 8 	Loss: 0.486973 Acc@1: 87.534384 (ε = 23.69, δ = 0.1)
Epoch:  40%|████      | 8/20 [03:32<05:20, 26.70s/epoch]
	Train Epoch: 9 	Loss: 0.485597 Acc@1: 87.688447 (ε = 24.93, δ = 0.1)
	Train Epoch: 9 	Loss: 0.488584 Acc@1: 87.966207 (ε = 26.01, δ = 0.1)
Epoch:  45%|████▌     | 9/20 [03:58<04:51, 26.53s/epoch]
	Train Epoch: 10 	Loss: 0.458325 Acc@1: 88.139416 (ε = 27.22, δ = 0.1)
	Train Epoch: 10 	Loss: 0.455704 Acc@1: 88.364202 (ε = 28.34, δ = 0.1)
Epoch:  50%|█████     | 10/20 [04:24<04:25, 26.53s/epoch]
	Validation set: Loss: 0.313254 Acc: 92.400568 
	Train Epoch: 11 	Loss: 0.461405 Acc@1: 88.630415 (ε = 29.49, δ = 0.1)
	Train Epoch: 11 	Loss: 0.473087 Acc@1: 88.642097 (ε = 30.54, δ = 0.1)
Epoch:  55%|█████▌    | 11/20 [04:51<03:59, 26.66s/epoch]
	Train Epoch: 12 	Loss: 0.452714 Acc@1: 89.011659 (ε = 31.72, δ = 0.1)
	Train Epoch: 12 	Loss: 0.430383 Acc@1: 89.317628 (ε = 32.76, δ = 0.1)
Epoch:  60%|██████    | 12/20 [05:19<03:34, 26.81s/epoch]
	Train Epoch: 13 	Loss: 0.398119 Acc@1: 90.049219 (ε = 33.93, δ = 0.1)
	Train Epoch: 13 	Loss: 0.420837 Acc@1: 89.655584 (ε = 34.96, δ = 0.1)
Epoch:  65%|██████▌   | 13/20 [05:44<03:05, 26.44s/epoch]
	Train Epoch: 14 	Loss: 0.416053 Acc@1: 89.557125 (ε = 36.11, δ = 0.1)
	Train Epoch: 14 	Loss: 0.417228 Acc@1: 89.568301 (ε = 37.09, δ = 0.1)
Epoch:  70%|███████   | 14/20 [06:11<02:39, 26.62s/epoch]
	Train Epoch: 15 	Loss: 0.397407 Acc@1: 89.876499 (ε = 38.28, δ = 0.1)
	Train Epoch: 15 	Loss: 0.384490 Acc@1: 90.426431 (ε = 39.29, δ = 0.1)
Epoch:  75%|███████▌  | 15/20 [06:39<02:14, 26.93s/epoch]
	Validation set: Loss: 0.308818 Acc: 92.986506 
	Train Epoch: 16 	Loss: 0.387987 Acc@1: 90.279677 (ε = 40.46, δ = 0.1)
	Train Epoch: 16 	Loss: 0.392181 Acc@1: 90.400348 (ε = 41.47, δ = 0.1)
Epoch:  80%|████████  | 16/20 [07:06<01:47, 26.95s/epoch]
	Train Epoch: 17 	Loss: 0.437742 Acc@1: 89.580380 (ε = 42.55, δ = 0.1)
	Train Epoch: 17 	Loss: 0.417760 Acc@1: 89.921583 (ε = 43.55, δ = 0.1)
Epoch:  85%|████████▌ | 17/20 [07:32<01:20, 26.81s/epoch]
	Train Epoch: 18 	Loss: 0.387639 Acc@1: 90.869645 (ε = 44.67, δ = 0.1)
	Train Epoch: 18 	Loss: 0.374644 Acc@1: 91.008429 (ε = 45.66, δ = 0.1)
Epoch:  90%|█████████ | 18/20 [07:59<00:53, 26.76s/epoch]
	Train Epoch: 19 	Loss: 0.380733 Acc@1: 91.220869 (ε = 46.81, δ = 0.1)
	Train Epoch: 19 	Loss: 0.372160 Acc@1: 91.303957 (ε = 47.75, δ = 0.1)
Epoch:  95%|█████████▌| 19/20 [08:26<00:26, 26.96s/epoch]
	Train Epoch: 20 	Loss: 0.377784 Acc@1: 90.742576 (ε = 48.86, δ = 0.1)
	Train Epoch: 20 	Loss: 0.384460 Acc@1: 90.649106 (ε = 49.83, δ = 0.1)
Epoch: 100%|██████████| 20/20 [08:54<00:00, 26.71s/epoch]
	Validation set: Loss: 0.341309 Acc: 91.903409 
"""

pattern = re.compile(r'(\d+\.\d+)s/epoch')

matches = re.findall(pattern, text)
print(matches)
print(len(matches))

# Convert matches to float and sum them up
total_seconds = sum(map(float, matches))

minutes = int(total_seconds // 60)
seconds = total_seconds % 60


print(f"Sum of 's/epoch' values: {minutes} min {seconds:.2f} s")
