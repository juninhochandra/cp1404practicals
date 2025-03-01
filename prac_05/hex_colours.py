COLOR_TO_CODE = {"AQUA": "#00ffff", "BLACK": "#000000", "BRONZE": "#cd7f32", "CELESTE": "#b2ffff", "COPPER": "#b87333",
                 "DARKVIOLET": "#9400d3", "EMERALD": "#50c878", "FAWN": "#e5aa70", "GRAY": "#bebebe", "IRIS": "#5a4fcf"}

color = input("Enter a color: ").upper()
while color != "":
    if color in COLOR_TO_CODE:
        print(COLOR_TO_CODE[color])
    else:
        print("Invalid color")
    color = input("Enter a color: ")