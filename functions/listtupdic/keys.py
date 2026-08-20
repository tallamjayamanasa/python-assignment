def greater_than_50(data):
    result = []

    for key, value in data.items():
        if value > 50:
            result.append(key)

    return result

marks = {
    "Math": 75,
    "Science": 45,
    "English": 65,
    "Social": 40
}

print(greater_than_50(marks))