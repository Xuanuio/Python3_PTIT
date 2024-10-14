# sử dụng giải thuật để tìm ra độ dài dãy con không giảm dài nhất từ mảng ban đầu và sau đó
# có thể xác định được k phần tử ít nhất cần loại bỏ = n - độ dài dãy con không giảm dài nhất.
# Kế đó, sử dụng phương pháp backtrack để tìm tất cả các dãy con không giảm dài nhất 
# từ mảng ban đầu sau khi xóa đi k phần tử, tiếp đó lưu lại và in ra toàn bộ các dãy con đó.

def dp(n, a):
    # Tạo mảng res để lưu độ dài dãy con tăng kết thúc tại mỗi phần tử a[i]
    res = [1] * n  # Ban đầu, mỗi phần tử có thể tạo thành dãy con độ dài 1.
    
    # Duyệt qua các phần tử của mảng
    for i in range(1, n):
        for j in range(i):
            # Nếu a[i] >= a[j] và độ dài dãy con tại a[i] nhỏ hơn độ dài dãy con tại a[j] + 1
            if a[i] >= a[j] and res[i] < res[j] + 1:
                res[i] = res[j] + 1  # Cập nhật độ dài dãy con tăng tại a[i]
    
    # Trả về độ dài lớn nhất của dãy con tăng
    return max(res)

def find(n, a, max_len):
    # Hàm backtrack để tìm tất cả các dãy con tăng dài nhất
    def backtrack(idx, cur_list):
        if len(cur_list) == max_len:  # Nếu độ dài của dãy con hiện tại bằng max_len
            result.append(cur_list[:])  # Thêm mảng trung gian của dãy con vào result
            return
        # Duyệt qua các phần tử từ vị trí idx
        for i in range(idx, n):
            # Nếu mảng trung gian rỗng hoặc a[i] >= phần tử cuối cùng của mảng trung gian
            if not cur_list or a[i] >= cur_list[-1]:
                # Gọi đệ quy với phần tử a[i] thêm vào cur_list
                backtrack(i + 1, cur_list + [a[i]])

    result = []  # Mảng lưu tất cả các dãy con tăng dài nhất
    backtrack(0, [])  # Bắt đầu gọi backtrack từ vị trí 0
    return result

def solve(n, a):
    max_len = dp(n, a)  # Tìm độ dài của dãy con tăng dài nhất
    k = n - max_len  # Tính số phần tử cần loại bỏ
    all_lis = find(n, a, max_len)  # Tìm tất cả các dãy con tăng dài nhất
    return k, all_lis  # Trả về số phần tử ít nhất cần loại bỏ và tất cả các dãy con.


if __name__ == '__main__':
    tmp = input().split()  # Nhập vào dãy số dưới dạng chuỗi và tách thành các phần tử
    n = len(tmp)  # Số lượng phần tử trong dãy
    a = []
    
    # Chuyển từng phần tử từ chuỗi sang số (nguyên hoặc thực)
    for num in tmp:
        try:
            a.append(int(num))  # Chuyển đổi thành số nguyên
        except ValueError:
            try:
                a.append(float(num))  # Chuyển đổi thành số thực
            except ValueError:
                pass  
   
    k, all_list = solve(n, a)
    
    # In ra số phần tử cần loại bỏ và tất cả các dãy con tăng dài nhất
    print(f'K = {k}')
    print('All LIST:')
    for x in all_list:
        print(x)