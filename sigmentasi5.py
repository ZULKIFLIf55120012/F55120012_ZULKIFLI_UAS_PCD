import cv2

# baca gambar
gambar = cv2.imread('burung.jpg')

#tampilkan gambar asli
cv2.imshow("original", gambar)

# convert BGR ke RGB
rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)
cv2.imshow("Hasil RGB", rgb)

# convert RGK ke HSV
hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
cv2.imshow("Hasil HSV", hsv)

# deklarasi batas bawah (hijau cerah)
light_green = (2, 200, 200)
# deklarasi batas atas (dark hijau)
dark_green = (18, 255, 255)

# tresholding
mask = cv2.inRange(hsv, light_green, dark_green)
cv2.imshow("Hasil MASK", mask)

# impose gambar asli dengan mask
result = cv2.bitwise_and(gambar, rgb, mask=mask)
cv2.imshow("Hasil Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

