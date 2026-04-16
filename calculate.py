import numpy as np

cpi_values = [1.952457, 1.598015, 1.505979, 1.508824,
              1.487910, 1.466167, 1.462928, 1.583342,
              1.570440, 1.567650, 1.554371, 1.530762,
              1.542104, 1.535514, 1.511080, 1.470590]

mean_cpi = np.mean(cpi_values)
cpi_std_dev = np.std(cpi_values, ddof=1)

misses = [36127, 17431, 14323, 14295,
          13934, 13056, 13279, 13064,
          17052, 16611, 16117, 15975,
          15092, 15417, 15303, 14803] 
hits = [802195, 649063, 677537, 677256,
        686201, 694019, 692151, 695667,
        652732, 658158, 657705, 663384,
        669331, 665366, 668184, 677784]

miss_ratio = []

for miss, hit in zip(misses, hits):
    if miss + hit > 0:
        miss_ratio.append(miss / (miss + hit))
    else:
        miss_ratio.append(0)

mean_miss_ratio = np.mean(miss_ratio)
miss_ratio_std_dev = np.std(miss_ratio, ddof=1)

print(f"Mean CPI: {mean_cpi}, Std Dev: {cpi_std_dev}")
print(f"Mean Miss Ratio: {mean_miss_ratio}, Std Dev: {miss_ratio_std_dev}")