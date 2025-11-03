# گرفتن تعداد درس‌ها
tedad_dars = int(input("تعداد درس‌ها را وارد کنید: "))

# گرفتن نمرات
nomarat = []
for i in range(tedad_dars):
    nomre = float(input(f"نمره درس {i+1} را وارد کنید: "))
    nomarat.append(nomre)

# محاسبه میانگین
miangin = sum(nomarat) / len(nomarat)

# نمایش وضعیت
if miangin < 10:
    print("مشروط")
elif miangin < 17:
    print("قبول")
else:
    print("عالی")