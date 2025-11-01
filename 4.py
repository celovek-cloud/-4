mandarini = int(input("Число мандаринов:"))
stupid_shcoklniki = int(input("Число школьников:"))
podelili = mandarini//stupid_shcoklniki
v_korzine = mandarini%stupid_shcoklniki
print(f"Каждому школьнику досталось {podelili} мандаринов")
print(f"В корзине осталось {v_korzine} мандаринов")