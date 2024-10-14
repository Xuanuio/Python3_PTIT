from sys import stdin  
import matplotlib.pyplot as plt  # Install và import thư viện matplotlib để vẽ đồ thị histogram.

# Xử lý Input đầu vào và lưu tần suất xuất hiện của mỗi từ vào dict.
# SD thư viện matplotlib để vẽ đồ thị histogram.
# Chú ý: Cần cài đặt thư viện matplotlib trước:
# Mở terminal: --> chạy lệnh: pip install matplotlib

if __name__ == '__main__':
    d = dict()  # Khởi tạo một dict để lưu số lần xuất hiện của mỗi từ
    translation_table = str.maketrans('.,:;!?', '      ')  # Tạo bảng dịch để thay thế các dấu câu bằng khoảng trắng.

    # Đọc toàn bộ Input đầu vào:
    for line in stdin:
        s = line.translate(translation_table)  # Thay thế các dấu câu trong dòng bằng khoảng trắng
        for x in s.split():  # Tách dòng thành các từ
            if x in d:  # Nếu từ đã tồn tại trong dict:
                d[x] += 1  # Tăng số lần xuất hiện của từ thêm 1
            else:  # Nếu từ chưa tồn tại trong dict:
                d[x] = 1  # Gán cho nó số lần xuất hiện là 1

    # Sắp xếp lại dict theo thứ tự giảm dần của số lần xuất hiện. (Nếu số lần xuất hiện bằng nhau thì sắp xếp theo thứ tự từ điển)
    sorted_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

    # In các từ và số lần xuất hiện theo thứ tự giảm dần:
    for x, freq in sorted_d:
        print(x, freq)

    # Vẽ đồ thị histogram
    words = [x for x, freq in sorted_d]  # Tạo danh sách các từ
    freqs = [freq for x, freq in sorted_d]  # Tạo danh sách số lần xuất hiện tương ứng của các từ

    plt.figure(figsize=(20, 10))  # Tạo một hình vẽ với kích thước 20x10 inch
    plt.bar(words, freqs, color='green')  # Vẽ biểu đồ cột với các từ trên trục x và số lần xuất hiện trên trục y
    plt.xlabel('Words')  # Đặt nhãn cho trục x
    plt.ylabel('Frequency')  # Đặt nhãn cho trục y
    plt.title('Word Frequency Histogram')  # Đặt tiêu đề cho biểu đồ
    plt.xticks(rotation=90)  # Xoay nhãn trục x 90 độ cho dễ đọc
    plt.tight_layout()  # Tự động điều chỉnh khoảng cách giữa các thành phần của biểu đồ
    plt.show()  # Show biểu đồ