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

## javascript keywords(açarları) haqqında məlumat:
 - export
 - ixrac ifadəsi, funksiyalara, obyektlərə və ya ibtidai dəyərlərə canlı bağlamaları moduldan ixrac etmək üçün JavaScript modulları yaradarkən istifadə olunur, beləliklə (import) - idxal ifadəsi ilə digər proqramlar tərəfindən istifadə edilə bilər.
 İdxal edilən bağlamanın dəyəri onu ixrac edən modulda dəyişikliyə məruz qalır. Bir modul ixrac etdiyi bir bağlamanın dəyərini yenilədikdə, yeniləmə idxal olunan dəyərində görünəcək.

İxrac olunan modullar, belə elan etməyinizdən asılı olmayaraq ciddi rejimdədir (nəzarətdədri). İxrac ifadəsi daxil edilmiş skriptlərdə istifadə edilə bilməz.
 Statik idxal ifadəsi başqa bir modul tərəfindən ixrac edilən yalnız oxunan canlı bağlamaları idxal etmək üçün istifadə olunur.
 "Modul" tipli skriptlər tələb etməyən funksiyaya bənzər dinamik import () da var.

 - Extends
 - Extends(genişləndirmə) açarı class(sinif) bəyan edərkən və ya sinif yaratmaq üçün istifadə olunur
 - Extends açar sözü, xüsusi sinifləri və daxili obyektləri alt siniflərə qoymaq üçün istifadə edilə bilər.

 - False 
 - Hər hansı dəyərin səhv olduğunu bildirir 1>2 böyükdür bu səhvdir bunun üçün false açar sözündən istifadə olunur. Bu funksiya mwqayisə üçün faydalıdır.

 - Finally
 - bu açar ilə hər hansı göndərişin düzgün göndərilməsi vəya göndərilmədiyi haqqında məlumatı ekranda əks etdirir.(bu mesaj gondərildi və ya bu mesaj səhvdir error verir)
 - Finally () metodu bir vəd qaytarır. Söz yerinə yetirildikdə və ya rədd edildikdə, göstərilən geri çağırma funksiyası yerinə yetirilir. Bu, sözün müvəffəqiyyətlə yerinə yetirildiyinə və ya vəd edildikdən sonra rədd edilməsinə baxmayaraq kodun işlədilməsi üçün bir yol təqdim edir.
 - burada then və catch istifadə olunur ki kodun təkrarlanmasının qarşısını alır.

 - for
 - For ifadəsi, mötərizədə olan və nöqtəli vergüllə ayrılmış üç əlavə ifadədən ibarət olan bir döngə yaradır, sonra döngədə icra ediləcək bir ifadə (adətən bir blok ifadəsi).
 məsələn:
 for (let i = 0; i < 9; i++) {
   console.log(i);
   // more statements
}
    burada i 0-dan başlayaraq 9-a qədər bütün rəqəmlər yazlıacaq, çünki bu i-nin 9-dan kiçik olduğunu yoxlayır

 - function
 - Javascriptin hər funksiyası bir function obyektidir.




