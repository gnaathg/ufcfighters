from django.db import models

class Fighters(models.Model):

    name = models.CharField(max_length=30)

    age = models.CharField(max_length=30)

    country = models.CharField(max_length=30)

    gender_type = (

        ("male","male"),
        ("female","female")
    )

    gender = models.CharField(max_length=30,choices=gender_type)


    blood_type = (
        ("A+ve", "A+ve"),

        ("A-ve", "A-ve"),

        ("B+ve", "B+ve"),

        ("B-ve", "B-ve"),

        ("O+ve", "O+ve"),

        ("O-ve", "O-ve"),

        ("AB+ve", "AB+ve"),

        ("AB-ve", "AB-ve"),

    )

    blood = models.CharField(max_length=30, choices=blood_type)

    fighting_options = (

        ("sambo", "sambo"),

        ("brazilian jiu jitsu", "brazilian jiu jitsu"),

        ("muay thai", "muay thai"),

        ("taekwondo", "taekwondo"),

        ("boxing", "boxing"),

        ("mma", "mma"),

    )

    fighting_style = models.CharField(max_length=30, choices=fighting_options)

    weight_options = (

        ("featherweight", "featherweight"),

        ("bantamweight", "bantamweight"),

        ("lightweight", "lightweight"),

        ("heavyweight", "heavyweight"),

        ("flyweight", "flyweight"),

        ('middleweight','middleweight')

    )
    
    weight_class = models.CharField(max_length=30, choices=weight_options)

    picture = models.ImageField(upload_to="fighters_images",null=True,blank=True)

    def __str__(self):

        return self.name
