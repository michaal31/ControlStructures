
x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

if x == 0 and y == 0:
        print(f"Point P({x},{y}) is at the origin of the coordinate system")
elif x == 0:
        print(f"Point P({x},{y}) is on the Y-axis of the coordinate system")
elif y == 0:
        print(f"Point P({x},{y}) is on the X-axis of the coordinate system")
elif x > 0 and y > 0:
        print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
        print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
        print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x > 0 and y < 0:
        print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")

