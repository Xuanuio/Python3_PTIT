if __name__ == '__main__':
    
    # Thay vì SD phương pháp Sinh, SD giải thuật cho bài này để tối ưu và xử lý được các testcase lớn 1 cách hiệu quả.
    
    n = int(input())

    # Khởi tạo 5 mảng cnt (với n+1 phần tử mỗi loại) để đếm số Hoán Vị kết thúc bằng các nguyên âm ueoai
    cnt_u, cnt_e, cnt_o, cnt_a, cnt_i = [0] * (n+1), [0] * (n+1), [0] * (n+1), [0] * (n+1), [0] * (n+1)

    # Bước khởi tạo: ban đầu = 1
    cnt_u[1], cnt_e[1], cnt_o[1], cnt_a[1], cnt_i[1] = 1, 1, 1, 1, 1

    # Tính toán: từ vị trí thứ 2 đến n:
    for i in range(2, n+1):
        # Số chuỗi kết thúc bằng 'u' ở vị trí i là tổng số chuỗi kết thúc bằng 'o' và 'i' ở vị trí i-1
        cnt_u[i] = cnt_o[i-1] + cnt_i[i-1]

        # Số chuỗi kết thúc bằng 'e' ở vị trí i là tổng số chuỗi kết thúc bằng 'a' và 'i' ở vị trí i-1
        cnt_e[i] = cnt_a[i-1] + cnt_i[i-1]

        # Số chuỗi kết thúc bằng 'o' ở vị trí i là số chuỗi kết thúc bằng 'i' ở vị trí i-1
        cnt_o[i] = cnt_i[i-1]

        # Số chuỗi kết thúc bằng 'a' ở vị trí i là tổng số chuỗi kết thúc bằng 'u', 'e' và 'i' ở vị trí i-1
        cnt_a[i] = cnt_u[i-1] + cnt_e[i-1] + cnt_i[i-1]

        # Số chuỗi kết thúc bằng 'i' ở vị trí i là tổng số chuỗi kết thúc bằng 'e' và 'o' ở vị trí i-1
        cnt_i[i] = cnt_e[i-1] + cnt_o[i-1]

    print(cnt_u[n] + cnt_e[n] + cnt_o[n] + cnt_a[n] + cnt_i[n])