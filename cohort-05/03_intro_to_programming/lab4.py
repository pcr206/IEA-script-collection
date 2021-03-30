minutes = 28435
hours = (minutes / 60)
days = (hours / 24)
print('Minutes:', minutes, 'Hours:', hours, 'Days:', days)
calculation1 = days * 24 + hours * 60
calculation2 = days * (24 + hours) * 60
calculation3 = (days * 24) + (hours * 60)
print("Cal1 ((19.74652777777778x24)+(473.9166666666667*60)):", calculation1)
print("Cal2 (19.74652777777778X(24+473.9166666666667)X60):", calculation2)
print("Cal3 ((19.74652777777778x24)+(473.9166666666667*60)):", calculation3)
###2nd option
hours = (minutes // 60)
days = (hours // 24)
print('Minutes:', minutes, 'Hours:', hours, 'Days:', days)
calculation1 = days * 24 + hours * 60
calculation2 = days * (24 + hours) * 60
calculation3 = (days * 24) + (hours * 60)
print("Cal1 ((19x24)+(473*60)):", calculation1)
print("Cal2 (19X(24+473)X60):", calculation2)
print("Cal3 ((19x24)+(473*60)):", calculation3)
