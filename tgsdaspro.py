suhu_badan = float(input("Masukkan suhu badan: "))

if 36.5 <= suhu_badan <= 37.5:
    print("Suhu badan normal")
elif 30 <= suhu_badan < 36.5 or 37.5 < suhu_badan <= 100:
    print("Suhu badan tidak normal")
else:
    print("Suhu badan tidak masuk akal")