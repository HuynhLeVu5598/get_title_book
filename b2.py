with open("output.txt", "r", encoding="utf-8") as read_file:
    content = read_file.readlines()

mycontent = ""
for c in content:
    mycontent += c


def remove_duplicates(text):
    # Tách các câu thành danh sách
    sentences = text.split("\n")
    # Sử dụng set để loại bỏ các câu trùng lặp
    unique_sentences = list(set(sentences))
    unique_list = []
    errors = ["®", "Vol"]
    for title in unique_sentences:
        for error in errors:
            if error in title:
                if len(title.split(error)[0]) > 5:
                    title = title.split(error)[0].strip()
            else:
                if len(title) > 5:
                    title = title.strip()
        if len(title) > 15:
            unique_list.append(title)
    unique_list = list(set(unique_list))

    # Gộp lại các câu không trùng lặp thành một chuỗi
    unique_text = "\n".join(unique_list)
    return unique_text


mytext = remove_duplicates(mycontent)
print(mytext)

with open("mylistunique.txt", "w", encoding="utf-8") as write_file:
    for ct in mytext:
        write_file.write(ct)
