# Thông tin về các quận
districts_info = {
    "BĐ": {"Diện tích (km2)": 9.224, "Dân số": 247100},
    "BTL": {"Diện tích (km2)": 43.35, "Dân số": 333300},
    "CG": {"Diện tích (km2)": 12.04, "Dân số": 266800},
    "ĐĐ": {"Diện tích (km2)": 9.96, "Dân số": 420900},
    "HBT": {"Diện tích (km2)": 10.09, "Dân số": 318000}
}

# Tạo list chứa tên các quận và dân số tương ứng
districts = list(districts_info.keys())
populations = [info["Dân số"] for info in districts_info.values()]


# Tìm số thứ tự của quận có dân số cao nhất và thấp nhất
max_population_index = populations.index(max(populations))
min_population_index = populations.index(min(populations))

print("Indices of:")
print(f"- Most populated dist.: {max_population_index}")
print(f"- Least populated dist.: {min_population_index}")
# In ra tên của hai quận tương ứng
most_populated_district = districts[max_population_index]
least_populated_district = districts[min_population_index]

print("Tên của hai quận tương ứng:")
print(f"Most populated dist: {most_populated_district}")
print(f"Least populated dist.: {least_populated_district}")
areas = [info["Diện tích (km2)"] for info in districts_info.values()]

# Tạo list mới chứa mật độ dân số của các quận
population_densities = [info["Dân số"] / info["Diện tích (km2)"] for info in districts_info.values()]

# In ra mật độ dân số của các quận
print("Population density of:")
for district, density in zip(districts_info.keys(), population_densities):
    print(f"- {district}: {density}")
    # Tính mật độ dân số của từng quận
population_densities = [info["Dân số"] / info["Diện tích (km2)"] for info in districts_info.values()]

# Tính tổng mật độ dân số
total_population_density = sum(population_densities)

# Tính tổng số quận
total_districts = len(districts_info)

# Tính mật độ dân số trung bình
average_population_density = total_population_density / total_districts

# In ra mật độ dân số trung bình của các quận
print("Average population density:")
print(average_population_density)
