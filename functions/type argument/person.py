def profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

profile(
    name="Jaya",
    age=18,
    city="Rajahmundry",
    education="Diploma"
)