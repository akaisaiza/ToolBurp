import subprocess

def run_dalfox(target_url, options, output_file):
    command = f'dalfox scan {target_url} {options}'  # Lệnh DalFox cần chạy

    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        result = result.decode('utf-8')  # Chuyển đổi kết quả thành chuỗi văn bản
        
        if output_file:
            with open(output_file, 'w') as file:
                file.write(result)  # Ghi kết quả vào tệp văn bản
            print(f'Kết quả đã được xuất ra file {output_file}')
        else:
            print(result)  # In kết quả của DalFox
    except subprocess.CalledProcessError as e:
        print(f'Lỗi khi chạy DalFox: {e.output.decode("utf-8")}')

# Lấy thông tin từ người dùng
target_url = input('Nhập URL cần kiểm tra: ')
options = input('Nhập các tùy chọn của DalFox (nếu có): ')
output_file = input('Nhập tên tệp văn bản để xuất kết quả (hoặc nhấn Enter để không xuất file): ')

run_dalfox(target_url, options, output_file)

