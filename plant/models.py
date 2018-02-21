from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Distribution(models.Model):
    distribution_id = models.IntegerField(db_column='Distribution_id', primary_key=True)  # Field name made lowercase.
    location_name = models.CharField(max_length=45, blank=True, null=True)
    location_vn = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distribution'
    def __str__(self):
        return self.location_name

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Familia(models.Model):
    id = models.IntegerField(primary_key=True)
    family = models.CharField(db_column='Family', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.family
    class Meta:
        managed = False
        db_table = 'familia'


class Genus(models.Model):
    id = models.IntegerField(primary_key=True)
    genus = models.CharField(db_column='Genus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.genus
    class Meta:
        managed = False
        db_table = 'genus'


class Metabolite(models.Model):
    metabolite_id = models.IntegerField(db_column='Metabolite_id', primary_key=True)  # Field name made lowercase.
    metabolite_name = models.CharField(db_column='Metabolite_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    casid = models.CharField(db_column='CASID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    inchikey = models.CharField(db_column='InChiKey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smiles = models.CharField(db_column='SMILES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=45, blank=True, null=True)  # Field name made lowercase.
    linkpubchem = models.CharField(db_column='LinkPubchem', max_length=250, blank=True, null=True)  # Field name made lowercase.
    linkknapsack = models.CharField(db_column='LinkKnapsack', max_length=45, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=500, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.metabolite_name
    class Meta:
        managed = False
        db_table = 'metabolite'


class Plant(models.Model):
    plant_id = models.IntegerField(db_column='Plant_id', primary_key=True)  # Field name made lowercase.
    plant_engname = models.CharField(max_length=45, blank=True, null=True)
    plant_vnname = models.CharField(max_length=45, blank=True, null=True)
    plant_image = models.CharField(max_length=500, blank=True, null=True)
    plant_image_2 = models.CharField(max_length=500, blank=True, null=True)
    plant_image_3 = models.CharField(max_length=500, blank=True, null=True)
    plant_image_4 = models.CharField(max_length=500, blank=True, null=True)
    familia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='Familia_id', blank=True, null=True)  # Field name made lowercase.
    genus = models.ForeignKey(Genus, models.DO_NOTHING, db_column='Genus_id', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.plant_engname
    class Meta:
        managed = False
        db_table = 'plant'


class PlantHasDistribution(models.Model):
    plant = models.ForeignKey(Plant, models.DO_NOTHING, db_column='Plant_id', primary_key=True)  # Field name made lowercase.
    distribution = models.ForeignKey(Distribution, models.DO_NOTHING, db_column='Distribution_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plant_has_distribution'
        unique_together = (('plant', 'distribution'),)


class PlantHasMetabolite(models.Model):
    plant = models.ForeignKey(Plant, models.DO_NOTHING, db_column='Plant_id', primary_key=True)  # Field name made lowercase.
    metabolite = models.ForeignKey(Metabolite, models.DO_NOTHING, db_column='Metabolite_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plant_has_metabolite'
        unique_together = (('plant', 'metabolite'),)


class PlantHasTherapeuticEffects(models.Model):
    plant = models.ForeignKey(Plant, models.DO_NOTHING, db_column='Plant_id', primary_key=True)  # Field name made lowercase.
    thera = models.ForeignKey('TherapeuticEffects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'plant_has_therapeutic_effects'
        unique_together = (('plant', 'thera'),)


class TherapeuticEffects(models.Model):
    thera_id = models.IntegerField(primary_key=True)
    thera_name = models.CharField(max_length=45, blank=True, null=True)
    def __str__(self):
        return self.thera_name
    class Meta:
        managed = False
        db_table = 'therapeutic_effects'
