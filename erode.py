import matplotlib.pyplot as plt

img = plt.imread('rice.pgm')
h, w = img.shape
original = img
print("Height:", h)
print("Width:", w)

eroded = [[0 for x in range(w)] for y in range(h)]
dil = [[0 for x in range(w)] for y in range(h)]
opening = [[0 for x in range(w)] for y in range(h)]
closing = [[0 for x in range(w)] for y in range(h)]
for y in range(h):
    for x in range(w):
        punkt = 0 if img[y, x] < 128 else 255

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                nachbar_y = y + dy
                nachbar_x = x + dx

                if 0 <= nachbar_y < h and 0 <= nachbar_x < w:
                    nachbar = 0 if img[nachbar_y, nachbar_x] < 128 else 255
                    if nachbar < punkt:
                        punkt = 0
                        break

            if punkt == 0:
                break

        eroded[y][x] = punkt

for y in range(h):
    for x in range(w):
        punkt = 0 if original[y, x] < 128 else 255

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                nachbar_y = y + dy
                nachbar_x = x + dx

                if 0 <= nachbar_y < h and 0 <= nachbar_x < w:
                    nachbar = 0 if original[nachbar_y, nachbar_x] < 128 else 255
                    if nachbar > punkt:
                        punkt = 255
                        break

            if punkt == 0:
                break

        dil[y][x] = punkt

fig, achsen = plt.subplots(1, 3, figsize=(15, 5))

achsen[0].imshow(original, cmap='gray', vmin=0, vmax=255)
achsen[0].set_title('Original')
achsen[0].axis('off')

achsen[1].imshow(dil, cmap='gray', vmin=0, vmax=255)
achsen[1].set_title('Dilation')
achsen[1].axis('off')

achsen[2].imshow(eroded, cmap='gray', vmin=0, vmax=255)
achsen[2].set_title('Erosion')
achsen[2].axis('off')

plt.tight_layout()
plt.show()