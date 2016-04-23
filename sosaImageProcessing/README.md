# sosaImageProcessing

## 다이어그램
 ![diagram](/diagram.png "diagram")

## 사용법
### ImageProcessing("Client에서 받은 이미지 경로", "흑백이미지를 저장할 이미지 경로")
### example : ImageProcessing("input/input.png", "save/save.png")

## 메서드 설명
### 1. __init__
#### ImageProcessing 클래스의 생성자로 클라이언트에서 받은 이미지 경로를 저장한 후 main 메서드를 호출한다.
#### INPUT_IMAGE : 클라이언트에서 받은 이미지 경로
#### SAVE_IMAGE : 흑백 이미지를 저장할 이미지 경로

### 2. main (전체 메서드를 실행하는 메서드)
#### img 변수에 cv2.imread를 통해 클라이언트에서 받은 이미지를 RGB 형태로 호출한다.
#### img_YCrCb 변수에 RGB형태의 이미지를 YCrCb의 형태로 바꿔 저장한다.
#### img_binary 변수에 setPreprocessing(img_YCrCb) 메서드의 결과값을 저장한다.
#### setPreprocessing 메서드는 skin color를 검출하여 흑백사진으로 변환한다.
#### cv2.imwrite를 사용하여 흑백이미지를 저장한다.
#### diff_percentage 변수에 get_image_pixel_similarity 메서드의 결과값을 저장한다.
#### get_image_pixel_similarity 메서드는 이미지의 타원 안의 살색의 비율을 리턴한다. (살색/타원)*100
#### image_matching을 통해 가장 유사한 이미지의 경로를 반환한다.

### 3. image_matching
#### get_image_pixel_similarity를 통해 나온 살색 비율을 넣는다.
#### 비율에 따라 가장 유사한 이미지의 경로를 반환한다.

### 4. setPreprocessing
#### YCrCb로 그려진 이미지의 skin color를 검출하여 흑백사진으로 반환한다.

### 5. get_image_pixel_similarity
#### img1 : client에서 서버로 전송된 이미지의 경로
#### img2 : 540*960 크기의 검은 reference image
#### 살색의 비율을 검출하는 메서드 ( Percentage를 반환한다.)

