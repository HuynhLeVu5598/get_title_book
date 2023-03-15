# Đọc nội dung 2 file vào 2 list
with open("a.txt", "r", encoding="utf-8") as file_a:
    a = file_a.read().splitlines()

with open("b.txt", "r", encoding="utf-8") as file_b:
    b = file_b.read().splitlines()

# Kiểm tra và xóa phần tử trùng nhau
for item_a in a:
    for item_b in b:
        if len(set(item_a.split()).intersection(set(item_b.split()))) >= 2:
            b.remove(item_b)
            # break

# Ghi lại nội dung của list b vào file b.txt
with open("b_new.txt", "w", encoding="utf-8") as file_b:
    for item in b:
        file_b.write("%s\n" % item)
