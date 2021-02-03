#授業予定日数取得
lesson_day = input("授業予定日数を入力！")

#予定授業時間
lesson_time = (int(lesson_day) * 6)

#必要出席時間
lesson_necessarytime = (lesson_time * 0.8)

#欠席可能時間
lesson_absencetime = (lesson_time - lesson_necessarytime)

#欠席可能日数
lesson_absenceday = (lesson_absencetime / 6)

#各情報出力
print("予定授業時間は", lesson_time)
print("必要出席時間は", lesson_necessarytime)
print("欠席可能時間は", lesson_absencetime)
print("欠席可能日数は", lesson_absenceday)
print("※あくまでの、参考までに！")
input("Enter 入力で終了！")