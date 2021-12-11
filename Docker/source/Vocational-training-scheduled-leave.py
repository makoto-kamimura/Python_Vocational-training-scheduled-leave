print("※ ご利用の際には、本Gitリポジトリにおける README 下部に記載している Note をお読みの上ご利用ください。")

# 予定している授業日数の入力
lesson_Day = int(input("予定している授業日数を入力してください(※数値のみ): "))

# 一日の授業時間の入力
lesson_Hour = int(input("一日の授業時間を入力してください(※数値のみ): "))

# 予定している授業時間(1d/6h)
lesson_Time = (lesson_Day * lesson_Hour)

# 必要出席時間(80%)
lesson_Necessary_Time = (lesson_Time * 0.8)

# 欠席可能時間
lesson_Absence_Time = (lesson_Time - lesson_Necessary_Time)

# 欠席可能日数
lesson_absenceday = (lesson_Absence_Time / lesson_Hour)

#各情報出力
print("予定総授業:", lesson_Time, "時間")
print("所定出席:", lesson_Necessary_Time, "時間")
print("欠席可能:", lesson_absenceday, "日")
print("欠席可能:", lesson_Absence_Time, "時間")
print("※ 訓練校毎に所定条件等がございますので、そちらをご確認の上のご利用をお願い致します。")
input("Enter:終了")