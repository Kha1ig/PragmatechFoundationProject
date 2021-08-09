justify-content və align-items arasında fərqlər nələrdir?
justify-content əsas ox boyunca işləyir və align isə xassələr Çapraz Axis üzərində işləyir.
justify-conntent və align-items hərəkətlərində oxşardır, fərq odur ki, justify-content əsas ox üzrə işləyir, ancaq align-items kəsişən oxlar üzrə işləyir.
align-content çox xətli konteynerlərdə işləyir və tək xətli konteynerlərə təsiri yoxdur.

Justify-content:space-around xüsusiyyəti maddələrin əvvəlində ortasında və sonrasında boşluqlar yaradır.

justify-content horizontal(üfüqi) ox boyunca:
flex-start- ox boyunca solda yerləşir
flex-end- ox boyunca sağda yerləşir
center- ox boyunca mərkəzdə yerləşir
space-between- ox boyunca bərabər paylayır
space-around-  ox boyunca bərabər paylayır bütün enlikdə (lakin kənarında boşluq olur)

align-items vertikal(y oxu boyunca):
flex-start- y oxu boyunca hündürlükdə yerləşir
flex-end- y oxu boyunca aşağıda yerləşir
flex end- y oxu boyunca mərkəzdə yerləşir
baseline- təməl xətlər eyni olur
stretch- hündürlükdə olmağa məcbur edir (sütunlar üçün əladır)

Flex-Shrink nədir

Flex-shrink xassəsi, konteynerin içərisində olan digər maddələrlə müqayisədə maddənin nə qədər kiçiləcəyini göstərir. Eyni qabın içərisinə yerləşdirilən digər elementlərlə müqayisədə bir elementin kiçilmə qabiliyyətini təyin edir.
Qeyd: Konteynerdəki maddə çevik deyilsə, flex-shrink xassəsi bu maddəyə təsir etməyəcək.

Flex-grow nədir
Flex-grow xüsusiyyəti, konteynerdəki digər maddələrlə müqayisədə maddənin nə qədər artacağını göstərir. Başqa sözlə, eyni qabda olan digər əşyalarla müqayisədə bir maddənin böyümək qabiliyyətidir.

Qeyd: Konteynerdəki maddə çevik deyilsə, flex-grow xüsusiyyəti bu maddəyə təsir etməyəcək.