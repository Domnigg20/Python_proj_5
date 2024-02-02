with open ("test.txt", "r") as f:

    f_contents = f.read(70)
    position = f.tell()
    print(f"Current position: {position} bytes")
    print(f_contents)

    f_seek = f.seek(120)
    print(f"Current position : {f_seek} bytes")
    print(f_contents)
