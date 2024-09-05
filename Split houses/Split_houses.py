def split_houses(n, village):
    # تحويل السلسلة إلى قائمة لتسهيل التعديلات
    village_list = list(village)
    
    # عدد الأسوار التي نحتاج لوضعها
    fences_needed = 0
    
    # نقوم بإنشاء قائمة من التعديلات المحتملة
    for i in range(n):
        if village_list[i] == 'H':
            # وضع أسوار على اليمين واليسار من المنازل
            if i > 0 and village_list[i - 1] == '.':
                village_list[i - 1] = 'B'
                fences_needed += 1
            if i < n - 1 and village_list[i + 1] == '.':
                village_list[i + 1] = 'B'
                fences_needed += 1
    
    # تحويل القائمة المعدلة إلى سلسلة
    modified_village = ''.join(village_list)
    
    # التحقق مما إذا كان التعديل يلبي الشروط
    for i in range(n):
        if village[i] == 'H':
            left = i
            while left >= 0 and village[left] != 'H':
                left -= 1
            right = i
            while right < n and village[right] != 'H':
                right += 1
            if left >= 0 and village[left] == 'H':
                left += 1
            if right < n and village[right] == 'H':
                right -= 1
            if left == i and right == i:
                continue
            if not (i - left == right - i):
                return "NO\n"

    return f"YES\n{modified_village}"

# قراءة المدخلات
n = int(input().strip())
village = input().strip()

# تنفيذ الدالة وعرض النتيجة
result = split_houses(n, village)
print(result)

