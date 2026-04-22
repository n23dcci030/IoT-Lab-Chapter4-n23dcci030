# BT3 — Wokwi GPIO Simulation

## Thông tin
- Nền tảng: Wokwi (Raspberry Pi Pico)
- Cảm biến: DHT22, HC-SR04
- Thiết bị: 3 LED (Red, Yellow, Green)

## Link mô phỏng
👉 https://wokwi.com/projects/461936763986735105

## Mô tả hoạt động
- Đọc nhiệt độ, độ ẩm từ DHT22
- Đo khoảng cách từ HC-SR04
- Xuất dữ liệu dạng CSV:
  timestamp,temperature,humidity,distance,status
- LED hiển thị trạng thái:
  - GREEN: bình thường
  - YELLOW/RED: cảnh báo

## Output mẫu
