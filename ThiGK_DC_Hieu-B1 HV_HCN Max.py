from sys import stdin

# Bài này để Code tối ưu chỉ sử dụng giải thuật để tính S_HV_Max và S_HCN_Max mà không đi tìm các HV, HCN cụ thể.
# --> Output chỉ in ra S_HV_Max và S_HCN_Max. Thuật toán được sử dụng đã trình bày chi tiết ở dưới.

a, dp = [], []  # Khai báo toàn cục để lưu 2 mảng a và dp.

def hv_solve(n, m):
    ans = 0  # Lưu độ dài của cạnh HV Max.
    
    # Duyệt từng phần tử của mảng a để khởi tạo giá trị ban đầu của mảng dp.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = a[i][j]  
            if dp[i][j]:  
                ans = 1  # Các HV đơn vị
    
    # Tính toán giá trị của mảng dp cho các ô, dựa trên quy tắc: mỗi ô của mảng dp sẽ lưu cạnh của HV Max kết thúc tại ô này.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i][j]:  # Chỉ xét đến ô có giá trị = 1.
                if not a[i - 1][j] or not a[i][j - 1] or not a[i - 1][j - 1]:
                    # Nếu ô trên, ô trái hoặc ô chéo trên bên trái != 1, bỏ qua (do không thể tạo thành 1 HV).
                    continue
                # Tính cạnh của HV có S Max kết thúc tại dp[i][j] bằng cách lấy Min của 3 ô xung quanh nó (trên, trái, chéo trái) + 1. 
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                ans = max(ans, dp[i][j])  # Cập nhật kết quả.

    print(ans * ans)  # In ra S Max của HV.

def hcn_solve(n, m):
    # Memset cho a với mỗi phần tử a[i][j] đại diện cho chiều cao của dãy 1 liên tiếp tính từ hàng đầu tiên đến hàng thứ i.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i][j] == 1:
                a[i][j] += a[i - 1][j]  # Tăng chiều cao của dãy liên tiếp tại cột j.

    maxx = 0  # Biến lưu S HCN Max.
    
    # Với mỗi hàng, tính S HCN Max = cách duyệt ngược từ cuối về đầu.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_val = a[i][j]  # Chiều cao nhỏ nhất cho đến cột hiện tại j.
            for l in range(j, 0, -1):  # Duyệt từ cột j về 1.
                if a[i][l] != 0:  # Nếu gặp giá trị != 0, tính S HCN đó.
                    if min_val > a[i][l]:
                        min_val = a[i][l]  # Cập nhật chiều cao.
                    maxx = max(maxx, min_val * (j - l + 1))  # Tính S và cập nhật.
                else:
                    break  # Nếu gặp giá trị 0, kết thúc duyệt (Vì không thể tạo 1 HCN).

    print(maxx)  # In ra S HCN Max.

if __name__ == '__main__':
    m = 0  
    
    inp = [] 
    for line in stdin:  # Đọc toàn bộ DL đầu vào.
        tmp = list(map(int, line.split()))  
        m = len(tmp)  # Số phần tử trên 1 dòng chính là slg cột m của ma trận.
        inp.extend(tmp)  # Thêm dòng dữ liệu vào inp.

    if m == 0:  # Nếu không có DL:
        print('INVALID!')  
        exit() 

    n = len(inp) // m  # Tính n thông qua tổng số phần tử của ma trận và số cột m.
    idx = 0  # Chỉ số để duyệt qua inp.

    # Khởi tạo mảng a và dp với kích thước (n+1)x(m+1).
    a = [[0] * (m + 1) for _ in range(n + 1)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a[i][j] = int(inp[idx])  # Gán giá trị từ inp vào a[i][j].
            idx += 1

    print('OUTPUT_1: S_HV_Max = ', end = '')
    hv_solve(n, m)
    print('OUTPUT_2: S_HCN_Max = ', end = '')
    hcn_solve(n, m)