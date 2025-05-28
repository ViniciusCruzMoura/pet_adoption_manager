from django.db import models
from django.utils import timezone
    
class Color(models.Model):
    name = models.CharField(
        verbose_name='Nome',
        max_length=10
    )
    def __str__(self):
        return f"""{self.name}"""
    class Meta:
        db_table = 'management_system_color'
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'
        managed = True
    
class Breed(models.Model):
    breed_type = models.CharField(
        verbose_name='Raça',
        max_length=50
    )
    def __str__(self):
        return f"""{self.breed_type}"""
    class Meta:
        db_table = 'management_system_breed'
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'
        managed = True

class AnimalType(models.Model):
    animal_type = models.CharField(
        verbose_name='Tipo de Animal',
        max_length=50
    )
    def __str__(self):
        return f"""{self.animal_type}"""
    class Meta:
        db_table = 'management_system_animaltype'
        verbose_name = 'Tipo de Animal'
        verbose_name_plural = 'Tipos de Animais'
        managed = True

class AnimalStatus(models.Model):
    animal_status = models.CharField(
        verbose_name='Situação do Animal',
        max_length=50
    )
    def __str__(self):
        return f"""{self.animal_status}"""
    class Meta:
        db_table = 'management_system_animalstatus'
        verbose_name = 'Situação do Animal'
        verbose_name_plural = 'Situações dos Animais'
        managed = True

class AnimalSize(models.Model):
    animal_size = models.CharField(
        verbose_name='Tamanho do Animal',
        max_length=50
    )
    def __str__(self):
        return f"""{self.animal_size}"""
    class Meta:
        db_table = 'management_system_animalsize'
        verbose_name = 'Tamanho do Animal'
        verbose_name_plural = 'Tamanhos dos Animais'
        managed = True

class Animal(models.Model):
    GENDER_CHOICES = (
        ('m', 'Macho'),
        ('f', 'Fêmea')
    )
    name = models.CharField(
        verbose_name='Nome', 
        max_length=100, 
        default=None, 
        blank=True, 
        null=True
    )
    # image = models.ImageField(
    #     verbose_name='Imagem', 
    #     upload_to ='uploads', 
    #     default=None, 
    #     blank=True, 
    #     null=True
    # )
    # image = models.ForeignKey(
    #     Images,
    #     verbose_name='Imagens',
    #     default=None, 
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL
    # )
    observation = models.CharField(
        verbose_name='Observação', 
        max_length=4000, 
        default=None, 
        blank=True, 
        null=True
    )
    pub_date = models.DateTimeField(
        verbose_name='Date de publicação', 
        default=None, 
        blank=True, 
        null=True
    )
    gender = models.CharField(
        verbose_name='Gênero',
        max_length=6, 
        choices=GENDER_CHOICES,
        default=None, 
        blank=True, 
        null=True
    )
    status = models.ForeignKey(
        AnimalStatus,
        verbose_name='Status',
        default=None, 
        blank=True, 
        null=True,
        on_delete=models.SET_NULL
    )
    size = models.ForeignKey(
        AnimalSize,
        verbose_name='Tamanho',
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    age = models.IntegerField(
        verbose_name='Idade',
        default=None, 
        blank=True, 
        null=True
    )
    # vaccinations = models.ManyToManyField(
    #     Vaccine,
    #     verbose_name='Vacinas',
    #     default=None, 
    #     blank=True
    # )
    color = models.ForeignKey(
        Color,
        verbose_name='Cor',
        default=None, 
        blank=True, 
        null=True,
        on_delete=models.SET_NULL
    )
    breed = models.ForeignKey(
        Breed,
        verbose_name='Raça',
        default=None, 
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    type = models.ForeignKey(
        AnimalType,
        verbose_name='Tipo de Animal',
        default=None, 
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    def img_preview(self):
        obj = Images.objects.filter(animal=self).order_by('-id')[:1] or None
        if obj is None:
            return ""
        return obj[0].img_preview()
    def __str__(self):
        return f"""{self.name}"""
    class Meta:
        db_table = 'management_system_animal'
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        managed = True

class Images(models.Model):
    file = models.ImageField(
        verbose_name='Arquivo', 
        upload_to ='uploads', 
        default=None, 
        blank=True, 
        null=True
    )
    animal = models.ForeignKey(
        Animal,
        verbose_name='Animais',
        default=None, 
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    def img_preview(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="80" height="80" />' % (self.file.url))
    #img_preview.short_description = 'Image'
    #img_preview.allow_tags = True
    def __str__(self):
        return f"""{self.file.name.replace('uploads/', '')}"""
    class Meta:
        db_table = 'management_system_images'
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        managed = True

class Telephone(models.Model):
    ddd = models.CharField(
        verbose_name='DDD',
        max_length=50
    )
    numero = models.CharField(
        verbose_name='Numero',
        max_length=50
    )
    def __str__(self):
        return f"""({self.ddd}) {self.numero}"""
    class Meta:
        db_table = 'management_system_telephone'
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
        managed = True
    
class Adopter(models.Model):
    name = models.CharField(
        verbose_name='Nome',
        max_length=100
    )
    phone = models.ForeignKey(
        Telephone,
        verbose_name='Telefone',
        default=None, 
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    email = models.CharField(
        verbose_name='Email',
        max_length=100
    )
    def __str__(self):
        return f"""{self.name}"""
    class Meta:
        db_table = 'management_system_adopter'
        verbose_name = 'Adotador'
        verbose_name_plural = 'Adotadores'
        managed = True

class Adoption(models.Model):
    fecha_solicitud = models.DateTimeField(
        verbose_name='Data de Inscrição',
        default=timezone.now
    )
    aprobada = models.BooleanField(
        verbose_name='Aprovada',
        default=False
    )
    fecha_aprobacion = models.DateTimeField(
        verbose_name='Data de Aprovação',
        blank=True, 
        null=True
    )
    animal_id = models.ForeignKey(
        Animal, 
        on_delete=models.CASCADE,
        verbose_name='Animal'
    )
    adopter_id = models.ForeignKey(
        Adopter, 
        on_delete=models.CASCADE,
        verbose_name='Adotador'
    )
    def __str__(self):
        return f"""{self.id}"""
    class Meta:
        db_table = 'management_system_adoption'
        verbose_name = 'Adoção'
        verbose_name_plural = 'Adoções'
        managed = True

class Vaccine(models.Model):
    name = models.CharField(
        verbose_name='Nome',
        max_length=50
    )
    animal = models.ForeignKey(
        Animal,
        verbose_name='Animais',
        default=None, 
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    def __str__(self):
        return f"""{self.name}"""
    class Meta:
        db_table = 'management_system_vaccine'
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        managed = True
