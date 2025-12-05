# dengan pernyataan continue kita dapat menghentikan iterasi saat ini dan melanjutkan ke iterasi berikutnya
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)