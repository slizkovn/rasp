24.02.2023


Для запуска нужно использовать main.py командой 
python main.py from_image to_image
где from_image - исходное изображение(например 1.png), to_image - результат

-=-=-=-=-=-

Для установки необходимых зависимостей:
pip install opencv-python


-=-=-=-=-=-

Для колибровки необходимо запустить colibration.py, который берет в том же каталоге фотографию .png и ищет на ней шахматную доску. В случае успеха программа выдаст что-то типа 

camera matrix:
 [[2.21683667e+04 0.00000000e+00 1.20839386e+03]
 [0.00000000e+00 1.90955028e+04 6.41530623e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
distortion coefficients:  [-1.05181947e+01 -4.46597883e+03 -2.48306773e-02 -1.96381917e-01
 -2.28701265e+01]

Эти параметры надо вставить в сооьветствующие места в main.py

camera_matrix = np.array( [[2.21683667e+04, 0.00000000e+00, 1.20839386e+03],
 [0.00000000e+00, 1.90955028e+04, 6.41530623e+02],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]);
dist_coefs = np.array([-1.05181947e+01, -4.46597883e+03, -2.48306773e-02, -1.96381917e-01, -2.28701265e+01]);

-=-=-=-=-=-

Сделано по инструкции с https://habr.com/ru/post/341160/
В common не хватало splitfn(file_path), взял из другого места.
Закоментил неиспользуемые библиотеки и 
#name = name[6].split(".")
#dst = dst[y:y+h-50, x+70:x+w-20] 
Добавил в main.py прием и обработку с помощью sys