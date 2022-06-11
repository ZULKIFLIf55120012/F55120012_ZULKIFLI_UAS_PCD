import cv2

# baca gambar
img = cv2.imread('burung.jpg')
cv2.imshow("original", img)

# Mengubah BGR ke RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# convert RGK ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
cv2.imshow("Hasil HSV", img)

#deklarasi batas warna
light =(50,20,20)
dark =(100, 255, 255)

# tresholding
mask = cv2.inRange(hsv, light, dark)
cv2.imshow("Hasil Tresholding", mask)

# impose gambar asli dengan mask
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
