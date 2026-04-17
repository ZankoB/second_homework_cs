import numpy as np

cpi_values = [8.207661, 40.317486, 46.606413, 47.593928,
              48.403651, 49.565766, 50.794706, 52.113216,
              40.249839, 40.763689, 41.341614, 41.666590,
              41.615621, 43.073711, 45.481101, 46.190685]

mean_cpi = np.mean(cpi_values)
cpi_std_dev = np.std(cpi_values, ddof=1)

misses = [] 
hits = []

print(f"Mean CPI: {mean_cpi}, Std Dev: {cpi_std_dev}")

if misses and hits and len(misses) == len(hits):
    miss_ratio = []
    for miss, hit in zip(misses, hits):
        if miss + hit > 0:
            miss_ratio.append(miss / (miss + hit))
        else:
            miss_ratio.append(0)

    mean_miss_ratio = np.mean(miss_ratio)
    miss_ratio_std_dev = np.std(miss_ratio, ddof=1)

    print(f"Mean Miss Ratio: {mean_miss_ratio}, Std Dev: {miss_ratio_std_dev}")